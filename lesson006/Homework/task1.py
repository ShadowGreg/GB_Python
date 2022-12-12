# Напишите программу, которая принимает на вход координаты двух точек и находит
#  расстояние между ними в 2D пространстве.

# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

from math import sqrt


def input_coordinates():
    temp_list = []
    # List = ['A', 'B']
    # for i in List:
    #     temp_list.append(float(input(f'Введите X точки {i} > ')))
    #     temp_list.append(float(input(f'Введите Y точки {i} > ')))
    temp_list = list(map(lambda x: int(x), input('введите координаты точек через пробел > ').split(' ')))
    return temp_list


# list = input_coordinates()


def get_distance(input_list=input_coordinates()):
    return sqrt((input_list[2] - input_list[0]) ** 2 + (input_list[3] - input_list[1]) ** 2)


print(
    f'Расстояние между точками A и B -> {round(get_distance(), 2)}')
