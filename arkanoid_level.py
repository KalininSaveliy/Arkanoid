"""Модуль отвечает за создание уровней"""

from arkanoid_block import *
from random import randint, choice

count = [20, 19]  # const число кубиков по горизонтали, вертикали, для которого делается уровень
k = [0.9, 0.5]  # отношение размера уровня к размерам окна (горизонталь, вертикаль)


def sizes_of_blocks(window_width, window_height):
    """Функция вычисляет размеры блоков, чтобы они помещались на данном окне
       (устойчивость к изменению размеров окна)"""

    block_length = window_width * k[0] / count[0]  # длина блока
    dl = window_width * (1 - k[0]) / 2  # отступ слева или справа

    block_thickness = window_height * k[1] / count[1]  # ширина блока
    dh = window_height / 24 + block_thickness  # отступ сверху

    return block_length, dl, block_thickness, dh


def count_of_blocks(window_width, window_height):
    """Функция вычисляет сколько блоков помещается на данном окне
       (устойчивость к изменению размеров окна)"""
    count_of_blocks_in_line = window_width // Block.length  # целое количество блоков, помещающихся в длину
    dl = window_width % Block.length  # остаток длины окна
    if dl == 0:
        count_of_blocks_in_line -= 1
        dl = Block.length

    # целое количество блоков, помещающихся в высоту, с учетом того, что играем только на верхней половине и
    # что сверху должно быть место для одного блока
    count_of_blocks_in_column = window_height // 2 // Block.thickness
    # Fixme: рассмотреть случай когда блоков по высоте мало или уровень опускается сильно ниже центра

    if count_of_blocks_in_line == 0 or count_of_blocks_in_column == 0:
        print("Ха-ха, очень смешно сделай окно побольше или блоки поменьше")
    return count_of_blocks_in_line, dl, count_of_blocks_in_column


"""Первые два тестовых уровня рассчитаны на размеры окна 800х600  !!!"""

def load_level(canvas, window_width, window_height, id):
  if id == 0:
    return [Block(canvas, 100, 100, 1)]
  if id == 1:
  #   blocks = []
  #   for i in range(25):
  #       for j in range(10):
  #           life = j % 4
  #           if life == 0:
  #               life = 1
  #           if j == 0:
  #               life = -1
  #           blocks.append(Block(canvas, 25 + i * 30, 50 + j * 11, life))
  #   return blocks
      """Два столбика и горочка"""
      blocks = []
      length, dl, thickness, dh = sizes_of_blocks(window_width, window_height)  # см подробности в самой функции

      for i in range(count[1]):
          for j in range(2):
              life = i % 2 + 1
              x = [dl + j * length, window_width - dl - (j + 1) * length]
              for _ in x:
                  blocks.append(Block(canvas, _, thickness * (i + 1) + window_height / 24, life))

      for i in range(11):
          life = i % 2 + 2
          x = [(i - 1) * length / 2 + dl, (23 - i) * length / 2 + dl]
          for _ in x:
              blocks.append(Block(canvas, _ + 4 * length, dh + (5 + i) * thickness, life))

      return blocks

  elif id == 2:
    # """Проверяет изменение жизней
    #     Поменяй переменную life, чтобы проверить разные случаи"""
    # blocks = []
    # for i in range(25):
    #     life = 2
    #     blocks.append(Block(canvas, 25 + i * 30, 200, life))
    """Создает рандомный симметричный относительно вертикали уровень
            Устойчив к изменению колличества блоков"""
    blocks = []
    length, dl, thickness, dh = sizes_of_blocks(window_width, window_height)  # см подробности в самой функции
    density = randint(1, 5)  # процент заполняемости поля (отношение False к True см. ниже)
    boolean_mas = [True] + density * [False]

    for j in range(count[1]):
        for i in range(count[0] // 2):
            if choice(boolean_mas):  # ставим ли блок в точку с координатами i, j
                life = choice([-1, 1, 1, 2, 3])
                for _ in range(2):
                    x = [i, count[0] - 1 - i]
                    blocks.append(Block(canvas, x[_] * length + dl, j * thickness + dh, life))

        if count[0] % 2 == 1 and choice(boolean_mas):
            life = choice([-1, 1, 1, 2, 3])
            blocks.append(Block(canvas, count[0] // 2 * length + dl, j * thickness + dh, life))

    return blocks

  else:
    """Пирамидка вершиной вниз"""
    blocks = []
    count_in_line, dl, count_in_column = count_of_blocks(window_width, window_height)  # см подробности в самой функции
    for i in range(count_in_column):
        le = count_in_line - i  # количество блоков в этой строчке
        for j in range(le):
            if i in (3, 7):
                life = -1
            elif le % 2 == 0:
                if j in (le // 2 - 1, le // 2):
                    life = 3
                elif j in (le // 2 - 3, le // 2 - 2, le // 2 + 1, le // 2 + 2):
                    life = 2
                else:
                    life = 1
            elif le % 2 == 1:
                if j in (le // 2 - 1, le // 2, le // 2 + 1):
                    life = 3
                elif j in (le // 2 - 3, le // 2 - 2, le // 2 + 2, le // 2 + 3):
                    life = 2
                else:
                    life = 1
            blocks.append(Block(canvas, (j + i / 2) * Block.length + dl / 2,
                                Block.thickness * (i + 1) + window_height / 24, life))
    return blocks


if __name__ == '__main__':
    print('This module is not for direct call')
