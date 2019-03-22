"""
Editor de pixels - para padronagem Mexicana!
Sesc Av. Paulista - FestA 2019
"""
add_library('pdf')

tam = 10
tam_pincel = 1
est_pincel = 0
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

paleta = True
salva_pdf = False

def setup():
    global cols, fils, grade
    size(600, 600)
    cols = width / tam
    fils = height / tam
    grade = [roxo] * cols * fils

    # for i in range(fils):
    #     for j in range(cols):
    #         pos = j + cols * i
    #         if (i + j) % 2 == 0:
    #             grade[pos] = 255
    #         else:
    #             grade[pos] = color(200, 0, 0)

def draw():
    global pos_cores, tam_pincel
    if salva_pdf:
        beginRecord(PDF, "Mexicano.pdf")
    
    noStroke()  # formas sem contorno
    for i in range(fils):
        for j in range(cols):
            x = j * tam
            y = i * tam
            pos = j + cols * i
            fill(grade[pos])
            if mouse_over(x, y, tam_pincel * tam):
                fill(cores[pos_cores])
                if mousePressed:
                    if mouseButton == LEFT:
                        if est_pincel == 0:
                            grade[pos] = cores[pos_cores]
                        elif est_pincel == 1:
                            if (i + j) % 2 == 0:
                                grade[pos] = cores[pos_cores]
                        elif est_pincel == 2:
                            if (i + j) % 2 == 1:
                                grade[pos] = cores[pos_cores]
                                
                    if mouseButton == RIGHT:
                        grade[pos] = branco
                    if mouseButton == CENTER:
                        if mouse_over(x, y, 1 * tam):
                            for i, cor in enumerate(cores):
                                if cor == grade[pos]:
                                    pos_cores = i
                                    break

            rect(x, y, tam, tam)
    if salva_pdf:
        endRecord()
        global salva_pdf
        salva_pdf = False
        
    # PALETA DE CORES
    if paleta:
        for i, cor in enumerate(cores):
            fill(cor)
            rect(i * 30, 0, 30, 30)
        noFill()
        strokeWeight(5)
        stroke(0)
        rect(pos_cores * 30, 0, 30, 30)

def mouse_over(x, y, tp):
    if tp == tam:
        return (x < mouseX < x + tam and
                y < mouseY < y + tam)
    else:
        return dist(x + tam / 2, y + tam / 2, mouseX, mouseY) < tp


def keyPressed():
    global pos_cores, est_pincel, paleta
    if key == ' ':
        pos_cores = (pos_cores + 1) % len(cores)
    if key == '+' or key == '=':
        est_pincel += 1    # tam_pincel = tam_pincel + 1
    if key == '-' and est_pincel > 0:
        est_pincel -= 1    # tam_pincel = tam_pincel - 1
    if key == "p":
        paleta = not paleta
    if key == "s":
        saveFrame("tela######.png")
    if key == "S":
        global salva_pdf
        salva_pdf = True

def mouseWheel(event):
    global tam_pincel
    tam_pincel += event.getCount()
    if tam_pincel < 1:
        tam_pincel = 1
