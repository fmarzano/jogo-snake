# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na Semana 1 do projeto.

## 1. Nome provisório do jogo

> Snake Evolution

## 2. Integrantes do grupo

* Nome 1: Fellipe Marzano
* Nome 2: Hector
* Nome 3: Raul
* Nome 4: João Pedro

## 3. Tipo de jogo

Tipo escolhido pelo grupo:

> Snake

## 4. Descrição geral do jogo

Descrição:

> O jogo será inspirado no clássico Snake. O jogador controla uma cobra que se move pela tela em busca de alimentos. Cada alimento coletado faz a cobra crescer e aumenta a pontuação. O desafio é continuar coletando alimentos sem colidir com as paredes ou com o próprio corpo da cobra.

## 5. Objetivo do jogador

Objetivo:

> Coletar o maior número possível de alimentos, aumentando a pontuação e o tamanho da cobra sem sofrer colisões.

## 6. Regras principais

Regras do grupo:

* A cobra se move continuamente pelo mapa.
* O jogador controla a direção da cobra usando o teclado.
* Cada alimento coletado aumenta a pontuação e o tamanho da cobra.
* Se a cobra colidir com uma parede, o jogo termina.
* Se a cobra colidir com o próprio corpo, o jogo termina.

## 7. Condição de vitória

Condição de vitória:

> O jogador vence ao atingir 50 pontos.

## 8. Condição de derrota ou encerramento

Condição de derrota ou encerramento:

> O jogo termina quando a cobra colide com uma parede ou com o próprio corpo.

## 9. Elementos previstos no jogo

### Jogador ou elemento principal

Descrição:

> Uma cobra controlada pelo jogador através das setas do teclado.

### Obstáculos, inimigos ou desafios

Descrição:

> As paredes do mapa e o próprio corpo da cobra funcionam como obstáculos que devem ser evitados.

### Itens, alvos ou objetos de interação

Descrição:

> Alimentos aparecem aleatoriamente no mapa e devem ser coletados pela cobra.

### Pontuação, vidas, tempo ou progresso

Descrição:

> Cada alimento coletado aumenta a pontuação em 1 ponto. O progresso é medido pela pontuação e pelo tamanho da cobra.

## 10. Controles previstos

Controles do grupo:

* Seta para cima: mover para cima
* Seta para baixo: mover para baixo
* Seta para esquerda: mover para esquerda
* Seta para direita: mover para direita
* ESC: sair do jogo

## 11. Organização inicial do código

Organização planejada:

* `main.py`: inicia o jogo;
* `src/jogo.py`: contém o loop principal;
* `src/cobra.py`: controla a movimentação e crescimento da cobra;
* `src/comida.py`: gera e controla os alimentos;
* `src/config.py`: configurações do jogo;
* `src/dados.py`: armazenamento de recordes.

## 12. Recursos externos previstos

Recursos previstos:

> Imagens gratuitas para a cobra e os alimentos, sons gratuitos para coleta de itens e efeitos de fim de jogo.

## 13. Principais dificuldades esperadas

Dificuldades previstas:

* Implementação correta do crescimento da cobra.
* Detecção de colisões.
* Salvamento e carregamento de recordes.

## 14. Escopo mínimo para a entrega final

Escopo mínimo:

> A versão mínima do jogo terá uma cobra controlada pelo teclado, alimentos gerados aleatoriamente, sistema de crescimento, sistema de pontuação, detecção de colisões e tela de fim de jogo.

## 15. Possíveis melhorias, caso haja tempo

Melhorias possíveis:

* Tela inicial.
* Sistema de ranking com recordes.
* Aumento progressivo da velocidade conforme a pontuação aumenta.
