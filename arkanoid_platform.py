"""Модуль, отвечающий за движение платформы"""


class Platform:

    def __init__(self, canvas, window_width, window_height):
        self.length = 70  # длина платформы
        self.thickness = 7  # толщина платформы
        self.color = 'blue'
        self.x = window_width / 2
        self.y = window_height * 7 / 8
        self.canvas = canvas

        # создаем платформу
        self.platform = [canvas.create_oval(self.x - (self.length - self.thickness) / 2, self.y - self.thickness / 2,
                                            self.x - (self.length + self.thickness) / 2, self.y + self.thickness / 2,
                                            fill=self.color),

                         canvas.create_oval(self.x - (- self.length - self.thickness) / 2, self.y - self.thickness / 2,
                                            self.x - (- self.length + self.thickness) / 2, self.y + self.thickness / 2,
                                            fill=self.color),

                         canvas.create_rectangle(self.x - self.length / 2, self.y - self.thickness / 2,
                                                 self.x + self.length / 2, self.y + self.thickness / 2,
                                                 fill=self.color)]
        #            canvas.create_rectangle(canvas.create_oval(x - (length - d) / 2, y - d / 2,
        #                                                       x - (length + d) / 2, y + d / 2,
        #                                                       fill=color))
        # фича: рисует красиво, но выдает ошибку

    def platform_centre(self):
        return self.x, self.y - self.thickness, self.l

    def move_platform(self, shift):
        for part in self.platform:
            self.canvas.move(part, shift, 0)

    def shift_platform(self, event):
        shift = 20
        if event.keysym == 'a' or 'Left':
            shift = - shift
        if event.kesym == 'd' or 'Right':
            pass
            S


if __name__ == "__main__":
    print('This module is not for direct call')
