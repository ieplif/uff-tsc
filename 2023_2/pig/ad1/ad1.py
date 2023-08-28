import random

class CampoMinado:
    """Classe Inicial em que são criadas as matrizaes bases do mapa e da revelação das bombas"""

    def __init__(self, tamanho, minas):
        self.tamanho = tamanho
        self.minas = minas
        self.mapa = [[0 for _ in range(tamanho)] for _ in range(tamanho)]
        self.revelado = [[False for _ in range(tamanho)] for _ in range(tamanho)]
        self.gerar_minas()

    """Método para gerar minas de acordo com o tamanho do mapa escolhido"""

    def gerar_minas(self):
        minas_colocadas = 0
        while minas_colocadas < self.minas:
            x = random.randint(0, self.tamanho - 1)
            y = random.randint(0, self.tamanho - 1)
            if self.mapa[x][y] != -1:
                self.mapa[x][y] = -1
                minas_colocadas += 1
                self.atualizar_vizinhos(x, y)

    """Método que ajusta as coordenadas para atualizar os vizinhos"""

    def atualizar_vizinhos(self, x, y):
        for i in range(max(0, x - 1), min(self.tamanho, x + 2)):
            for j in range(max(0, y - 1), min(self.tamanho, y + 2)):
                if self.mapa[i][j] != -1:
                    self.mapa[i][j] += 1

    """Método que faz a revelação no mapa de acordo com as coordenadas"""

    def revelar(self, x, y):
        if not (0 <= x < self.tamanho) or not (0 <= y < self.tamanho):
            return
        if self.revelado[x][y]:
            return

        self.revelado[x][y] = True

        if self.mapa[x][y] == 0:
            for i in range(max(0, x - 1), min(self.tamanho, x + 2)):
                for j in range(max(0, y - 1), min(self.tamanho, y + 2)):
                    self.revelar(i, j)

    """Método para imprimir o mapa inicial e o mapa com as revelações das bombas"""
    def imprimir_mapa(self):
        for x in range(self.tamanho):
            for y in range(self.tamanho):
                if not self.revelado[x][y]:
                    print(".", end=" ")
                elif self.mapa[x][y] == -1:
                    print("*", end=" ")
                else:
                    print(self.mapa[x][y], end=" ")
            print()

"""Método principal de execução"""

def main():
    while True:
        try:
            dificuldade = int(input("Escolha a dificuldade (tamanho do mapa e quantidade de minas): "))
            if dificuldade <= 0:
                print("Dificuldade deve ser maior que 0.")
                continue
            break
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

    jogo = CampoMinado(dificuldade, dificuldade)
    
    while True:
        jogo.imprimir_mapa()
        
        try:
            x = int(input("Digite a coordenada x: "))
            y = int(input("Digite a coordenada y: "))
        except ValueError:
            print("Por favor, insira coordenadas válidas.")
            continue
        
        if not (0 <= x < dificuldade) or not (0 <= y < dificuldade):
            print("Coordenadas fora dos limites do mapa.")
            continue
        
        if jogo.mapa[x][y] == -1:
            jogo.revelado[x][y] = True
            jogo.imprimir_mapa()
            print("BOMBA! Você perdeu!")
            break
        
        jogo.revelar(x, y)
        
        if all(all(revealed or jogo.mapa[x][y] == -1 for y, revealed in enumerate(linha)) for x, linha in enumerate(jogo.revelado)):
            jogo.imprimir_mapa()
            print("Parabéns! Você venceu!")
            break

if __name__ == "__main__":
    main()
