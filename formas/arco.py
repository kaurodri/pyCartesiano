import tkinter as tk

class Desenhar:
    def __init__(self, canvas, conf, x, y, raio, angulo_inicial, angulo_final):
        self.canvas = canvas
        largura = conf[0]
        altura = conf[1]
        escala = conf[2]

        #coordenadas cartesianas para as coordenadas do canvas
        x_canvas = largura / 2 + x * escala
        y_canvas = altura / 2 - y * escala

        #
        self.canvas.create_arc(x_canvas - raio * escala, y_canvas - raio * escala,
                               x_canvas + raio * escala, y_canvas + raio * escala,
                               start=angulo_inicial, extent=angulo_final,
                               outline="orange", width=2)