"""Главный модуль"""

import tkinter
from arkanoid_block import *
from arkanoid_ball import *
from arkanoid_platform import *


def main():
    global canvas, root, window_width, window_height
    window_width = 800
    window_height = 600
    # создаем окно для игры
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, width=window_width, height=window_height, bg="black")
    canvas.pack(side=tkinter.TOP)
    root.bind('<Double-Button-1>', new_game)  # запуск игры двойным щелчком
    root.mainloop()


def new_game(event):
    score = 0
    text_score = canvas.create_text(window_width/20, window_height/24,
                                    text='Score: ' + str(score), fill='white')
    platform = Platform(canvas, window_width, window_height)
    root.bind('<Key>', platform.move_platform)


main()
