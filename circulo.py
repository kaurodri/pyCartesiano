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

# Função para desenhar um círculo
def desenhar_circulo(canvas, x, y, raio):
    escala = 60  # Escala para desenhar os pontos
    largura = 600  # Largura do canvas
    altura = 600   # Altura do canvas
    
    # Converter as coordenadas cartesianas para as coordenadas do canvas
    x_canvas = largura / 2 + x * escala
    y_canvas = altura / 2 - y * escala
    
    # Desenhar o círculo
    canvas.create_oval(x_canvas - raio * escala, y_canvas - raio * escala,
                       x_canvas + raio * escala, y_canvas + raio * escala,
                       outline="green", width=2)

# Função principal
def main():
    root = tk.Tk()
    root.title("Plano Cartesiano")

    canvas = tk.Canvas(root, width=600, height=600, bg="white")
    canvas.pack()

    desenhar_plano_cartesiano(canvas)
    desenhar_circulo(canvas, -2, 2, 1)  # Desenha um círculo com centro em (-2, 3) e raio 2

    root.mainloop()

if __name__ == "__main__":
    main()
