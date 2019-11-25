"""Главный модуль"""

import tkinter
from arkanoid_block import *
from arkanoid_ball import *
from arkanoid_platform import *


def main():
    global canvas
    window_width = 800
    window_height = 600
    # создаем окно для игры
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, width=window_width, height=window_height, bg="black")
    canvas.pack(side=tkinter.TOP)
    canvas.bind('<Double-Button-1>', new_game)  # запуск игры двойным щелчком
    root.mainloop()


def new_game(event):
    score = 0
    text_score = canvas.create_text(40, 25, text='Score: ' + str(score), fill='white')


main()
