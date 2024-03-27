import tkinter as tk

class Desenhar:
    def __init__(self, canvas, conf, cor, coord):
        self.canvas = canvas

        #index.py
        largura = conf[0]
        altura = conf[1]
        escala = conf[2]
        x = coord[0][0]
        y = coord[0][1]
        raio = coord[1]
        angulo_inicial = coord[2][0]
        angulo_final = coord[2][1]

        #coordenadas cartesianas para as coordenadas do canvas
        x_canvas = largura / 2 + x * escala
        y_canvas = altura / 2 - y * escala

        #
        self.canvas.create_arc(x_canvas - raio * escala, y_canvas - raio * escala,
                               x_canvas + raio * escala, y_canvas + raio * escala,
                               start=angulo_inicial, extent=angulo_final,
                               outline=cor, width=2)