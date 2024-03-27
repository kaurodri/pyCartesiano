from plano import *
from formas import arco, circulo, quadrado, triangulo

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Plano Cartesiano")

    conf = [600, 600, 60] # largura / altura / escala

    canvas = tk.Canvas(root, width=conf[0], height=conf[1], bg="white")
    canvas.pack()

    plano = Plano(canvas, conf)
    arco.Desenhar(canvas, conf, 2, -2, 1, 0, 180) #arco com centro em (x,y) e angulo em (a,b)
    circulo.Desenhar(canvas, conf, -2, 2, 1)  #círculo com centro em (x, y) e raio r
    quadrado.Desenhar(canvas, conf, 2, 2, 2)  #quadrado com centro em (x, y) e altura h
    triangulo.Desenhar(canvas, conf, -2, -1, -3, -3, -1, -3)  #triângulo com vértices em (x1, y1), (x2, y2,) e (x3, y3)
    
    #arco.Desenhar(canvas, conf, 0, 0, 2, 90, 90)
    #arco.Desenhar(canvas, conf, 0, 4, 2, -90, 180)
    #arco.Desenhar(canvas, conf, 0, 0, 6, 0, 90)
    
    root.mainloop()