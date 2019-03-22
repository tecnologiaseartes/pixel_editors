"""
Editor de pixels - para padronagem Mexicana!
Sesc Av. Paulista - FestA 2019
"""

tam = 30

verde = color(0, 200, 0)
vermelho = color(200, 0, 0)
preto = color(0)
azul = color(0, 0, 200)
branco = color(255)
laranja = color(245, 143, 17)
roxo = color(183, 11, 175)
azul_marinho = color(0, 21, 100)

cores = [verde, azul_marinho,
         vermelho, preto, azul,
         branco, laranja, roxo]
pos_cores = 0

def setup():
    global cols, fils, grade
    size(600, 600)
    cols = width / tam
    fils = height / tam
    grade = [255] * cols * fils

    for i in range(fils):
        for j in range(cols):
            pos = j + cols * i
            if (i + j) % 2 == 0:
                grade[pos] = 255
            else:
                grade[pos] = color(200, 0, 0)

def draw():
    noStroke()
    for i in range(fils):
        for j in range(cols):
            x = j * tam
            y = i * tam
            pos = j + cols * i
            fill(grade[pos])
            if mouse_over(x, y, tam):
                fill(cores[pos_cores])
                if mousePressed:
                    grade[pos] = cores[pos_cores]
            rect(x, y, tam, tam)

    for i, cor in enumerate(cores):
        fill(cor)
        rect(i * 30, 0, 30, 30)
    noFill()
    strokeWeight(5)
    stroke(0)
    rect(pos_cores * 30, 0, 30, 30)

def mouse_over(x, y, tam):
    return (x < mouseX < x + tam and
            y < mouseY < y + tam)

def keyPressed():
    global pos_cores
    if key == ' ':
        pos_cores = (pos_cores + 1) % len(cores) 
