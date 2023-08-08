# AD1 1o semestre de 2023

## 1 - Objetivo
Implementar um jogo da forca utilizando orientação a objetos e Python. As
palavras usadas para o jogo devem estar em português e devem ser acentuadas
corretamente.

## 1.1 - Descrição do Jogo
O jogo da Forca é um jogo de adivinhação de palavras, no qual o jogador deve
acertar a palavra proposta tendo como dica apenas o número de letras que
compõem a palavra e o tema ao qual esta palavra está ligada.

O jogador deve tentar adivinhar a palavra dando palpites sobre letras que
possam pertencer à palavra proposta. A cada letra errada, uma parte do corpo
de um boneco (“o enforcado”) deve ser desenhada.  Se o desenho do enforcado for completado antes de o jogador acertar a palavra proposta, o jogador perde o jogo. Caso contrário, o jogador ganha o jogo.

As partes desenhadas do enforcado devem seguir a ordem: cabeça, tronco,
braços e pernas, resultando em um máximo de 5 erros sem que o jogador perca
o jogo.


## 1.2 - Requisitos

* O jogo deve ser desenvolvido utilizando orientaçãao a objetos;

* A evoluçãoao do desenho do enforcado deve ser mostrada no terminal, juntamente com a forca, a cada nova tentativa do jogador;

* As palavras devem ser obtidas a partir de um arquivo contendo um dicionário de palavras;

* As palavras dos diferentes temas podem estar em um mesmo arquivo ou
em arquivos separados, à escolha do programador;

* A palavra e o tema definidos para um turno devem ser obtidos de forma
aleatória;

* A quantidade mínima de temas é 5 e de palavras é 20;

* O jogador deve ser informado sobre o tema ao qual a palavra pertence e
quantas letras a palavra possui;

* Ao final do jogo, perdendo ou ganhando, o jogador deve poder escolher
sair do jogo ou jogar novamente;

* O código desenvolvido deve estar documentado.

## 2 - Bibliotecas

Sugere-se utilizar a biblioteca random para escolher aleatoriamente uma palavra
a partir de um arquivo texto com uma palavra por linha.

## 3 - Testes

* O(s) arquivo(s) de palavras deve(m) existir, caso não exista(m), um erro
deve ser gerado;

* Deve-se garantir que o usuário insira em seu palpite apenas uma letra por
tentativa;

* Deve-se garantir que caracteres especiais não possam ser usados #, $, %,
$, etc., à exceçãao do hífen.


## 4 - O que Entregar

Deve ser enviado o código fonte em mídia digital e o programa deverá rodar em
ambiente Linux com Python 3 recomendável que rode em Python 2 também.

Não fornecemos código “gabarito” nesse curso, visto que não existe gabarito
de programa. Cada pessoa implementa a mesma funcionalidade e resolve o
mesmo problema de formas distintas.




