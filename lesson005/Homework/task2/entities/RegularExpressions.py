from random import randint


def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, input_amount):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {input_amount} конфет.")


amount = 2021

player1 = input("Введите имя первого игрока: ")
