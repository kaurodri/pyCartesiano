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
        lado = coord[1]

        # Converter as coordenadas cartesianas para as coordenadas do canvas
        x_canvas = largura / 2 + x * escala
        y_canvas = altura / 2 - y * escala

        # Desenhar o quadrado
        self.canvas.create_rectangle(x_canvas - lado * escala / 2, y_canvas - lado * escala / 2,
                                x_canvas + lado * escala / 2, y_canvas + lado * escala / 2,
                                outline=cor, width=2)