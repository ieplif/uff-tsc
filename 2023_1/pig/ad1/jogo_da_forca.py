import random

# Jogo da forca
class Forca:
    """Método construtor"""
    def __init__(self, tema: str, palavra: str):
        self.tema = tema
        self.palavra = palavra
        self.letras_corretas = []
        self.letras_erradas = []
        self.vidas = 6


    """Método para adivinhar a letra"""
    def adivinhar(self, letra: str):
        if letra in self.palavra:
            self.letras_corretas.append(letra)
        else:
            self.letras_erradas.append(letra)
            self.vidas -= 1


    """Método para verificar se o jogador venceu"""
    def ganhou(self):
        if "_" not in self.palavra_escondida():
            return True
        return False


    """Método para verificar se o jogador perdeu"""
    def perdeu(self):
        return self.vidas == 0


    """Método para finalizar o jogo"""
    def fim_de_jogo(self):
        if self.ganhou():
            print(f"Parabéns, você ganhou! A palavra é {self.palavra}")
            
        else:
            print(f"Você perdeu! A palavra era {self.palavra}.")


    """Método para econder a palavra"""
    def palavra_escondida(self):
            status = ""
            for letra in self.palavra:
                if letra not in self.letras_corretas:
                    status += "_" 
                else:
                    status += letra
            return status


    """Método para desenhar a forca"""
    def desenhar_forca(self):  
        if len(self.letras_erradas) == 0:
            forca = ["-" * 9, "| /     |", "|       ", "|       ", "|      ", "|       ", "|      "]
            print(forca[0])
            print(forca[1])
            print(forca[2])
            print(forca[3])
            print(forca[4])
            print(forca[5])
            print(forca[6])
        elif len(self.letras_erradas) == 1:
            forca = ["-" * 9, "| /     |", "|       O", "|       ", "|      ", "|       ", "|      "]
            print(forca[0])
            print(forca[1])
            print(forca[2])
            print(forca[3])
            print(forca[4])
            print(forca[5])
            print(forca[6])
        elif len(self.letras_erradas) == 2:
            forca = ["-" * 9, "| /     |", "|       O", "|       ^", "|      ", "|       ", "|      "]
            print(forca[0])
            print(forca[1])
            print(forca[2])
            print(forca[3])
            print(forca[4])
            print(forca[5])
            print(forca[6])
        elif len(self.letras_erradas) == 3:
            forca = ["-" * 9, "| /     |", "|       O", "|       ^", "|      /|\ ", "|       ", "|      "]
            print(forca[0])
            print(forca[1])
            print(forca[2])
            print(forca[3])
            print(forca[4])
            print(forca[5])
            print(forca[6])
        elif len(self.letras_erradas) == 4:
            forca = ["-" * 9, "| /     |", "|       O", "|       ^", "|      /|\ ", "|       ^", "|      "]
            print(forca[0])
            print(forca[1])
            print(forca[2])
            print(forca[3])
            print(forca[4])
            print(forca[5])
            print(forca[6])
        elif len(self.letras_erradas) == 5:
            forca = ["-" * 9, "| /     |", "|       O", "|       ^", "|      /|\ ", "|       ^", "|      / \ "]
            print(forca[0])
            print(forca[1])
            print(forca[2])
            print(forca[3])
            print(forca[4])
            print(forca[5])
            print(forca[6])
        
        print(f"Letras erradas: {self.letras_erradas}")
        print(f"Letras corretas: {self.letras_corretas}")
        print(self.palavra_escondida())


"""Fazendo a leitura do arquivo com as palavras e temas"""
def obter_palavra_aleatoria():
    with open("palavras.txt", "r", encoding="utf-8") as arquivo:
        palavras = [linha.strip() for linha in arquivo]

    tema, palavra = random.choice(palavras).split(":")
    return tema, palavra


"""Método para jogar"""
def jogar_forca():
    while True:
        tema, palavra = obter_palavra_aleatoria()
        jogo = Forca(tema, palavra)
            
        print("Bem-vindo ao jogo da forca!")
        print(f"O tema é: {tema}")
        print(f"A palavra possui {len(palavra)} letras.")
                
        while True:   
            jogo.desenhar_forca()
                    
            letra = input("Digite uma letra: ").strip().lower()
                    
            if len(letra) != 1 or not letra.isalpha():
                print("Digite apenas uma letra!")
                    
                    
            if letra in jogo.letras_corretas or letra in jogo.letras_erradas:
                print("Essa letra já foi escolhida!")
                
                    
            jogo.adivinhar(letra)

                    
            if jogo.ganhou() or jogo.perdeu():
                jogo.fim_de_jogo()
                break

        resposta = input("Deseja jogar novamente? (s/n)").strip().lower()
        if resposta == "n":
            break
jogar_forca()
