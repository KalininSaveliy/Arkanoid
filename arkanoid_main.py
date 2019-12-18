"""Главный модуль"""

import tkinter as tk
import time
from arkanoid_level import *
from arkanoid_block import *
from arkanoid_ball import *
from arkanoid_platform import *



class Game:

    def __init__(self, tk, width, height):
        self.tk = tk
        self.width = width
        self.height = height

        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height, bg="black")
        self.canvas.pack(side=tk.TOP)

        # bottom buttons
        self.menu_frame = tk.Frame(self.root, width=self.width)
        self.menu_frame.pack(side = self.tk.BOTTOM)

        self.start_button = tk.Button(self.menu_frame, text="Start New Game!", command = self.start_handler, width = 60, height = 20)
        self.exit_button  = tk.Button(self.menu_frame, text="Exit!", command = self.exit_handler, width = 60, height = 20)
        self.start_button.pack(side = self.tk.LEFT)
        self.exit_button.pack(side = self.tk.LEFT)

        self.background_color = "black"
        self.score_color = "white"
        self.lifes_color = "white"

        # collision
        self.last_x = 0
        self.last_y = 0
        self.saved_x = -1000
        self.saved_y = -1000

        # score
        self.current_score = 0
        self.score_element = self.canvas.create_text(self.width / 20, self.height / 24,
                                                     text="Score: " + str(self.current_score), fill="black")

        self.congrats_element = self.canvas.create_text(self.width / 2, self.height / 2, text="Congratulations! Try beat next one!")
        self.gameover_element = self.canvas.create_text(self.width / 2, self.height / 2, text="Opss... Just give it a try. :)")
        self.current_lifes = 3
        self.max_lifes = 3
        self.lifes_element = self.canvas.create_text(self.width - self.width / 20, self.height / 24, fill="black")

        self.need_stop_loop = False
        self.current_level = 0
        self.need_load_level = 0

        self.platform = None
        self.blocks = []
        self.ball = None

        self.after_id = []

        # draw start screen
        # self.root.bind("<Double-Button-1>", self.start_new_game)
        # self.root.unbind("<Double-Button-1>")
        # FiX ME: unbind херово работает
        self.root.mainloop()

    def start_handler(self):
        self.need_load_level = 0
        self.start_new_game()
        self.current_level = 0

    def exit_handler(self):
        self.root.delete("all")

    # b->r - ray, f-s - segment
    def is_cross (self, bx, by, rx, ry, fx, fy, sx, sy):
        # self.canvas.create_line(fx, fy, sx, sy, fill="#00ffff")
        # self.canvas.create_line(bx, by, rx, ry, fill="#ff8800")
        def vec2 (bx, by, x, y):
            return [x - bx, y - by]

        def dist (v):
            return (v[0] ** 2 + v[1] ** 2) ** 0.5

        def cross (f, s):
            return f[0] * s[1] - s[0] * f[1]

        first = vec2(bx, by, fx, fy)
        second = vec2(bx, by, sx, sy)
        ray = vec2(bx, by, rx, ry)

        first_area = cross(first, ray)
        second_area = cross(ray, second)
        area = cross(first, second)

        do_calc_dist = False

        # проверяем пересечение
        if area == 0 and first_area == 0:
            if dist(vec2(ray[0], ray[1], first[0], first[1])) < dist(vec2(ray[0], ray[1], second[0], second[1])):
                self.last_x = fx
                self.last_y = fy
                return True
            else:
                self.last_x = sx
                self.last_y = sy
                return True

        if area > 0 and first_area > 0 and second_area > 0 or area < 0 and first_area < 0 and second_area < 0:
            self.last_x = bx + ray[0] * area / (first_area + second_area)
            self.last_y = by + ray[1] * area / (first_area + second_area)
            return True

        return False

    def gamecycle (self):
        if self.need_stop_loop:
            return True
        # global debug_lines
        # for l in debug_lines:
        #     (self.canvas).delete(l)

        self.saved_x = -1000
        self.saved_y = -1000

        def process_line (x1, y1, x2, y2):
            if self.is_cross(self.ball.x, self.ball.y, self.ball.x + self.ball.dx, self.ball.y + self.ball.dy, x1, y1,
                             x2, y2):
                if (self.saved_x - self.ball.x) ** 2 + (self.saved_y - self.ball.y) ** 2 > (
                        self.last_x - self.ball.x) ** 2 + (self.last_y - self.ball.y) ** 2:
                    self.saved_x = self.last_x
                    self.saved_y = self.last_y
                    self.was_block = self.now_blocks
                    self.update_block = self.now_blocks
                    # line_length = 3
                    # debug_lines.append(self.canvas.create_line(self.saved_x - line_length, self.saved_y - line_length, self.saved_x + line_length, self.saved_y + line_length, fill="white"))
                    # debug_lines.append(self.canvas.create_line(self.saved_x - line_length, self.saved_y + line_length, self.saved_x + line_length, self.saved_y - line_length, fill="white"))
                    # debug_lines.append(self.canvas.create_line(self.ball.x, self.ball.y, self.saved_x, self.saved_y, fill="#338866"))

                    # save segment
                    self.segment_x1 = x1
                    self.segment_x2 = x2

        def process_rect (x, y, w, h):
            process_line(x, y, x + w, y)
            process_line(x, y, x, y + h)
            process_line(x + w, y + h, x, y + h)
            process_line(x + w, y + h, x + w, y)

        self.now_blocks = True
        self.was_block = False
        # # check blocks collisions
        for b in range(len(self.blocks)):
            process_rect(self.blocks[b].x, self.blocks[b].y, self.blocks[b].length, self.blocks[b].thickness)
            if self.was_block and self.update_block:
                self.last_block = b
                self.update_block = False

        self.now_blocks = False
        # platform collision check
        process_rect(self.platform.x - self.platform.length / 2, self.platform.y - self.platform.thickness / 2,
                     self.platform.length, self.platform.thickness)

        # boundaries check
        process_rect(0, 0, self.width, self.height)

        dist = ((self.saved_x - self.ball.x) ** 2 + (self.saved_y - self.ball.y) ** 2)

        if dist < self.ball.v ** 2:
            if self.saved_y > self.height - 1:
                if self.on_floor_hit():
                    return
            if self.segment_x2 - self.segment_x1 != 0:
                self.ball.dy *= -1
            else:
                self.ball.dx *= -1
            if self.was_block:
                self.on_block_hit(self.last_block)

        if self.ball.x > self.width or self.ball.x < 0 or self.ball.y > self.height or self.ball.y < 0:
            self.need_load_level = self.current_level
            self.start_new_game()

        self.ball.move()

        # print(self.ball.x, self.ball.y, self.ball.dx, self.ball.dy)

        # (self.canvas.create_line(self.ball.x, self.ball.y, self.ball.x + self.ball.dx, self.ball.y + self.ball.dy, fill="#fff000"))

        self.after_id.append(self.root.after(32, self.gamecycle))

    def hide_score (self):
        self.canvas.itemconfig(self.score_element, fill=self.background_color)

    def show_score (self):
        self.canvas.itemconfig(self.score_element, fill=self.score_color, text="Score: " + str(self.current_score))
    
    def update_lifes(self):
        self.canvas.itemconfig(self.lifes_element, fill=self.lifes_color, text="Lives: " + str(self.current_lifes))

    def hide_lifes(self):
        self.canvas.itemconfig(self.lifes_element, fill=self.background_color)

    def show_game_over(self):
        self.canvas.itemconfig(self.gameover_element, fill="white")

    def hide_game_over(self):
        self.canvas.itemconfig(self.gameover_element, fill="black")

    def show_congrats(self):
                self.canvas.itemconfig(self.congrats_element, fill="white")

    def hide_congrats(self):
        self.canvas.itemconfig(self.congrats_element, fill="black")

    def on_game_over(self):
        self.show_game_over()
        time.sleep(2)
        self.hide_game_over()
        self.need_load_level = 1
        self.start_new_game()
        self.current_level = 1
        self.current_lifes = self.max_lifes
        self.high_score = self.current_score
        self.current_score = 0

    def on_floor_hit (self):
        self.current_lifes -= 1
        if self.current_lifes >= 0:
            self.update_lifes()
        else:
            self.on_game_over()

    def on_block_hit (self, block):
        if self.blocks[block].life_points > -1:
            self.current_score += 1
            if self.blocks[block].hit():
                del self.blocks[block]
        self.show_score()

        live_blocks = 0
        for i in self.blocks:
            live_blocks += i.life_points
        if live_blocks <= 0:
            self.show_congrats()
            time.sleep(1)
            self.hide_congrats()
            self.need_load_level = self.current_level + 2
            self.start_new_game()
            self.current_level = self.current_level + 1


    # we need to define level reference system
    def start_new_game (self):
        for job in self.after_id:
            self.root.after_cancel(job)
        self.current_lifes = self.max_lifes
        # print(self.platform)
        if self.platform:
# it doesn't work at all. check arkanoid_platform for more information
#            print("was call start new _game")
#            del self.platform
#           print("was del call")
            self.platform.destroy()
        self.platform = Platform(self.canvas, self.width, self.height)
        
        if (len(self.blocks)):
            for b in self.blocks:
                del b
        self.blocks = load_level(self.canvas, self.width, self.height, self.need_load_level)
        
        if self.ball:
            del self.ball
        self.ball = Ball(self.canvas, self.platform.x, self.platform.y - 20, 5, 10)

        self.root.bind('<Key>', self.platform.move_platform)
        self.show_score()
        self.update_lifes()
        self.gamecycle()


def main():
    game = Game(tk, 800, 600)


if __name__ == '__main__':
    main()
