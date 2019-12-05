"""Модуль, отвечающий за движение и соударение шарика"""
from random import randint, choice
import math
colors = ['red','orange','yellow','green','blue']

class Ball:
    def __init__(self, canvas, x, y, r, max_speed):

        self.canvas = canvas

        self.x = x
        self.y = y
        self.r = r


        self.dx    = randint(-max_speed, max_speed)
        self.dy    = - (max_speed ** 2 - self.dx ** 2) ** 0.5

        # canvas drawing
        self.ball  = canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        self.color = choice(colors)
        self.canvas.itemconfig(self.ball, fill=self.color)
        #canv.addtag_withtag("ball", self.ball) # не шарю





    "Перемещение на dx,dy"

    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.canvas.move(self.ball, self.dx, self.dy)