import tkinter as tk

class Quadrado:
    def __init__(self, canvas, x, y, lado):
        self.canvas = canvas
        escala = 60  # Escala para desenhar os pontos
        largura = 600  # Largura do canvas
        altura = 600   # Altura do canvas

        # Converter as coordenadas cartesianas para as coordenadas do canvas
        x_canvas = largura / 2 + x * escala
        y_canvas = altura / 2 - y * escala

        # Desenhar o quadrado
        self.canvas.create_rectangle(x_canvas - lado * escala / 2, y_canvas - lado * escala / 2,
                                x_canvas + lado * escala / 2, y_canvas + lado * escala / 2,
                                outline="blue", width=2)