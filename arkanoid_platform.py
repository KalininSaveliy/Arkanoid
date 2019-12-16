"""Модуль, отвечающий за класс платформы

    Получает на вход: полотно для рисования,
                      размеры полотна

    Модуль может: передвигать платформу по нажатию клавиш A и D (Left и Right)
                  выводить координаты платформы"""


class Platform:

    def __init__(self, canvas, window_width, window_height):
        self.length = 70  # длина платформы
        self.thickness = 7  # толщина платформы
        self.color = 'blue'

        # координаты ценрта платформы
        self.x = window_width / 2
        self.y = window_height * 7 / 8

        # диапазон движения центра платформы
        self.x_max = window_width - self.length / 2
        self.x_min = self.length / 2
        self.canvas = canvas

        # создаем платформу, в этом разделе задается ее форма
        self.platform = [canvas.create_oval(self.x - (self.length - self.thickness) / 2, self.y - self.thickness / 2,
                                            self.x - (self.length + self.thickness) / 2, self.y + self.thickness / 2,
                                            fill=self.color),

                         canvas.create_oval(self.x - (- self.length - self.thickness) / 2, self.y - self.thickness / 2,
                                            self.x - (- self.length + self.thickness) / 2, self.y + self.thickness / 2,
                                            fill=self.color),

                         canvas.create_oval(self.x - self.length / 2, self.y - self.thickness / 2,
                                            self.x + self.length / 2, self.y + self.thickness / 2,
                                            fill=self.color)]

    # WTF IDK WHY IT'S NOT WORKING? I mean that in block and ball all stuff work pretty nice but when i call that nothing is happen
    # print before and after work but inside not
    # check arkanoid_main start_new_game func
    # def __del__(self):
    #     print("was executed")
    #    self.canvas.delete(self.platform[0])
    #    self.canvas.delete(self.platform[1])
    #    self.canvas.delete(self.platform[2])

    def destroy(self):
        self.canvas.delete(self.platform[0])
        self.canvas.delete(self.platform[1])
        self.canvas.delete(self.platform[2])


    def centre(self):
        """Выводит координаты в формате: х центра платформы и у его верхней грани"""
        return self.x, self.y - self.thickness, self.length + self.thickness

    def move_platform(self, event):
        """Передвижение платформы при нажатии клавиш"""
        shift = 30  # модуль сдвига платформы за одно нажатие клавишы

        # перемещение вправо
        if event.keysym == 'd' or event.keysym == 'Right':
            if self.x <= self.x_max - shift:
                self.x += shift
                for part in self.platform:
                    self.canvas.move(part, shift, 0)
            elif self.x <= self.x_max:
                self.x = self.x_max
                for part in self.platform:
                    self.canvas.move(part, self.x_max - self.x, 0)

        # перемещение влево
        if event.keysym == 'a' or event.keysym == 'Left':
            if self.x >= self.x_min + shift:
                self.x -= shift
                for part in self.platform:
                    self.canvas.move(part, -shift, 0)
            elif self.x >= self.x_min:
                self.x = self.x_min
                for part in self.platform:
                    self.canvas.move(part, self.x_min - self.x, 0)


if __name__ == "__main__":
    print('This module is not for direct call')
