from src.funcoes import (
    calcular_pontos,
    calcular_velocidade,
    colidiu_corpo,
    colidiu_parede,
    direcao_oposta,
    jogador_perdeu,
    jogador_venceu,
    limitar_valor,
    mover_cobra,
    tempo_restante,
)


def test_calcular_pontos():
    """Deve somar corretamente os pontos atuais com os pontos ganhos."""
    assert calcular_pontos(10, 5) == 15


def test_jogador_perdeu_com_zero_vidas():
    """Deve indicar derrota quando o total de vidas chega a zero."""
    assert jogador_perdeu(0) is True


def test_jogador_nao_perdeu_com_vidas():
    """Nao deve indicar derrota quando o jogador ainda tem vidas."""
    assert jogador_perdeu(3) is False


def test_limitar_valor_abaixo_do_minimo():
    """Deve retornar o limite minimo quando o valor informado for menor."""
    assert limitar_valor(-5, 0, 100) == 0


def test_limitar_valor_acima_do_maximo():
    """Deve retornar o limite maximo quando o valor informado for maior."""
    assert limitar_valor(150, 0, 100) == 100


def test_limitar_valor_dentro_do_intervalo():
    """Deve manter o valor original quando ele ja estiver no intervalo."""
    assert limitar_valor(50, 0, 100) == 50


def test_mover_cobra_mantem_tamanho():
    cobra = [(40, 20), (20, 20), (0, 20)]
    assert mover_cobra(cobra, (20, 0)) == [(60, 20), (40, 20), (20, 20)]


def test_colidiu_corpo_quando_cabeca_repetida():
    cobra = [(20, 20), (40, 20), (20, 20)]
    assert colidiu_corpo(cobra) is True


def test_colidiu_parede_fora_da_tela():
    assert colidiu_parede((-20, 100), 800, 600, 20) is True


def test_direcao_oposta_bloqueia_retorno_imediato():
    assert direcao_oposta((20, 0), (-20, 0)) is True
    assert direcao_oposta((20, 0), (0, 20)) is False


def test_tempo_restante_nao_fica_negativo():
    assert tempo_restante(90, 95) == 0


def test_jogador_venceu_quando_cobra_preenche_tabuleiro():
    largura = 800
    altura = 600
    tamanho_bloco = 20
    cobra_preenchida = [(0, 0)] * ((largura // tamanho_bloco) * (altura // tamanho_bloco - 2))
    cobra_incompleta = [(0, 0)] * 10

    assert jogador_venceu(cobra_preenchida, largura, altura, tamanho_bloco) is True
    assert jogador_venceu(cobra_incompleta, largura, altura, tamanho_bloco) is False


def test_calcular_velocidade_aumenta_com_pontos():
    assert calcular_velocidade(0) == 9
    assert calcular_velocidade(40) == 11
