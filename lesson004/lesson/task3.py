# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
#  1) с помощью математических формул нахождения корней квадратного уравнения
#  2) с помощью дополнительных библиотек Python (scipy)

# line = input('Введите А B C >').split(' ')

# def convert(in_array: list):
#     out_array = []
#     for i in in_array:
#         out_array.append(int(i))
#     return


from sympy.solvers import solve
from sympy import Symbol


def fun(a, b, c):
    x = Symbol('x')
    return solve(f'{a}*x**2+{b}*x+{c}', x)


print('Корни уравнения:', *fun(1, -16, 28))



