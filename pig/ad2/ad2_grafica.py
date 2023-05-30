import tkinter as tk
from tkinter import messagebox
import random


# Função para obter tema e palavra
def obter_palavra_aleatoria():
    with open("palavras.txt", "r", encoding="utf-8") as arquivo:
        palavras = [linha.strip() for linha in arquivo]

    tema, palavra = random.choice(palavras).split(":")
    return tema, palavra

tema, palavra = obter_palavra_aleatoria()
tentativas_maximas = 6
tentativas = 0
letras_corretas = []

# Função para verificar se a letra está correta
def verificar_letra():
    global tentativas, letras_corretas
    letra = letra_entry.get()
    letra_entry.delete(0, tk.END)
    if letra in letras_corretas:
        messagebox.showinfo("Letra Repetida", f"A letra '{letra}' já foi escolhida!")
        return
    if letra in palavra:
        letras_corretas.append(letra)
        for i in range(len(palavra)):
            if palavra[i] == letra:
                palavra_label.config(text=palavra_label.cget("text")[:i] + letra + palavra_label.cget("text")[i + 1:])
        if palavra_label.cget("text") == palavra:
            messagebox.showinfo("Parabéns!", "Você venceu!")
            window.quit()
    else:
        tentativas += 1
        desenhar_forca()
        if tentativas == tentativas_maximas:
            messagebox.showinfo("Game Over", f"Você perdeu! A palavra era '{palavra}'.")
            window.quit()

# Função para desenhar a forca
def desenhar_forca():
    forca_canvas.delete("all")
    if tentativas >= 0:
        forca_canvas.create_line(20, 180, 180, 180)
        forca_canvas.create_line(100, 20, 100, 180)
        forca_canvas.create_line(100, 20, 180, 20)
        forca_canvas.create_line(180, 20, 180, 60)   
        forca_canvas.create_oval(160, 60, 200, 100)
    if tentativas >= 2:
        forca_canvas.create_line(180, 100, 180, 140)
    if tentativas >= 3:
        forca_canvas.create_line(180, 110, 160, 130)
    if tentativas >= 4:
        forca_canvas.create_line(180, 110, 200, 130)
    if tentativas >= 5:
        forca_canvas.create_line(180, 140, 200, 160)
    if tentativas >= 6:
        forca_canvas.create_line(180, 140, 160, 160)

# Configurar a janela
window = tk.Tk()
window.title("Jogo da Forca")
window.geometry("400x400")

# Configurar o canvas da forca
forca_canvas = tk.Canvas(window, width=400, height=200)
forca_canvas.pack()

lb_bem_vindo = tk.Label(window, text="Bem-vindo ao Jogo da Forca")
lb_bem_vindo.pack()

lb_dica =tk.Label(window, text= f"O tema é {tema} e a palavra possui {len(palavra)} letras.")
lb_dica.pack()

# Configurar a palavra oculta
palavra_label = tk.Label(window, text="_ " * len(palavra), font=("Helvetica", 14))
palavra_label.pack()

# Configurar o input de letra
letra_entry = tk.Entry(window, font=("Helvetica", 24))
letra_entry.pack()

# Configurar o botão de verificação de letra
verificar_button = tk.Button(window, text="Verificar", command=verificar_letra)
verificar_button.pack()

# Iniciar o jogo
window.mainloop()