import random
import tkinter
from tkinter import *
from tkinter.messagebox import showinfo

root = Tk()
root.title("Game")
root.geometry("300x300")

GameOver = False
Turn = 0
buttons = []
count = 0

#Определение первого хода
def first_turn():
    global Turn
    if random.randint(0, 1) == 1:
        Turn = "Player"
    else:
        Turn = "AI"
        AI()

#Поле
map = [0,1,2,3,4,5,6,7,8]

#Условия победы
victorys = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]

#cwadawdsa
def CheckVictory():
    global GameOver, count
    count += 1
    for line in victorys:
        X = 0
        O = 0
        for i in line:
            element = map[i]
            if element == "X":
                X += 1
            elif element == "O":
                O += 1
        if X == 3:
            showinfo(title="Игра окончена", message='Вы выйграли')
            GameOver = True
        if O == 3:
            showinfo(title="Игра окончена", message='Вы проиграли')
            GameOver = True
        if count == 9:
            showinfo(title="Игра окончена",message="Ничья")
            root.destroy()
            count += 1
            GameOver = True
    if GameOver == True:
        root.destroy()

def CheckMap(numX, numO):
    global CX
    for line in victorys:
        X = 0
        O = 0
        for i in line:
            element = map[i]
            if element == "X":
                X += 1
            elif element == "O":
                O += 1
        if numX == X and numO == O:
            for i in line:
                if map[i] != "X" and map[i] != "O":
                    CX = i
                    return True

def AI():
    global CX
    #Если есть выйгрыш одним ходом
    if CheckMap(0,2):
        ButtonClick(CX)
    #Если игрок может выйграть 1 ходом
    elif CheckMap(2, 0):
        ButtonClick(CX)
    #Если 1 своя и 0 игроков
    elif CheckMap(0, 1):
        ButtonClick(CX)
    #Если Центр свободен
    elif map[4] != "X" and map[4] != "O":
        ButtonClick(4)
    #В противном случае занимает 1 ячейку
    elif map[0] != "X" and map[0] != "O":
        ButtonClick(0)
    else:
        while True:
            a = random.randint(0,8)
            if map[a] == "X" or map[a] == "O":
                continue
            else:
                break
        ButtonClick(a)



class playButton():

    def __init__(self, cord):
        self.cord = cord
        x = cord % 3
        y = cord // 3
        self.button = Button(root, width=10, height=5, command=lambda x=cord: ButtonClick(x))
        canvas.create_window(x * 100 + 50, y * 100 + 50, window=self.button, width=100, height=100)


def ButtonClick(i):
    global Turn
    if Turn == "Player":
        buttons[i].button.configure(state=tkinter.DISABLED,text="X")
        map[i] = "X"
        CheckVictory()
        if not GameOver:
            Turn = "AI"
            AI()

    else:
        buttons[i].button.configure(state=tkinter.DISABLED,text="O")
        map[i] = "O"
        Turn = "Player"
        CheckVictory()



#Создание кнопок
def CreateButton():
    for i in range(9):
        buttons.append(playButton(i))



canvas = Canvas(bg="white", width=300, height=300)
canvas.grid()


#игровое поле
canvas.create_line(0,100,300,100)
canvas.create_line(0,200,300,200)
canvas.create_line(100,0,100,300)
canvas.create_line(200,0,200,300)
CreateButton()

first_turn()
root.mainloop()
