import os
import random

import pygame

from src.config import (
    ALTURA_TELA,
    AMARELO,
    AZUL,
    BRANCO,
    CAMINHO_RANKING,
    CAMINHO_RECORDE,
    CELULAS_TOTAIS,
    CINZA,
    FPS,
    LARGURA_TELA,
    PONTOS_POR_COMIDA,
    PRETO,
    TAMANHO_BLOCO,
    TEMPO_PARTIDA,
    TITULO_JOGO,
    VERDE,
    VERDE_ESCURO,
    VERMELHO,
)
from src.dados import atualizar_ranking, carregar_ranking, carregar_recorde, salvar_recorde
from src.funcoes import (
    calcular_pontos,
    calcular_velocidade,
    colidiu_corpo,
    colidiu_parede,
    crescer_cobra,
    direcao_oposta,
    jogador_venceu,
    mover_cobra,
    tempo_restante,
)


def gerar_posicao_livre(cobra):
    """Gera uma posicao alinhada na grade e fora do corpo da cobra."""
    colunas = LARGURA_TELA // TAMANHO_BLOCO
    linhas = ALTURA_TELA // TAMANHO_BLOCO

    while True:
        posicao = (
            random.randrange(0, colunas) * TAMANHO_BLOCO,
            random.randrange(2, linhas) * TAMANHO_BLOCO,
        )
        if posicao not in cobra:
            return posicao


