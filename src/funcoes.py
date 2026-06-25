def calcular_pontos(pontos_atual, pontos_ganhos):
    """Soma os pontos ganhos à pontuação atual."""
    return pontos_atual + pontos_ganhos


def tomar_dano(vida_atual, dano):
    """Reduz a vida atual com base no dano recebido."""
    return vida_atual - dano


def jogador_perdeu(vidas):
    """Indica se o jogador ficou sem vidas."""
    return vidas <= 0


def limitar_valor(valor, minimo, maximo):
    """Mantém um valor dentro do intervalo [minimo, maximo]."""
    if valor < minimo:
        return minimo
    if valor > maximo:
        return maximo
    return valor


def verificar_colisao(retangulo_1, retangulo_2):
    """Verifica sobreposição entre dois retângulos do Pygame."""
    return retangulo_1.colliderect(retangulo_2)


def mover_cobra(cobra, direcao):
    """Retorna a cobra com a cabeca movida na direcao informada."""
    cabeca_x, cabeca_y = cobra[0]
    passo_x, passo_y = direcao
    nova_cabeca = (cabeca_x + passo_x, cabeca_y + passo_y)
    return [nova_cabeca] + cobra[:-1]


def crescer_cobra(cobra, direcao):
    """Retorna a cobra com uma nova cabeca, mantendo o corpo anterior."""
    cabeca_x, cabeca_y = cobra[0]
    passo_x, passo_y = direcao
    nova_cabeca = (cabeca_x + passo_x, cabeca_y + passo_y)
    return [nova_cabeca] + cobra


def colidiu_parede(cabeca, largura, altura, tamanho_bloco):
    """Verifica se a cabeca da cobra saiu dos limites da tela."""
    x, y = cabeca
    return x < 0 or y < 0 or x >= largura or y >= altura


def colidiu_corpo(cobra):
    """Verifica se a cabeca encostou em alguma parte do corpo."""
    return cobra[0] in cobra[1:]


def direcao_oposta(direcao_atual, nova_direcao):
    """Impede que a cobra vire diretamente para o lado oposto."""
    return (
        direcao_atual[0] + nova_direcao[0] == 0
        and direcao_atual[1] + nova_direcao[1] == 0
    )


def calcular_velocidade(pontos):
    """Aumenta a velocidade aos poucos conforme a pontuacao cresce."""
    return 9 + pontos // 20


def tempo_restante(tempo_total, segundos_passados):
    """Calcula o tempo restante da partida sem permitir valor negativo."""
    restante = tempo_total - segundos_passados
    if restante < 0:
        return 0
    return restante


def jogador_venceu(cobra, largura, altura, tamanho_bloco):
    """Indica se a cobra ocupou todas as celulas disponiveis no tabuleiro."""
    colunas = largura // tamanho_bloco
    linhas_jogo = altura // tamanho_bloco - 2
    capacidade = colunas * linhas_jogo
    return len(cobra) >= capacidade
