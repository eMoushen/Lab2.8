#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def test():
    number = 1
    while True:
        a = int(input("Введите число: "))
        number *= a
        if number == 0:
            print("Произведение равно 0")
            break
        else:
            print(f"Полученное произведение:  {number}")


if __name__ == '__main__':
    test()