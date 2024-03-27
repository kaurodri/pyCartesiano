import tkinter as tk

class Desenhar:
    def __init__(self, canvas, conf, x, y, raio):
        self.canvas = canvas
        largura = conf[0]
        altura = conf[1]
        escala = conf[2]

        # Converter as coordenadas cartesianas para as coordenadas do canvas
        x_canvas = largura / 2 + x * escala
        y_canvas = altura / 2 - y * escala

        # Desenhar o círculo
        self.canvas.create_oval(x_canvas - raio * escala, y_canvas - raio * escala,
                           x_canvas + raio * escala, y_canvas + raio * escala,
                           outline="green", width=2)