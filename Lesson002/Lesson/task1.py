# # 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность
# из N членов.

# #     *Пример:*
# #     - Для N = 5: 1, -3, 9, -27, 81
# #     1 -3 9 -27 81
# #     (-3)**0 (-3)**1 (-3)**2 (-3)**3 (-3)**4

# # умножение выполняется быстрей

# # lst = []
# # n = int(input("Write count: "))
# # for i in range(0,n+1):
# #     lst.append((-3)**i ) # последовательность операций () * / потом - и +
    
# # print(lst)


# # i = int(input('Введите число N: '))
# # y = 1
# # while i >= 1:
# #     print(int(y))
# #     y = y * (-3)
# #     i = i - 1


# # i = int(input('Введите число N: '))
# # y = 1
# # while i >= 1:
# #     print(y)
# #     y *= -3
# #     i -= 1


# # i = int(input('Введите число N: '))
# # y = 1
# # while i:
# #     print(y)
# #     y *= -3
# #     i -= 1


# i = int(input('Введите число N: '))
# y = 1
# while i:
#     print(y)
#     y *= -3
#     i -= 1
# else:
#     print('срабатывает когда шататно завершился цикл, если внутри цикла + breke - но не выполнится continue - переходит снова на проверку условия цикла')

# маржовый оператор :=  pass пустой оператор

while k:=int(input('--> ')) <= 0:
    pass



