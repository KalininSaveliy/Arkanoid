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
        self.gamecycle()
        self.root.mainloop()

    def gamecycle(self):
        # is_x_detected = False
        # is_y_detected = False

        # # check blocks collisions
        # for b in self.blocks

        #     if self.ball.check_collision_x(b):
        #         is_x_detected = True

        #     if self.ball.check_collision_y(b):
        #         is_y_detected = True

        #     if is_x_detected and is_y_detected:
        #         break

        # # platform check
        # if self.ball.check_collision_x(self.platform)
        #     is_x_detected = True

        # if self.ball.check_collision_y(self.platform)
        #     is_y_detected = True

        


        self.root.after(50, self.gamecycle)

    def hide_score(self):
        self.canvas.itemconfig(self.score_element, fill = self.background_color)

    def show_score(self):
        self.canvas.itemconfig(self.score_element, fill = self.score_color)

    # we need to define level reference system
    def start_new_game(self, event):
        self.platform = Platform(self.canvas, self.width, self.height)
        self.blocks = create_check_level(self.canvas, self.width, self.height)
        self.ball = Ball()
        self.root.bind('<Key>', self.platform.move_platform)
        self.show_score()

def main():
    game = Game(tk, 800, 600)

if __name__ == '__main__':
    main()