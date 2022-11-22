# Напишите программу, которая по заданному номеру четверти, показывает диапазон
# возможных координат точек в этой четверти (x и y).
# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3


def what_quarter(inX, inY):
    if inX > 0 and inY > 0:
        print("Точка в I четверти")
    elif inX < 0 and inY > 0:
        print("Точка во II четверти")
    elif inX < 0 and inY < 0:
        print("Точка в III четверти")
    elif inX > 0 and inY < 0:
        print("Точка в IV четверти")
    elif inX == 0 and inY == 0:
        print("Точка в центре координат")
    elif inX == 0:
        print("Точка на оси X")
    elif inY == 0:
        print("Точка на оси Y")

print("Координаты точки:")
x = float(input("x = "))
y = float(input("y = "))


what_quarter(x, y)
