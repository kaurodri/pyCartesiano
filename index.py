from plano import *
from formas import circulo, quadrado, triangulo

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Plano Cartesiano")

    canvas = tk.Canvas(root, width=600, height=600, bg="white")
    canvas.pack()

    plano = Plano(canvas)
    circulo.desenhar(canvas, -2, 2, 1)  # Desenha um círculo com centro em (-2, 3) e raio 2
    quadrado.desenhar(canvas, 1, 1, 2)  # Desenha um quadrado com vértice superior esquerdo em (1, 1) e lado de comprimento 2
    triangulo.desenhar(canvas, -1, -1, -4, -2, -2, -4)  # Desenha um triângulo com vértices em (1, 1), (4, 2) e (2, 4)
    root.mainloop()