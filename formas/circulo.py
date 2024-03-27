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

        # Converter as coordenadas cartesianas para as coordenadas do canvas
        x_canvas = largura / 2 + x * escala
        y_canvas = altura / 2 - y * escala

        # Desenhar o círculo
        self.canvas.create_oval(x_canvas - raio * escala, y_canvas - raio * escala,
                           x_canvas + raio * escala, y_canvas + raio * escala,
                           outline=cor, width=2)