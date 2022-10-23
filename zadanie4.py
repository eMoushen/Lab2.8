#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_input():
    ls = input("Введите строку: ")
    return ls


def test_input(ls):
    # Возможно ли переданное значение преобразовать к числу
    if type(ls) == int:
        return True
    elif ls.isnumeric():
        return True
    else:
        return False


def str_to_int(ls):
    a = int(ls)
    return a


def print_int(ls):
    print(ls)


if __name__ == '__main__':
    ls = get_input()
    exam = test_input(ls)
    if exam is True:
        print_int(str_to_int(ls))
    else:
        print("Нельзя преобразовать в число")