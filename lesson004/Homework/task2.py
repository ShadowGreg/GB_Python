# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
from sympy import primefactors
from itertools import groupby


def prim_func(in_num):
    i = 2
    prim = []
    while i * i <= in_num:
        while in_num % i == 0:
            prim.append(i)
            in_num = in_num / i
        i = i + 1
    if in_num > 1:
        prim.append(int(in_num))
    out = [el for el, _ in groupby(prim)]
    return out


n = 3 * 7 * 11 * 21 * 23 * 13 * 24 * 165

print("The prime factors from library of num {} \t: {}".format(n, primefactors(n)))
print("The prime factors fom function of num {} \t: {}".format(n, prim_func(n)))
