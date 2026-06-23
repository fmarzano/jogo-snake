# Snake Evolution

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

Este jogo é inspirado no clássico Snake, onde o jogador controla uma cobra que cresce ao coletar alimentos espalhados pelo mapa.

## Integrantes do Grupo

* Fellipe Marzano
* Hector
* Raul
* João Pedro
* Lucas Oliveira Dias

## Estrutura do Projeto

* `main.py`: ponto de entrada da aplicação.
* `src/`: código-fonte principal do jogo.
* `assets/`: imagens, fontes e sons.
* `data/`: arquivos persistentes (recorde/ranking).
* `tests/`: testes unitários com pytest.
* `docs/`: documentação do projeto, incluindo a proposta inicial.

## Descrição do Jogo

O jogador controla uma cobra que se move continuamente pelo mapa. Durante a partida, alimentos aparecem em posições aleatórias e devem ser coletados para aumentar a pontuação e o tamanho da cobra.

O desafio é sobreviver o máximo possível sem colidir com as paredes ou com o próprio corpo.

## Objetivo do Jogador

Coletar o maior número possível de alimentos para aumentar a pontuação e crescer a cobra, evitando colisões que encerram a partida.

## Regras do Jogo

* O jogador controla a direção da cobra usando as setas do teclado.
* A cobra cresce ao coletar alimentos.
* Cada alimento coletado aumenta a pontuação.
* Colidir com uma parede encerra a partida.
* Colidir com o próprio corpo encerra a partida.
* O jogador vence ao atingir a pontuação definida pelo grupo.

## Controles

* Seta para cima: mover para cima
* Seta para baixo: mover para baixo
* Seta para esquerda: mover para esquerda
* Seta para direita: mover para direita
* ESC: sair do jogo

## Como Executar o Projeto

### 1. Clonar o Repositório

```bash
git clone LINK_DO_REPOSITORIO
```

### 2. Entrar na Pasta do Projeto

```bash
cd NOME_DA_PASTA
```

### 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 4. Executar o Jogo

```bash
python main.py
```

## Como Executar os Testes

```bash
python -m pytest
```

## Checklist Mínimo para Entrega

* [x] Preencher README com descrição, regras e controles do jogo.
* [x] Atualizar `docs/proposta.md` com a proposta do grupo.
* [ ] Garantir que o jogo executa com `python main.py`.
* [ ] Garantir que os testes passam com `pytest`.

## Tecnologias Utilizadas

* Python
* Pygame
* Pytest
* Git e GitHub

## Possíveis Melhorias Futuras

* Sistema de ranking.
* Aumento progressivo da velocidade.
* Tela inicial.
* Menu de pausa.
* Efeitos sonoros.
* Animações.
* Diferentes temas de mapa.

## Observações

O projeto será desenvolvido de forma incremental durante o semestre, buscando manter o código organizado, modularizado e documentado para facilitar a manutenção e evolução do jogo.
