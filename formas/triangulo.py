import tkinter as tk

class Desenhar:
    def __init__(self, canvas, conf, x1, y1, x2, y2, x3, y3):
        self.canvas = canvas
        largura = conf[0]
        altura = conf[1]
        escala = conf[2]

        # Converter as coordenadas cartesianas para as coordenadas do canvas
        x1_canvas = largura / 2 + x1 * escala
        y1_canvas = altura / 2 - y1 * escala
        x2_canvas = largura / 2 + x2 * escala
        y2_canvas = altura / 2 - y2 * escala
        x3_canvas = largura / 2 + x3 * escala
        y3_canvas = altura / 2 - y3 * escala

        # Desenhar o triângulo
        self.canvas.create_polygon(x1_canvas, y1_canvas, x2_canvas, y2_canvas, x3_canvas, y3_canvas,
                              outline="red", fill="", width=2)