def criar_estado_inicial():
    """Monta o estado inicial da partida."""
    centro_x = (LARGURA_TELA // 2 // TAMANHO_BLOCO) * TAMANHO_BLOCO
    centro_y = (ALTURA_TELA // 2 // TAMANHO_BLOCO) * TAMANHO_BLOCO
    cobra = [
        (centro_x, centro_y),
        (centro_x - TAMANHO_BLOCO, centro_y),
        (centro_x - 2 * TAMANHO_BLOCO, centro_y),
    ]
    return {
        "modo": "menu",
        "cobra": cobra,
        "direcao": (TAMANHO_BLOCO, 0),
        "proxima_direcao": (TAMANHO_BLOCO, 0),
        "comida": gerar_posicao_livre(cobra),
        "pontos": 0,
        "mensagem_final": "",
        "ranking_salvo": False,
    }


def desenhar_texto(tela, fonte, texto, cor, x, y, centralizado=True):
    """Desenha um texto simples na tela."""
    superficie = fonte.render(texto, True, cor)
    rect = superficie.get_rect()
    if centralizado:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    tela.blit(superficie, rect)


def desenhar_grade(tela):
    """Desenha uma grade discreta para reforcar o movimento em blocos."""
    for x in range(0, LARGURA_TELA, TAMANHO_BLOCO):
        pygame.draw.line(tela, (44, 49, 58), (x, 40), (x, ALTURA_TELA))
    for y in range(40, ALTURA_TELA, TAMANHO_BLOCO):
        pygame.draw.line(tela, (44, 49, 58), (0, y), (LARGURA_TELA, y))


def desenhar_partida(tela, fonte, fonte_grande, estado, recorde, ranking, restante):
    """Renderiza todos os elementos visuais da partida."""
    tela.fill(CINZA)
    pygame.draw.rect(tela, PRETO, (0, 0, LARGURA_TELA, 40))
    desenhar_grade(tela)

    comida_rect = pygame.Rect(estado["comida"], (TAMANHO_BLOCO, TAMANHO_BLOCO))
    pygame.draw.rect(tela, VERMELHO, comida_rect, border_radius=5)

    for indice, parte in enumerate(estado["cobra"]):
        cor = VERDE if indice == 0 else VERDE_ESCURO
        rect = pygame.Rect(parte, (TAMANHO_BLOCO, TAMANHO_BLOCO))
        pygame.draw.rect(tela, cor, rect, border_radius=5)

    info = (
        f"Pontos: {estado['pontos']}  Recorde: {recorde}  "
        f"Tempo: {restante}s  Meta: preencher tudo"
    )
    desenhar_texto(tela, fonte, info, BRANCO, 12, 10, centralizado=False)

    if estado["mensagem_final"]:
        painel = pygame.Rect(150, 170, 500, 260)
        pygame.draw.rect(tela, PRETO, painel, border_radius=8)
        pygame.draw.rect(tela, AZUL, painel, width=2, border_radius=8)
        desenhar_texto(tela, fonte_grande, estado["mensagem_final"], AMARELO, 400, 220)
        desenhar_texto(tela, fonte, f"Pontuacao final: {estado['pontos']}", BRANCO, 400, 270)
        desenhar_texto(tela, fonte, "Espaco: jogar de novo | ESC: sair", BRANCO, 400, 315)
        melhores = "Ranking: " + ", ".join(str(valor) for valor in ranking[:5])
        desenhar_texto(tela, fonte, melhores, BRANCO, 400, 355)


def finalizar_partida(estado, mensagem):
    """Marca a partida como encerrada."""
    estado["mensagem_final"] = mensagem
    estado["modo"] = "fim"


def atualizar_partida(estado, segundos_passados):
    """Atualiza regras, movimento, pontuacao e condicoes de fim."""
    if estado["mensagem_final"]:
        return

    restante = tempo_restante(TEMPO_PARTIDA, segundos_passados)
    if restante == 0:
        finalizar_partida(estado, "Tempo esgotado!")
        return

    estado["direcao"] = estado["proxima_direcao"]
    proxima_cabeca = (
        estado["cobra"][0][0] + estado["direcao"][0],
        estado["cobra"][0][1] + estado["direcao"][1],
    )

    if proxima_cabeca == estado["comida"]:
        estado["cobra"] = crescer_cobra(estado["cobra"], estado["direcao"])
        estado["pontos"] = calcular_pontos(estado["pontos"], PONTOS_POR_COMIDA)
        if len(estado["cobra"]) >= CELULAS_TOTAIS:
            finalizar_partida(estado, "Vitoria!")
            return
        estado["comida"] = gerar_posicao_livre(estado["cobra"])
    else:
        estado["cobra"] = mover_cobra(estado["cobra"], estado["direcao"])

    if colidiu_parede(estado["cobra"][0], LARGURA_TELA, ALTURA_TELA, TAMANHO_BLOCO):
        finalizar_partida(estado, "Voce bateu na parede!")
    elif colidiu_corpo(estado["cobra"]):
        finalizar_partida(estado, "Voce bateu no corpo!")
    elif jogador_venceu(estado["cobra"], LARGURA_TELA, ALTURA_TELA, TAMANHO_BLOCO):
        finalizar_partida(estado, "Vitoria!")


def salvar_resultado_se_necessario(estado, recorde):
    """Atualiza recorde e ranking quando a partida termina."""
    if not estado["mensagem_final"] or estado["ranking_salvo"]:
        return recorde, carregar_ranking(CAMINHO_RANKING)

    if estado["pontos"] > recorde:
        recorde = estado["pontos"]
        salvar_recorde(CAMINHO_RECORDE, recorde)

    ranking = atualizar_ranking(CAMINHO_RANKING, estado["pontos"])
    estado["ranking_salvo"] = True
    return recorde, ranking


def desenhar_tela_inicial(tela, fonte, fonte_grande, recorde, ranking):
    """Desenha a tela inicial com instrucoes e recordes."""
    tela.fill(CINZA)
    desenhar_texto(tela, fonte_grande, TITULO_JOGO, AMARELO, LARGURA_TELA // 2, 120)
    desenhar_texto(
        tela,
        fonte,
        "Pressione ESPACO para jogar",
        BRANCO,
        LARGURA_TELA // 2,
        220,
    )
    desenhar_texto(
        tela,
        fonte,
        "Use as setas para mover a cobra",
        BRANCO,
        LARGURA_TELA // 2,
        260,
    )
    desenhar_texto(
        tela,
        fonte,
        f"Recorde: {recorde}",
        BRANCO,
        LARGURA_TELA // 2,
        320,
    )
    melhores = "Ranking: " + ", ".join(str(valor) for valor in ranking[:5])
    desenhar_texto(tela, fonte, melhores, BRANCO, LARGURA_TELA // 2, 360)


def gerar_previa(caminho_saida):
    """Gera uma imagem estatica para revisao visual do jogo."""
    os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
    pygame.init()
    tela = pygame.Surface((LARGURA_TELA, ALTURA_TELA))
    fonte = pygame.font.Font(None, 28)
    fonte_grande = pygame.font.Font(None, 48)
    estado = criar_estado_inicial()
    estado["pontos"] = 30
    estado["comida"] = (560, 300)
    ranking = [50, 40, 30, 20, 10]
    desenhar_partida(tela, fonte, fonte_grande, estado, 50, ranking, 72)
    pygame.image.save(tela, caminho_saida)
    pygame.quit()


def executar_jogo():
    """Executa o loop principal do jogo."""
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    fonte = pygame.font.Font(None, 28)
    fonte_grande = pygame.font.Font(None, 48)
    relogio = pygame.time.Clock()
    evento_movimento = pygame.USEREVENT + 1

    estado = criar_estado_inicial()
    recorde = carregar_recorde(CAMINHO_RECORDE)
    ranking = carregar_ranking(CAMINHO_RANKING)
    inicio_partida = None
    pygame.time.set_timer(evento_movimento, 0)

    rodando = True
    while rodando:
        segundos_passados = 0
        restante = TEMPO_PARTIDA
        if inicio_partida is not None:
            segundos_passados = (pygame.time.get_ticks() - inicio_partida) // 1000
            restante = tempo_restante(TEMPO_PARTIDA, segundos_passados)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    rodando = False
                elif evento.key in (pygame.K_SPACE, pygame.K_RETURN):
                    if estado["modo"] == "menu":
                        estado = criar_estado_inicial()
                        estado["modo"] = "jogo"
                        inicio_partida = pygame.time.get_ticks()
                        pygame.time.set_timer(
                            evento_movimento, 1000 // calcular_velocidade(estado["pontos"])
                        )
                    elif estado["modo"] == "fim":
                        estado = criar_estado_inicial()
                        estado["modo"] = "menu"
                        inicio_partida = None
                        pygame.time.set_timer(evento_movimento, 0)
                if estado["modo"] == "jogo":
                    direcoes = {
                        pygame.K_UP: (0, -TAMANHO_BLOCO),
                        pygame.K_DOWN: (0, TAMANHO_BLOCO),
                        pygame.K_LEFT: (-TAMANHO_BLOCO, 0),
                        pygame.K_RIGHT: (TAMANHO_BLOCO, 0),
                    }
                    if evento.key in direcoes:
                        nova_direcao = direcoes[evento.key]
                        if not direcao_oposta(estado["direcao"], nova_direcao):
                            estado["proxima_direcao"] = nova_direcao
            elif evento.type == evento_movimento and estado["modo"] == "jogo":
                atualizar_partida(estado, segundos_passados)
                pygame.time.set_timer(
                    evento_movimento, 1000 // calcular_velocidade(estado["pontos"])
                )

        recorde, ranking = salvar_resultado_se_necessario(estado, recorde)
        pygame.display.set_caption(
            f"{TITULO_JOGO} | Pontos: {estado['pontos']} | Recorde: {recorde}"
        )

        if estado["modo"] == "menu":
            desenhar_tela_inicial(tela, fonte, fonte_grande, recorde, ranking)
        else:
            desenhar_partida(tela, fonte, fonte_grande, estado, recorde, ranking, restante)

        pygame.display.flip()
        relogio.tick(FPS)

    pygame.quit()
