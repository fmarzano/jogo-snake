# Snake Evolution

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

Este jogo é inspirado no clássico Snake. O jogador controla uma cobra que cresce ao coletar alimentos espalhados pelo mapa, tentando alcançar a meta de pontos antes que o tempo acabe.

## Integrantes do Grupo

* Fellipe Marzano
* Hector Paulo 
* Raul Rocha
* João Pedro Faria Lemos
* Lucas Oliveira Dias

## Estrutura do Projeto

* `main.py`: ponto de entrada da aplicação.
* `src/`: código-fonte principal do jogo.
* `assets/`: pastas reservadas para futuras imagens, fontes e sons.
* `data/`: arquivos persistentes (recorde/ranking).
* `tests/`: testes unitários com pytest.
* `docs/`: documentação do projeto, incluindo a proposta inicial.

## Descrição do Jogo

O jogador controla uma cobra que se move continuamente em uma grade. Durante a partida, alimentos aparecem em posições aleatórias e devem ser coletados para aumentar a pontuação e o tamanho da cobra.

O desafio é atingir 50 pontos dentro do tempo limite sem colidir com as paredes ou com o próprio corpo.

## Objetivo do Jogador

Coletar alimentos, crescer a cobra e alcançar 50 pontos antes que o tempo termine.

## Regras do Jogo

* O jogador controla a direção da cobra usando as setas do teclado.
* A cobra cresce ao coletar alimentos.
* Cada alimento coletado aumenta a pontuação em 10 pontos.
* A velocidade aumenta aos poucos conforme a pontuação cresce.
* Colidir com uma parede encerra a partida.
* Colidir com o próprio corpo encerra a partida.
* O jogador vence ao atingir 50 pontos.
* O jogo também encerra se o tempo de 90 segundos acabar.
* O recorde e o ranking das melhores pontuações são salvos na pasta `data/`.

## Controles

* Seta para cima: mover para cima
* Seta para baixo: mover para baixo
* Seta para esquerda: mover para esquerda
* Seta para direita: mover para direita
* Espaço: jogar novamente depois do fim da partida
* ESC: sair do jogo

## Como Executar o Projeto

### 1. Extrair o arquivo da entrega

Extraia o arquivo `.zip` e abra a pasta `Snake_Evolution` no terminal.

### 2. Entrar na Pasta do Projeto

```bash
cd Snake_Evolution
```

### 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 4. Executar o Jogo

```bash
python main.py
```

## Prévia Visual

Uma imagem de prévia pode ser gerada com:

```bash
python gerar_previa.py
```

O arquivo será salvo em `docs/previa.png`.

## Como Executar os Testes

```bash
python -m pytest
```

## Checklist Mínimo para Entrega

* [x] Preencher README com descrição, regras e controles do jogo.
* [x] Atualizar `docs/proposta.md` com a proposta do grupo.
* [x] Garantir que o jogo executa com `python main.py`.
* [x] Garantir que os testes passam com `pytest`.

## Tecnologias Utilizadas

* Python
* Pygame
* Pytest
* Git e GitHub

## Recursos Externos

O jogo nao utiliza imagens, sons ou fontes externas. A cobra, a comida, a grade e
os paineis sao desenhados diretamente com recursos do Pygame. O projeto utiliza
somente as bibliotecas listadas em `requirements.txt`.

## Possíveis Melhorias Futuras

* Tela inicial com menu.
* Menu de pausa.
* Efeitos sonoros.
* Animações.
* Diferentes temas de mapa.

## Observações

Esta e a versao final do projeto, organizada de forma modular e acompanhada de
documentacao, persistencia de dados e testes automatizados.
