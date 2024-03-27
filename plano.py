import tkinter as tk

# Função para desenhar o plano cartesiano
class Plano:
    def __init__(self, canvas, conf):
        self.canvas = canvas
        largura = conf[0]
        altura = conf[1]
        escala = conf[2]
        
        # Desenha as linhas horizontais
        for i in range(-20, 21):
            self.canvas.create_line(0, altura/2 - i*escala, largura, altura/2 - i*escala, fill="gray")
    
        # Desenha as linhas verticais
        for i in range(-20, 21):
            self.canvas.create_line(largura/2 + i*escala, 0, largura/2 + i*escala, altura, fill="gray")
    
        # Desenha os eixos x e y
        self.canvas.create_line(0, altura/2, largura, altura/2, fill="black", width=2)
        self.canvas.create_line(largura/2, 0, largura/2, altura, fill="black", width=2)