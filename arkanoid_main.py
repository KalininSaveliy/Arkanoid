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

        self.debug_line = self.canvas.create_line(0,0,1,1)  

        # draw start screen
        self.root.bind("<Double-Button-1>", self.start_new_game)
        self.root.mainloop()


    def dist_if_collide(self, bx, by, rx, ry, fx, fy, sx, sy):
        def vec2(bx, by, x, y):
            return [x - bx, y - by]

        def dist(v):
            return (v[0] ** 2 + v[1] ** 2) ** 0.5

        def cross(f, s):
            return f[0] * s[1] - s[0] * f[1]

        first  = vec2(bx, by, fx, fy)
        second = vec2(bx, by, sx, sy)
        ray    = vec2(bx, by, rx, ry)

        first_area  = cross(first, ray)
        second_area = cross(ray, second)
        area        = cross(first, second)

        do_calc_dist = False

        # проверяем пересечение
        if area > 0:
            if first_area > 0 and second_area > 0:
                do_calc_dist = True
        elif area < 0:
            if first_area < 0 and second_area < 0:
                do_calc_dist = True
        elif first_area == 0:
                return min(dist(vec2(ray[0], ray[1], first[0], first[1])), dist(vec2(ray[0], ray[1], second[0], second[1])))

        if do_calc_dist:
            return area / (first_area + second_area)
            self.canvas.create_line(x1, y1, x2, y2, fill="orange")
        else:
            return math.inf

    def gamecycle(self):

        self.r = math.inf
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0

        def process_rect(x, y, w, h):
            # global r, x1, x2, y1, y2 # wtf didn't work but must. just trying to access gamecycle variables ...

            def process_line(x1, y1, x2, y2):

                ndist = self.dist_if_collide(self.ball.x, self.ball.y, self.ball.dx, self.ball.dy, x1, y1, x2, y2)
                if self.r > ndist:
                    self.x1 = x1
                    self.y1 = y1
                    self.x2 = x2
                    self.y2 = y2
                    self.r = ndist

            process_line(x, y, x+w, y)
            process_line(x, y, x, y+h)
            process_line(x+w, y+h, x+w, y)
            process_line(x+w, y+h, x, y+h)
            # def process_line(x, y, w, h)
            # ndist = self.dist_if_collide(self.ball.x, self.ball.y, self.ball.dx, self.ball.dy, x - self.ball.r, y - self.ball.r, x + w + self.ball.r, y - self.ball.r)
            # if self.r > ndist:
            #     self.x1 = x - self.ball.r
            #     self.y1 = y - self.ball.r
            #     self.x2 = x + w + self.ball.r
            #     self.y2 = y - self.ball.r
            #     self.r = ndist

            # # process_line(x - self.ball.r / 2, y - self.ball.r / 2, x + w + self.ball.r / 2, y - self.ball.r / 2)
            # # process_line(x - self.ball.r / 2, y - self.ball.r / 2, x - self.ball.r / 2, y + h + self.ball.r / 2)
            # # process_line(x + w + self.ball.r / 2, y + h + self.ball.r / 2, x + w + self.ball.r / 2, y - self.ball.r / 2)
            # # process_line(x + w + self.ball.r / 2, y + h + self.ball.r / 2, x - self.ball.r / 2, y + h + self.ball.r / 2)

            # ndist = self.dist_if_collide(self.ball.x, self.ball.y, self.ball.dx, self.ball.dy, x - self.ball.r, y - self.ball.r, x - self.ball.r, y + h + self.ball.r)
            # if self.r > ndist:
            #     self.x1 = x - self.ball.r
            #     self.y1 = y - self.ball.r
            #     self.x2 = x - self.ball.r
            #     self.y2 = y + h + self.ball.r
            #     self.r = ndist

            # ndist = self.dist_if_collide(self.ball.x, self.ball.y, self.ball.dx, self.ball.dy, x + w + self.ball.r, y + h + self.ball.r, x + w + self.ball.r, y - self.ball.r)
            # if self.r > ndist:
            #     self.x1 = x + w + self.ball.r
            #     self.y1 = y + h + self.ball.r
            #     self.x2 = x + w + self.ball.r
            #     self.y2 = y - self.ball.r
            #     self.r = ndist

            # ndist = self.dist_if_collide(self.ball.x, self.ball.y, self.ball.dx, self.ball.dy, x + w + self.ball.r, y + h + self.ball.r, x - self.ball.r, y + h + self.ball.r)
            # if self.r > ndist:
            #     self.x1 = x + w + self.ball.r
            #     self.y1 = y + h + self.ball.r
            #     self.x2 = x - self.ball.r
            #     self.y2 = y + h + self.ball.r
            #     self.r = ndist


        # # check blocks collisions
        for b in self.blocks:
            process_rect(b.x, b.y, b.length, b.thickness)

        # platform collision check
        process_rect(self.platform.x - self.platform.length / 2, self.platform.y - self.platform.thickness / 2, self.platform.length, self.platform.thickness)

        # boundaries check
        process_rect(0, 0, self.width, self.height)

        print(self.ball.x, self.ball.y, self.ball.dx, self.ball.dy, 1/self.r)
        self.canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill="white")
        
        if self.r > 1:
            oldx = self.ball.x
            oldy = self.ball.y

            if self.y2 - self.y1 == 0: # cross [1, 0], [x2-x1, y2-y1]
                self.ball.x += self.ball.dx
                self.ball.y += 1 / self.r * self.ball.dy - (1 - 1/self.r) * self.ball.dy
                self.ball.dy *= -1
            else:
                self.ball.y += self.ball.dy
                self.ball.x += 1 / self.r * self.ball.dx - (1 - 1/self.r) * self.ball.dx
                self.ball.dx *= -1
            self.canvas.move(self.ball, self.ball.x - oldx, self.ball.x - oldy)
        else:
            self.ball.x += self.ball.dx
            self.ball.y += self.ball.dy
            self.canvas.move(self.ball.ball, self.ball.dx, self.ball.dy)

        self.debug_line = self.canvas.create_line(self.ball.x, self.ball.y, self.ball.x + self.ball.dx, self.ball.y + self.ball.dy, fill="#00ff00")



        self.root.after(250, self.gamecycle)

    def hide_score(self):
        self.canvas.itemconfig(self.score_element, fill = self.background_color)

    def show_score(self):
        self.canvas.itemconfig(self.score_element, fill = self.score_color)

    # we need to define level reference system
    def start_new_game(self, event):
        self.platform = Platform(self.canvas, self.width, self.height)
        self.blocks = create_check_level(self.canvas, self.width, self.height)
        self.ball = Ball(self.canvas, self.platform.x , self.platform.y - 20, 5, 10)
        self.root.bind('<Key>', self.platform.move_platform)
        self.show_score()
        self.gamecycle()

def main():
    game = Game(tk, 800, 600)

if __name__ == '__main__':
    main()