"""Модуль, отвечающий за движение и соударение шарика"""

v = 11
colors = ['red','orange','yellow','green','blue']

class Ball(canv, platform):
    
    def __init__(self):
        self.r     = 5
        self.x     = platform.x
        self.y     = platform.y + self.r
        self.dx    = rnd(-10,10)
        self.dy    = (v**2-dx**2)**0.5
        self.ball  = canv.create_oval(self.x - self.r,self.y - self.r, self.x + self.r, self.y + self.r)
        self.color = choice(colors)
        #canv.itemconfig(self.ball, fill="red") # не шарю
        #canv.addtag_withtag("ball", self.ball) # не шарю

    "Функция, отвечающая за движение шарика"
    
    def move_ball(self):
    
        canv.move(ball,dx,dy)
        x+=dx
        y+=dy
        canv.move(self.ball, self.dx, self.dy)
    
    "Функция, отвечающая за соударение шарика"
    
    def rebound_ball(self):
        
        if  y <= r or y >= window_height - r:
            dy=-dy
        if  x <= r or x >= window_width - r:
            dx=-dx
        if self.x < h_wall.x + h_wall.width and self.x + self.r > h_wall.x and self.y < h_wall.y + h_wall.height and self.y + self.r > h_wall.y:
            # нужно увеличивать счётчик очков
            # нужно прописать отскок в этом случае (есть отскок сверху снизу и слева справа)
pass
