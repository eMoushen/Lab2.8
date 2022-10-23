#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def add(products):
    print("сколько добавить товаров?")
    kol = int(input())
    k = 0
    for m in range(kol):
        k = k + 1
        name = input("Введите название для " + "{}".format(k) + " товара:  ")
        shope = input("Введите название магазина:  ")
        price = int(input("Стоимость товара:  "))
        product = {
            'name': name,
            'price': price,
            'shope': shope,
        }
        products.append(product)
        products.sort(key=lambda item: item.get('name', ''))


def list_1(products):
    # Заголовок таблицы.
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 5,
        '-' * 20,
        '-' * 14,
        '-' * 17
    )
    print(line)
    print(
        '| {:^5} | {:^20} | {:^14} | {:^17} |'.format(
            "№",
            "Название товара",
            "Цена",
            "Название магазина"
        )
    )
    print(line)
    # Вывести данные о всех товарах.
    for idx, product in enumerate(products, 1):
        print(
            '| {:>5} | {:<20} | {:<14} | {:>17} |'.format(
                idx,
                product.get('name', ''),
                product.get('price', 0),
                product.get('shope', '')
            )
        )
    print(line)


def select(products):
    # Проверить наличие товара.
    nalich = "new balance"

    flag = False
    for product in products:
        if nalich in product['name']:
            print(f'Товар в наличии: {product["name"]}\nЦена: {product["price"]}\n')
            flag = True

    if not flag:
        print(f'\nТаких товаров нет: {nalich}')


def help_1():
    print("Список команд:\n")
    print("add - добавить товар")
    print("list - вывести список товаров")
    print("select - товары в наличии")
    print("help - отобразить справку")
    print("exit - завершить работу с программой")


def main():
    print("help - список всех команд")
    products = []

    while True:
        command = input(">>> ").lower()

        if command == "help":
            help_1()

        elif command == "add":
            add(products)

        elif command == 'list':
            list_1(products)

        elif command == 'exit':
            break

        elif command == 'select':
            select(products)

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()
