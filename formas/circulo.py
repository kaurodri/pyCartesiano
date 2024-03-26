import tkinter as tk

class desenhar:
    def __init__(self, canvas, x, y, raio):
        self.canvas = canvas
        escala = 60  # Escala para desenhar os pontos
        largura = 600  # Largura do canvas
        altura = 600   # Altura do canvas

        # Converter as coordenadas cartesianas para as coordenadas do canvas
        x_canvas = largura / 2 + x * escala
        y_canvas = altura / 2 - y * escala

        # Desenhar o círculo
        self.canvas.create_oval(x_canvas - raio * escala, y_canvas - raio * escala,
                           x_canvas + raio * escala, y_canvas + raio * escala,
                           outline="green", width=2)