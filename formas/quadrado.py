import tkinter as tk

class Desenhar:
    def __init__(self, canvas, conf, x, y, lado):
        self.canvas = canvas
        largura = conf[0]
        altura = conf[1]
        escala = conf[2]

        # Converter as coordenadas cartesianas para as coordenadas do canvas
        x_canvas = largura / 2 + x * escala
        y_canvas = altura / 2 - y * escala

        # Desenhar o quadrado
        self.canvas.create_rectangle(x_canvas - lado * escala / 2, y_canvas - lado * escala / 2,
                                x_canvas + lado * escala / 2, y_canvas + lado * escala / 2,
                                outline="blue", width=2)