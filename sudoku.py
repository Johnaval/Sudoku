# -*- coding: cp1252 -*-
from tkinter import *
from random import *
from tkinter import messagebox
import os

LADO = 60

WIDTH = 40 + LADO * 9
HEIGHT = 40 + LADO * 9

class Facil:

    def __init__(self):
        self.jogos_disponiveis = []
        self.cria_jogos()

    def cria_jogos(self):
        old_game = 0
        
        arq = open(gameDir + '\easy.csv')
        for linha in arq:
            linha = linha.split(';')
            if linha[0] != 'GAME':
                jogo[int(linha[2])][int(linha[3])][0] = int(linha[1])
                jogo[int(linha[2])][int(linha[3])][1] = 'TRUE'
                jogo[int(linha[2])][int(linha[3])][2] = 'blue'
            else:
                try:
                    self.jogos_disponiveis.append(jogo)
                except: pass
                
                temp_list = []
                temp2_list = []
                jogo = []
                for i in range(9):
                    for j in range(9):
                        temp2_list.append(0)
                        temp2_list.append('False')
                        temp2_list.append('red')
                        temp_list.append(temp2_list)
                        temp2_list = []
                    jogo.append(temp_list)
                    temp_list = []

        arq.close()
    
        

    def seleciona_jogo(self):
        return self.jogos_disponiveis[randint(0, len(self.jogos_disponiveis) - 1)]

class Medio:

    def __init__(self):
        self.jogos_disponiveis = []
        self.cria_jogos()

    def cria_jogos(self):
        old_game = 0

        arq = open(gameDir + '\medium.csv')
        for linha in arq:
            linha = linha.split(';')
            if linha[0] != 'GAME':
                jogo[int(linha[2])][int(linha[3])][0] = int(linha[1])
                jogo[int(linha[2])][int(linha[3])][1] = 'TRUE'
                jogo[int(linha[2])][int(linha[3])][2] = 'blue'
            else:
                try:
                    self.jogos_disponiveis.append(jogo)
                except: pass
                
                temp_list = []
                temp2_list = []
                jogo = []
                for i in range(9):
                    for j in range(9):
                        temp2_list.append(0)
                        temp2_list.append('False')
                        temp2_list.append('red')
                        temp_list.append(temp2_list)
                        temp2_list = []
                    jogo.append(temp_list)
                    temp_list = []

        arq.close()
    
        

    def seleciona_jogo(self):
        return self.jogos_disponiveis[randint(0, len(self.jogos_disponiveis) - 1)]

class Dificil:

    def __init__(self):
        self.jogos_disponiveis = []
        self.cria_jogos()

    def cria_jogos(self):
        old_game = 0

        arq = open(gameDir + '\hard.csv')
        for linha in arq:
            linha = linha.split(';')
            if linha[0] != 'GAME':
                jogo[int(linha[2])][int(linha[3])][0] = int(linha[1])
                jogo[int(linha[2])][int(linha[3])][1] = 'TRUE'
                jogo[int(linha[2])][int(linha[3])][2] = 'blue'
            else:
                try:
                    self.jogos_disponiveis.append(jogo)
                except: pass
                
                temp_list = []
                temp2_list = []
                jogo = []
                for i in range(9):
                    for j in range(9):
                        temp2_list.append(0)
                        temp2_list.append('False')
                        temp2_list.append('red')
                        temp_list.append(temp2_list)
                        temp2_list = []
                    jogo.append(temp_list)
                    temp_list = []

        arq.close()
    
        

    def seleciona_jogo(self):
        return self.jogos_disponiveis[randint(0, len(self.jogos_disponiveis) - 1)]

def solver():
    messagebox.showinfo('Sudoku', 'Not ready yet')
        

def apertou(event):
    try:
        numero.set(int(event.char))
    except:
        pass

def click1(event):
    item = canvas.find_overlapping(event.x, event.y, event.x, event.y)
    tags = canvas.gettags(item[0])

    if tags[3] == 'NFIXO':
        jogo[int(tags[0])][int(tags[1])][0] = numero.get()
        constroi_jogo(1)

def start():
    global numero, root, jogo
    root = Tk()
    root.title('Sudoku')
    root.resizable(FALSE,FALSE)

    numero = IntVar()
    numero.set(0)

    frame = Frame(root)
    frame.grid(row = 0, column = 0)
    Label(frame, text = 'Number: ').grid(row = 0, column = 0, padx = 5, pady = 5)
    Label(frame, textvariable = numero).grid(row = 0, column = 1, padx = 5, pady = 5)
    Solver_Button = Button(frame, command = solver, text = "Solve")
    Solver_Button.grid(row = 0, column = 2, padx = 5, pady = 5)

    if dificuldade.get() == 'facil':
        facil = Facil()
        jogo = facil.seleciona_jogo()
    elif dificuldade.get() == 'medio':
        medio = Medio()
        jogo = medio.seleciona_jogo()
    elif dificuldade.get() == 'dificil':
        dificil = Dificil()
        jogo = dificil.seleciona_jogo()

    constroi_jogo(0)
    
    root.bind('<KeyPress>', apertou)
    canvas.bind('<Button 1>', click1)

    root.mainloop()

