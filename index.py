from plano import *
from formas import arco, circulo, quadrado, triangulo

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Plano Cartesiano")

    canvas = tk.Canvas(root, width=600, height=600, bg="white")
    canvas.pack()

    largura = 600
    altura = 600
    escala = 60

    plano = Plano(canvas, largura, altura, escala)
    arco.Desenhar(canvas, largura, altura, escala, 2, -2, 1, 0, 180)
    circulo.Desenhar(canvas, largura, altura, escala, -2, 2, 1)  #círculo com centro em (x, y) e raio r
    quadrado.Desenhar(canvas, largura, altura, escala, 2, 2, 2)  #quadrado com centro em (x, y) e altura h
    triangulo.Desenhar(canvas, largura, altura, escala, -2, -1, -3, -3, -1, -3)  #triângulo com vértices em (x1, y1), (x2, y2,) e (x3, y3)
    
    #arco.Desenhar(canvas, largura, altura, escala, 0, 0, 2, 90, 90)
    #arco.Desenhar(canvas, largura, altura, escala, 0, 4, 2, -90, 180)
    #arco.Desenhar(canvas, largura, altura, escala, 0, 0, 6, 0, 90)
    
    root.mainloop()