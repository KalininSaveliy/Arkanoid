"""Модуль отвечает за создание уровней"""

from arkanoid_block import *


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
    blocks = []
    for i in range(25):
        for j in range(10):
            life = j % 4
            if life == 0:
                life = 1
            if j == 0:
                life = -1
            blocks.append(Block(canvas, 25 + i * 30, 50 + j * 11, life))
    return blocks 
  elif id == 2:
    """Проверяет изменение жизней
        Поменяй переменную life, чтобы проверить разные случаи"""
    blocks = []
    for i in range(25):
        life = 2
        blocks.append(Block(canvas, 25 + i * 30, 200, life))
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
