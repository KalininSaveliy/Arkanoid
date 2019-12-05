"""Модуль, отвечающий за движение и соударение шарика"""
from random import randint, choice 
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



    "Проверка столкновения с каким-либо объектом. У объекта должны быть поля x, y, w, h"

    def check_collision_x(self, obj):
        return obj.x - self.r <= self.x + self.dx and self.x + self.dx <= obj.x + obj.w + self.r

    def check_collision_y(self, obj):
        return obj.y - self.r <= self.y + self.dy and self.y + self.dy <= obj.y + obj.h + self.r

    "Проверка столкновения с границой экрана"
    
    def check_boundaries_x(self, width):
        return self.r >= self.x + self.dx or self.x + self.dx >= width - self.r

    def check_boundaries_y(self, height):
        return self.r >= self.y + self.dy or self.y + self.dy >= height - self.r

    "Перемещение на dx,dy"

    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.canvas.move(self.ball, self.dx, self.dy)