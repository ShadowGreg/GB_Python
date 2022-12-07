# 2. Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#
# a) Добавьте игру против бота
#
# b) Подумайте как наделить бота ""интеллектом""

# вариант человек против человека:
from entities.RegularExpressions import *

player2 = input("Введите имя второго игрока: ")

priority = randint(0, 2)
if priority:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0
counter2 = 0

while amount > 28:
    if priority:
        k = input_dat(player1)
        counter1 += k
        amount -= k
        priority = False
        p_print(player1, k, counter1, amount)
    else:
        k = input_dat(player2)
        counter2 += k
        amount -= k
        priority = True
        p_print(player2, k, counter2, amount)

if priority:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")
