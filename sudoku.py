# -*- coding: cp1252 -*-
from tkinter import *
from random import *
from tkinter import messagebox
import os
import time

LADO = 60

WIDTH = 40 + LADO * 9
HEIGHT = 40 + LADO * 9

class readGame:

    def __init__(self, difficulty):
        self.jogos_disponiveis = []
        self.cria_jogos(difficulty)
    
    def cria_jogos(self, difficulty):
        old_game = 0
        
        arq = open(gameDir + '\\' + difficulty + '.csv')
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
    find = find_empty()
    if not find:
        return True
    else:
        row, col = find
    for i in range(1,10):
        jogo[row][col][0] = i
        draw(1)
        #time.sleep(0.01)
        canvas.update()
        if jogo[row][col][2] == 'blue':
            if solver():
                return True
    jogo[row][col][0] = 0
    draw(1)
    return False    
        
def find_empty():
    for i in range(9):
        for j in range(9):
            if jogo[i][j][0] == 0:
                return(i,j)
    return None     

def chose_number(event):
    try:
        numero.set(int(event.char))
    except:
        pass

def click1(event):
    item = canvas.find_overlapping(event.x, event.y, event.x, event.y)
    tags = canvas.gettags(item[0])

    if tags[3] == 'NFIXO':
        jogo[int(tags[0])][int(tags[1])][0] = numero.get()
        draw(1)

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

    difficulty = readGame(dificuldade.get())
    jogo = difficulty.seleciona_jogo()

    draw(0)
    
    root.bind('<KeyPress>', chose_number)
    canvas.bind('<Button 1>', click1)

    root.mainloop()

def check_game():
    for i in range(9):
        for j in range(9):
            if jogo[i][j][1] == 'False' and jogo[i][j][0] > 0:
                jogo[i][j][2] = 'blue'
                for k in range(1, 9):
                    if jogo[i][j][0] == jogo[i-k][j][0] or jogo[i][j][0] == jogo[i][j-k][0]:
                        jogo[i][j][2] = 'red'
                        break
                         
def draw(inicio):
    global canvas

    if inicio == 0:
        canvas = Canvas(root, bg='white', width = WIDTH, height = HEIGHT, bd = 2, relief = RIDGE)
        canvas.grid(row = 1, column =0)
    else:
        check_game()
        canvas.delete(ALL)
    
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

def button():
    if dificuldade.get() == '':
        messagebox.showerror('Sudoku', 'Choose the difficulty')
    else:
        root2.destroy()
        start()
    
def begin():
    global root2, dificuldade
    root2 = Tk()
    root2.title('Sudoku')
    root2.resizable(FALSE,FALSE)

    label_frame = LabelFrame(root2, text = 'Sudoku')
    label_frame.grid(padx = 5, pady = 5)

    Label(label_frame, text = 'Choose the difficulty').grid(row = 0, column = 0, padx = 5, pady = 5)

    dificuldade = StringVar()
    Radiobutton(label_frame, text = 'Easy', variable = dificuldade, value = 'easy', indicatoron = 0).grid(row = 1, column = 0, padx = 5, pady = 5)
    Radiobutton(label_frame, text = 'Medium', variable = dificuldade, value = 'medium', indicatoron = 0).grid(row = 2, column = 0, padx = 5, pady = 5)
    Radiobutton(label_frame, text = 'Hard', variable = dificuldade, value = 'hard', indicatoron = 0).grid(row = 3, column = 0, padx = 5, pady = 5)

    Button(label_frame, text = 'Start', command = button).grid(row = 4, column = 0, padx = 5, pady = 5)

    root2.mainloop()

gameDir = os.path.dirname(os.path.realpath(__file__))
begin()
