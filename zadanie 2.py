#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def cylinder():
    r = int(input("Введите радиус цилиндра: "))
    h = int(input("Введите высоту цилиндра: "))
    bs = 2 * math.pi * r * h

    quest = int(input("Вы хотите получить площадь боковой поверхности или полную площадь ?\n"
                      "Боковой поверхности - 1\n"
                      "Полную площадь цилиндра - 2\n"))
    if quest == 1:
        print("Площадь боковой поверхности = ", bs)

    elif quest == 2:
        print("Полная площадь цилиндра = ", bs + (circle(r) * 2))


def circle(r):
    return math.pi * r ** 2


if __name__ == '__main__':
    cylinder()