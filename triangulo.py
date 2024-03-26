import tkinter as tk

# Função para desenhar o plano cartesiano
def desenhar_plano_cartesiano(canvas):
    largura = 600  # Largura do canvas
    altura = 600   # Altura do canvas
    escala = 60    # Escala para desenhar os pontos
    
    # Desenha as linhas horizontais
    for i in range(-5, 6):
        canvas.create_line(0, altura/2 - i*escala, largura, altura/2 - i*escala, fill="gray")
    
    # Desenha as linhas verticais
    for i in range(-5, 6):
        canvas.create_line(largura/2 + i*escala, 0, largura/2 + i*escala, altura, fill="gray")
    
    # Desenha os eixos x e y
    canvas.create_line(0, altura/2, largura, altura/2, fill="black", width=2)
    canvas.create_line(largura/2, 0, largura/2, altura, fill="black", width=2)

# Função para desenhar um triângulo
def desenhar_triangulo(canvas, x1, y1, x2, y2, x3, y3):
    escala = 60  # Escala para desenhar os pontos
    largura = 600  # Largura do canvas
    altura = 600   # Altura do canvas
    
    # Converter as coordenadas cartesianas para as coordenadas do canvas
    x1_canvas = largura / 2 + x1 * escala
    y1_canvas = altura / 2 - y1 * escala
    x2_canvas = largura / 2 + x2 * escala
    y2_canvas = altura / 2 - y2 * escala
    x3_canvas = largura / 2 + x3 * escala
    y3_canvas = altura / 2 - y3 * escala
    
    # Desenhar o triângulo
    canvas.create_polygon(x1_canvas, y1_canvas, x2_canvas, y2_canvas, x3_canvas, y3_canvas,
                          outline="red", fill="", width=2)

# Função principal
def main():
    root = tk.Tk()
    root.title("Plano Cartesiano")

    canvas = tk.Canvas(root, width=600, height=600, bg="white")
    canvas.pack()

    desenhar_plano_cartesiano(canvas)
    desenhar_triangulo(canvas, 1, 1, 4, 2, 2, 4)  # Desenha um triângulo com vértices em (1, 1), (4, 2) e (2, 4)

    root.mainloop()

if __name__ == "__main__":
    main()
