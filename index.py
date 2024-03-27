from plano import *
from formas import arco, circulo, quadrado, triangulo

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Plano Cartesiano")

    arc = arco              #centro em (x,y), raio r e angulo em (a,b)
    cir = circulo           #centro em (x, y) e raio r
    qua = quadrado          #centro em (x, y) e altura h
    tri = triangulo         #vértices em (x1, y1), (x2, y2,) e (x3, y3)
    conf = [600, 600, 60]   # largura / altura / escala

    canvas = tk.Canvas(root, width=conf[0], height=conf[1], bg="white")
    canvas.pack()

    plano = Plano(canvas, conf)
    arc.Desenhar(canvas, conf, "red", [[2, -2], 1, [0, 180]])
    cir.Desenhar(canvas, conf, "red", [[-2, 2], 1])
    qua.Desenhar(canvas, conf, "red", [[2, 2], 2])
    tri.Desenhar(canvas, conf, "red", [[-2, -1], [-3, -3], [-1, -3]])

    root.mainloop()