"""Модуль, отвечающий за движение и соударение шарика"""


from random import choice, randint as rnd


class Ball:
    def __init__(self, canvas, platform):
        self.canvas = canvas
        self.v = 11
        colors = ['red', 'orange', 'yellow', 'green', 'blue']
        self.r = 5
        self.x, self.y, self.platform_len = platform.centre
        self.y -= self.r
        self.dx = rnd(-10, 10)
        self.dy = - (self.v**2 - self.dx**2)**0.5
        self.color = choice(colors)
        self.ball = canvas.create_oval(self.x - self.r,self.y - self.r,
                                       self.x + self.r, self.y + self.r,
                                       fill=self.color)
        #canv.itemconfig(self.ball, fill="red")  # не шарю
        #canv.addtag_withtag("ball", self.ball)  # не шарю
    
    def move_ball(self):
        """Функция, отвечающая за движение шарика"""
        if True:  # провека условия соударения шарика с блоками или платформой
            pass
        self.x += self.dx
        self.y += self.dy
        self.canvas.move(self.ball, self.dx, self.dy)
    
    # def rebound_ball(self):
    #     """Функция, отвечающая за соударение шарика"""
    #     if  self.y <= self.r or self.y >= window_height - self.r:
    #         self.dy=-self.dy
    #     if  self.x <= self.r or self.x >= self.window_width - self.r:
    #         self.dx=-self.dx
    #     if self.x < h_wall.x + h_wall.width and self.x + self.r > h_wall.x and self.y < h_wall.y + h_wall.height and self.y + self.r > h_wall.y:
            # нужно увеличивать счётчик очков для этого есть переменная score
            # нужно прописать отскок в этом случае (есть отскок сверху снизу и слева справа)
