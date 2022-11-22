# Напишите программу, которая принимает на вход координаты двух точек и находит
#  расстояние между ними в 2D пространстве.

# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

from math import sqrt


def in_coords():
    temp_list = []
    List = ['A', 'B']
    for i in List:
        temp_list.append(float(input(f'Введите X точки {i} > ')))
        temp_list.append(float(input(f'Введите Y точки {i} > ')))
    return temp_list


list = in_coords()


def get_distance(inList):
    return sqrt((inList[2] - inList[0]) ** 2 + (inList[3] - inList[1]) ** 2)


print(
    f'Расстояние между точками A ({list[0]},{list[1]}); B ({list[2]},{list[3]}) -> {round(get_distance(list),2)}')
