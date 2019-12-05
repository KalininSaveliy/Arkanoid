"""Модуль, отвечающий за движение и соударение шарика"""
from random import randint, choice 
v = 10
colors = ['red','orange','yellow','green','blue']

class Ball:
    
    def __init__(self, canvas, x, y, r, window_width, window_height):
        self.width = window_width
        self.height = window_height

        self.c = canvas

        self.r = r
        self.x = x
        self.y = y

        self.dx    = randint(-10,10)
        self.dy    = (v**2-self.dx**2)**0.5

        self.ball  = canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        self.color = choice(colors)
        canv.itemconfig(self.ball, fill=self.color)
        #canv.addtag_withtag("ball", self.ball) # не шарю

    # change color func

    "Функция, отвечающая за движение шарика"

    def check_collision_x(self, obj):
        return obj.x - self.r <= self.x + self.dx and self.x + self.dx <= obj.x + obj.w + self.r

    def check_collision_y(self, obj):
        return obj.y - self.r <= self.y + self.dy and self.y + self.dy <= obj.y + obj.h + self.r

    def move(self, blocks, platform):

        def lengthhh(x, y):
            return (x**2 + y**2) ** 0.5

        def dot(x1, y1, x2, y2):
            return x1 * y1 + x2 * y2

        def cross(x1, y1, x2, y2):
            return x1 * y2 - x2 * y1

        def check_collide(bx, by, x0, y0, x1, y1, x2, y2):
            #check area
            area = cross(x0 - bx, y0 - by, x2 - bx, y2 - by)
            # dist from bx,by to segment x0,y0 - x2,y2
            dist = area / lengthhh(x2-x0, y2-x0)

            if dist > lengthhh(x1-bx, y1-by):
                return False

            return cross(x0-bx, y0-by, x1-bx, y1-by) * cross(x1-bx, y1-by, x2-bx, y2-by) > 0



        # global v
        # length = d

        # # шаг вектор
        # step_dx = self.dx / v
        # step_dy = self.dy / v

        # # сохранение изменённой координаты вектора
        # nx = self.x
        # ny = self.y

        # # while length >= 1:
        #   for b in blocks:
        #     if check_collide(nx, ny, b.x, b.y, step_dx, step_dy, b.x, b.y + b.height):

        

        for b in blocks:
            if check_collide(self.x, self.y, b.x + b.width, b.y, self.dx, self.dy, b.x, b.y):
                self.dy = -self.dy
            elif check_collide(self.x, self.y, b.x, b.y + b.height, self.dx, self.dy, b.x, b.y):
                self.dx = -self.dx
            elif check_collide(self.x, self.y, b.x + b.width, b.y + b.height, self.dx, self.dy, b.x, b.y + b.height):
                self.dy = -self.dy
            elif check_collide(self.x, self.y, b.x, b.y + b.height, self.dx, self.dy, b.x + b.width, b.y):
                self.dx = -self.dx

        if check_collide(self.x, self.y, 0, 0, self.dx, self.dy, self.width, 0):
            self.dy = -self.dy
        
        elif check_collide(self.x, self.y, 0, 0, self.dy, self.dy, 0, self.height):
            self.dx = -self.dx

        elif check_collide(self.x, self.y, self.width, 0, self.dx, self.dy, self.width, self.height):
            self.dx = -self.dx

        elif check_collide(self.x, self.y, 0, self.height, self.dx, self.dy, self.width, self.height):
            self.dy = -self.dy
    
        self.x += self.dx
        self.y += self.dy
        print(self.x, self.y)
        self.canv.move(self.ball, self.dx, self.dy)
    
    "Функция, отвечающая за соударение шарика"
    
    def check_boundaries(self):
        if  self.y <= self.r or self.y >= self.height - self.r:
            self.dy= -self.dy
        if  self.x <= r or x >= window_width - r:
            dx=-dx
        if self.x < h_wall.x + h_wall.width and self.x + self.r > h_wall.x and self.y < h_wall.y + h_wall.height and self.y + self.r > h_wall.y:
            # нужно увеличивать счётчик очков
            # нужно прописать отскок в этом случае (есть отскок сверху снизу и слева справа)
            pass
