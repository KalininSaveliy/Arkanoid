"""Главный модуль"""

import tkinter as tk
import time
from arkanoid_level import *
from arkanoid_block import *
from arkanoid_ball import *
from arkanoid_platform import *



# bind_id = None
# # создаем окно для игры
# window_width = 800
# window_height = 600
# root = tkinter.Tk()
# canvas = tkinter.Canvas(root, width=window_width, height=window_height, bg="black")
# canvas.pack(side=tkinter.TOP)
# is_running = False

# score = 0
# score_element = canvas.create_text(window_width / 20, window_height / 24, text='Score: ' + str(score), fill='black')

# def update_score(value):
#     score_element

# def main():
#     root.bind('<Double-Button-1>', new_game)  # запуск игры двойным щелчком
#     root.mainloop()


# def new_game(event):
#     global is_running
#     if is_running:
#         return
#     is_running = True
#     score = 0
#     text_score = canvas.create_text(window_width/20, window_height/24,
#                                     text='Score: ' + str(score), fill='white')
#     platform = Platform(canvas, window_width, window_height)
#     # создание чек-уровня, в переменную blocks записываються данные о блоках
#     blocks = create_check_level(canvas, window_width, window_height)
#     root.bind('<Key>', platform.move_platform)

class Game():
    def __init__(self, tk, width, height):
        self.tk = tk
        self.width = width
        self.height = height

        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width = self.width, height = self.height, bg = "black")
        self.canvas.pack(side = tk.TOP)

        self.background_color = "black"
        self.score_color = "white"

        # score
        self.score = 0
        self.score_element = self.canvas.create_text(self.width / 20, self.height / 24, text = "Score: " + str(self.score), fill = "black")

        # draw start screen
        self.root.bind("<Double-Button-1>", self.start_new_game)
        self.root.mainloop()

    # def check_point_in_box(self, x, y, box):
    #     if 9 
    # #write test collision

    def gamecycle(self):
        is_x_detected = False
        is_y_detected = False

        # check blocks collisions
        for b in self.blocks:

            class block_wrap:
                x = b.x
                y = b.y
                w = b.length
                h = b.thickness

            x_check =

            if self.ball.check_collision_x(block_wrap):
                is_x_detected = True

            if self.ball.check_collision_y(block_wrap):
                is_y_detected = True

            if is_x_detected and is_y_detected:
                break

        if is_x_detected:
            print("x block collision")

        if is_y_detected:
            print("y block collision")

        class platform_wrap:
            x = self.platform.x - self.platform.length / 2
            y = self.platform.y - self.platform.thickness / 2
            w = self.platform.length
            h = self.platform.thickness

        # platform check
        if self.ball.check_collision_x(platform_wrap):
            is_x_detected = True

        if self.ball.check_collision_y(platform_wrap):
            is_y_detected = True

        # playground boundaries check

        if self.ball.check_boundaries_x(self.width):
            is_x_detected = True

        if self.ball.check_boundaries_y(self.height):
            is_y_detected = True

        if is_x_detected:
            self.ball.dx *= -1

        if is_y_detected:
            self.ball.dy *= -1

        self.ball.move()

        self.root.after(50, self.gamecycle)

    def hide_score(self):
        self.canvas.itemconfig(self.score_element, fill = self.background_color)

    def show_score(self):
        self.canvas.itemconfig(self.score_element, fill = self.score_color)

    # we need to define level reference system
    def start_new_game(self, event):
        self.platform = Platform(self.canvas, self.width, self.height)
        self.blocks = create_check_level(self.canvas, self.width, self.height)
        self.ball = Ball(self.canvas, self.platform.x , self.platform.y - 10, 10, 10)
        self.root.bind('<Key>', self.platform.move_platform)
        self.show_score()
        self.gamecycle()

def main():
    game = Game(tk, 800, 600)

if __name__ == '__main__':
    main()