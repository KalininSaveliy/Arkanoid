"""Модуль, отвечающий за класс кирпичей (блоков)

    Получает на вход: полотно для рисования,
                      координаты,
                      количество жизней

    Модуль может: выводить координаты блока,
                  менять цвет взависимости от жизней"""


class Block:

    def __init__(self, canvas, x, y, life_points):
        self.canvas = canvas
        self.length = 30  # длина блока
        self.thickness = 10  # толщина блока
        self.x = x  # координата верхнего левого угла по оси х
        self.y = y  # координата верхнего левого угла по оси у

        # количество жизней блока - число попаданий, необходимых для уничтожения блока
        # -1 означает, что блок нельзя сломать
        self.life_points = life_points
        self.dict = {-1: 'grey', 1: 'green', 2: 'yellow', 3: 'red'}  # зависимость между цветом и колличеством жизней
        color = self.dict[self.life_points]

        # создание блока
        self.block = self.canvas.create_rectangle(self.x, self.y, self.x + self.length,
                                                  self.y + self.thickness, fill=color)

    def hit(self):
        """Уменьшает количество жизней и меняет цвет блока"""
        # возвращает boolean -  нужно ли блок удалить с уровня
        self.life_points -= 1
        if self.life_points == 0:
            self.canvas.delete(self.block)
            return True
        # возвращает boolean -  нужно ли блок удалить с уровня
        # FIXME: не работает
        #else:
        #    self.canvas.coords(self.block, fill=self.dict[self.life_points])
        #    return False

    def his_place(self):
        """Выводит координаты блока в формате х, у верхнего левого угла, х, у нижнего правого угла"""
        return self.x, self.y, self.x + self.length, self.y + self.thickness


if __name__ == '__main__':
    print('This module is not for direct call')
