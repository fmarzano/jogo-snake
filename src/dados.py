def salvar_recorde(caminho_arquivo, pontuacao):
    """Salva a pontuação recorde em arquivo texto."""
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(str(pontuacao))


def carregar_recorde(caminho_arquivo):
    """Carrega o recorde salvo; retorna 0 se não existir valor válido."""
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().strip()

            if conteudo == "":
                return 0

            return int(conteudo)

    except FileNotFoundError:
        return 0
    except ValueError:
        return 0


def carregar_ranking(caminho_arquivo):
    """Carrega as pontuacoes do ranking em ordem decrescente."""
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            pontuacoes = []
            for linha in arquivo:
                linha = linha.strip()
                if linha:
                    pontuacoes.append(int(linha))
            return sorted(pontuacoes, reverse=True)
    except (FileNotFoundError, ValueError):
        return []


def salvar_ranking(caminho_arquivo, ranking):
    """Salva o ranking, mantendo uma pontuacao por linha."""
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        for pontuacao in ranking:
            arquivo.write(f"{pontuacao}\n")


def atualizar_ranking(caminho_arquivo, pontuacao, limite=5):
    """Inclui a pontuacao atual e retorna as melhores pontuacoes."""
    ranking = carregar_ranking(caminho_arquivo)
    ranking.append(pontuacao)
    ranking = sorted(ranking, reverse=True)[:limite]
    salvar_ranking(caminho_arquivo, ranking)
    return ranking
