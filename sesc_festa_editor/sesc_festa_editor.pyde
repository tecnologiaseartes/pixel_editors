"""
Editor de pixels - para padronagem Mexicana!
Sesc Av. Paulista - FestA 2019
"""
from __future__ import unicode_literals
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
scroll_paleta = False
edita_cor = False
control_apertado = False
mirror_tosco = 0

def setup():
    global cols, fils, grade
    size(600, 600)
    cols = width / tam
    fils = height / tam
    grade = [branco] * cols * fils
    help()

def draw():
    global pos_cores, tam_pincel, salva_pdf
    if salva_pdf:
        beginRecord(PDF, "Mexicano#####.pdf")

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

    paleta_e_sliders()

def mouse_over(x, y, tp):
    def dentro(mx, my):
        if tp == tam:
            return (x < mx < x + tam and
                    y < my < y + tam)
        else:
            return dist(x + tam / 2, y + tam / 2, mx, my) < tp
    if mirror_tosco == 0:
        return dentro(mouseX, mouseY)
    elif mirror_tosco == 1:
        return dentro(mouseX, mouseY) or dentro(width - mouseX, mouseY)
    elif mirror_tosco == 2:
        return dentro(mouseX, mouseY) or dentro(mouseX, height - mouseY)
    else:
        return (dentro(mouseX, mouseY) or
                dentro(mouseX, height - mouseY) or
                dentro(width - mouseX, mouseY) or
                dentro(width - mouseX, height - mouseY)  
                )
        
def keyPressed():
    global pos_cores, est_pincel, paleta, salva_pdf
    if key == ' ':
        pos_cores = (pos_cores + 1) % len(cores)
    if key == '+' or key == '=':
        est_pincel = (1 + est_pincel) % 3
        println("Pincel modo: "+ str(est_pincel))
    if key == '-' and est_pincel > 0:
        est_pincel -= 1    # tam_pincel = tam_pincel - 1
        println("Pincel modo: "+ str(est_pincel))
    if key == "p":
        paleta = not paleta
    if key == "s":
        saveFrame("tela######.png")
    if key == "S":
        salva_pdf = True
    if keyCode == SHIFT:
        global scroll_paleta
        scroll_paleta = True
    if keyCode == CONTROL:
        global control_apertado
        control_apertado = True

    if key == "c":
        global edita_cor
        edita_cor = not edita_cor
    if key == "m":
        global mirror_tosco
        mirror_tosco = (mirror_tosco + 1) % 4
    if key == "h": help()
    
def keyReleased():
    if keyCode == SHIFT:
        global scroll_paleta
        scroll_paleta = False
    if keyCode == CONTROL:
        global control_apertado
        control_apertado = False

def mouseWheel(event):
    global tam_pincel, pos_cores

    if scroll_paleta:
        pos_cores += event.getCount()
        if pos_cores < 0:
            pos_cores = len(cores) - 1
        elif pos_cores > len(cores) - 1:
            pos_cores = 0
    elif edita_cor:
        if control_apertado:
            vel = 5
        else:
            vel = 1
        c = cores[pos_cores]
        r, g, b = red(c), green(c), blue(c)
        #  rect(50, 100, 510, 50)
        pos_y = 100
        if (50 < mouseX < 560 and pos_y < mouseY < pos_y + 50):
            r += event.getCount() * vel
            if r < 0:
                r = 0
            elif r > 255:
                r = 255
        pos_y = 200
        if (50 < mouseX < 560 and pos_y < mouseY < pos_y + 50):
            g += event.getCount() * vel
            if g < 0:
                g = 0
            elif g > 255:
                g = 255
        pos_y = 300
        if (50 < mouseX < 560 and pos_y < mouseY < pos_y + 50):
            b += event.getCount() * vel
            if b < 0:
                b = 0
            elif b > 255:
                b = 255
        # REMONTA COR EDITADA
        cores[pos_cores] = color(r, g, b)
    else:
        tam_pincel += event.getCount()
        if tam_pincel < 1:
            tam_pincel = 1


def paleta_e_sliders():
    # SLIDERS EDITOR DE COR
    if edita_cor:
        pushStyle()
        stroke(0)
        fill(255)
        # R
        rect(50, 100, 510, 50)
        line(50, 125, 50 + 510, 125)
        r = red(cores[pos_cores])
        fill(255, 0, 0)
        ellipse(50 + r * 2, 125, 50, 50)
        fill(255)
        textAlign(CENTER, CENTER)
        textSize(18)
        text(str(int(r)), 50 + r * 2, 125)
        # G
        rect(50, 200, 510, 50)
        line(50, 225, 50 + 510, 225)
        g = green(cores[pos_cores])
        fill(0, 255, 0)
        ellipse(50 + g * 2, 225, 50, 50)
        fill(255)
        textAlign(CENTER, CENTER)
        textSize(18)
        text(str(int(g)), 50 + g * 2, 225)
        # B
        rect(50, 300, 510, 50)
        line(50, 325, 50 + 510, 325)
        b = blue(cores[pos_cores])
        fill(0, 0, 255)
        ellipse(50 + b * 2, 325, 50, 50)
        fill(255)
        textAlign(CENTER, CENTER)
        textSize(18)
        text(str(int(b)), 50 + b * 2, 325)
        popStyle()

    # PALETA DE CORES
    if paleta:
        for i, cor in enumerate(cores):
            fill(cor)
            rect(i * 30, 0, 30, 30)
        noFill()
        strokeWeight(5)
        stroke(0)
        rect(pos_cores * 30, 0, 30, 30)

def help():
    from javax.swing import JOptionPane
    message = """    Teclas:
            'c' editar cor ativa
            'm' modos de espelhamento
            's' salva PNG
            'S' salva PDF
            'p' mostra/esconde paleta de cores
            ScrollWheel muda tamanho do pincel
            SHIFT + ScrollWheel muda cor
            ESPACO muda cor
            '=' Estilos de pincel: normal/xadrez par/xadrez ímpar
            'h' Para este painel de ajuda
            """
    ok = JOptionPane.showMessageDialog(None, message)
