from plano import *
from formas import circulo, quadrado, triangulo

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Plano Cartesiano")

    canvas = tk.Canvas(root, width=600, height=600, bg="white")
    canvas.pack()

    plano = Plano(canvas)
    circulo.desenhar(canvas, -2, 2, 1)  #círculo com centro em (x, y) e raio r
    quadrado.desenhar(canvas, 2, 2, 2)  #quadrado com centro em (x, y) e altura h
    triangulo.desenhar(canvas, -2, -1, -3, -3, -1, -3)  #triângulo com vértices em (x1, y1), (x2, y2,) e (x3, y3)
    root.mainloop()