"""Главный модуль"""

import tkinter
from arkanoid_level import *
from arkanoid_block import *
from arkanoid_ball import *
from arkanoid_platform import *



bind_id = None
# создаем окно для игры
window_width = 800
window_height = 600
root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=window_width, height=window_height, bg="black")
canvas.pack(side=tkinter.TOP)
is_running = False


def main():
    root.bind('<Double-Button-1>', new_game)  # запуск игры двойным щелчком
    root.mainloop()


def new_game(event):
    global is_running
    if is_running:
        return
    is_running = True
    score = 0
    text_score = canvas.create_text(window_width/20, window_height/24,
                                    text='Score: ' + str(score), fill='white')
    platform = Platform(canvas, window_width, window_height)
    # создание чек-уровня, в переменную blocks записываються данные о блоках
    blocks = create_check_level(canvas, window_width, window_height)
    root.bind('<Key>', platform.move_platform)


main()
