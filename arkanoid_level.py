"""Модуль отвечает за создание уровней"""

from arkanoid_block import *


def create_check_level(canvas, window_width, window_height):
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


if __name__ == '__main__':
    print('This module not for direct call')