def verifica_jogo():
    for i in range(9):
        for j in range(9):
            check_var = True
            direction = '-x'
            linha = i
            coluna = j
            local = jogo[i][j]
            valor = local[0]
            if local[1] == 'False' and local[0] != 0:
                while check_var == True:
                    if direction == '-x':
                        coluna -= 1
                        ponto = faz_verificacao(linha, coluna, valor)
                        if ponto == 1:
                            jogo[i][j][2] = 'red'
                            check_var = False
                        elif ponto == 0:
                            jogo[i][j][2] = 'blue'
                        elif ponto == 2:
                            coluna = j
                            direction = '+x'
                    elif direction == '+x':
                        coluna += 1
                        ponto = faz_verificacao(linha, coluna, valor)
                        if ponto == 1:
                            jogo[i][j][2] = 'red'
                            check_var = False
                        elif ponto == 0:
                            jogo[i][j][2] = 'blue'
                        elif ponto == 2:
                            coluna = j
                            direction = '-y'
                    elif direction == '-y':
                        linha -= 1
                        ponto = faz_verificacao(linha, coluna, valor)
                        if ponto == 1:
                            jogo[i][j][2] = 'red'
                            check_var = False
                        elif ponto == 0:
                            jogo[i][j][2] = 'blue'
                        elif ponto == 2:
                            linha = i
                            direction = '+y'
                    elif direction == '+y':
                        linha += 1
                        ponto = faz_verificacao(linha, coluna, valor)
                        if ponto == 1:
                            jogo[i][j][2] = 'red'
                            check_var = False
                        elif ponto == 0:
                            jogo[i][j][2] = 'blue'
                        elif ponto == 2:
                            check_var = False
                        

def faz_verificacao(i,j,valor):
    if i < 0 or i > 8 or j < 0 or j > 8:
        return 2
    else:
        if jogo[i][j][0] != valor:
            return 0
        elif jogo[i][j][0] == valor:
            return 1

def verifica_fim():
    check_var = True

    for i in range(9):
        for j in range(9):
            if jogo[i][j][2] == 'red':
                check_var = False

    if check_var == True:
        canvas.delete(ALL)
        canvas.create_text(WIDTH/2, HEIGHT/2, text='Congratulations, you completed the game', anchor = N)
            
        

    

def constroi_jogo(inicio):
    global canvas

    try:
        canvas.delete(ALL)
    except: pass

    if inicio == 0:
        canvas = Canvas(root, bg='white', width = WIDTH, height = HEIGHT, bd = 2, relief = RIDGE)
        canvas.grid(row = 1, column =0)
    else:
        verifica_jogo()
    

    for i in range(9):
        for j in range(9):
            if jogo[i][j][1] == 'TRUE':
                canvas.create_rectangle(20 + LADO * j, 20 + LADO * i, 20 + LADO *(j+1), 20 + LADO * (i+1), fill='white', tag = (i, j, jogo[i][j][0],'FIXO'))
                canvas.create_text(20 + LADO * j + LADO/2, 20 + LADO * i + LADO/2, text=jogo[i][j][0], font=('Purisa', 16), tag = (i, j, jogo[i][j][0], 'FIXO'))
            else:
                canvas.create_rectangle(20 + LADO * j, 20 + LADO * i, 20 + LADO *(j+1), 20 + LADO * (i+1), fill='white', tag = (i, j, jogo[i][j][0],'NFIXO'))
                if jogo[i][j][0] != 0:
                    canvas.create_text(20 + LADO * j + LADO/2, 20 + LADO * i + LADO/2, text=jogo[i][j][0], font=('Purisa', 16), fill=jogo[i][j][2], tag = (i, j, jogo[i][j][0], 'NFIXO'))
                    
                

    for i in range(3):
        for j in range(3):
            canvas.create_rectangle(20 + LADO * (i * 3), 20 + LADO * (j * 3), 20 + LADO * ((i + 1) * 3), 20 + LADO * ((j + 1) * 3), width = 3)

    verifica_fim()

def botao():
    if dificuldade.get() == '':
        messagebox.showerror('Sudoku', 'Choose the difficulty')
    else:
        root2.destroy()
        start()
    

def abrir():
    global root2, dificuldade
    root2 = Tk()
    root2.title('Sudoku')
    root2.resizable(FALSE,FALSE)

    label_frame = LabelFrame(root2, text = 'Sudoku')
    label_frame.grid(padx = 5, pady = 5)

    Label(label_frame, text = 'Choose the difficulty').grid(row = 0, column = 0, padx = 5, pady = 5)

    dificuldade = StringVar()
    Radiobutton(label_frame, text = 'Easy', variable = dificuldade, value = 'facil', indicatoron = 0).grid(row = 1, column = 0, padx = 5, pady = 5)
    Radiobutton(label_frame, text = 'Medium', variable = dificuldade, value = 'medio', indicatoron = 0).grid(row = 2, column = 0, padx = 5, pady = 5)
    Radiobutton(label_frame, text = 'Hard', variable = dificuldade, value = 'dificil', indicatoron = 0).grid(row = 3, column = 0, padx = 5, pady = 5)

    Button(label_frame, text = 'Start', command = botao).grid(row = 4, column = 0, padx = 5, pady = 5)

    root2.mainloop()

gameDir = os.path.dirname(os.path.realpath(__file__))
abrir()
