# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример:

# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06

def calculation_formula(in_num: int):
    return (1 + 1 / in_num) ** in_num


def calculation(in_num: int):
    output_str = ''
    count = 0
    for i in range(1, in_num + 1):
        if i == in_num:
            sign = ''
        else:
            sign = ', '
        count = count + calculation_formula(i)
        output_str = output_str + str(i) + ':' + ' ' + str(round(calculation_formula(i), 2)) + sign
    return output_str, count


n = int(input('введите n > '))
print(f'Для n={n}, тогда [{calculation(n)[0]}] Сумам {calculation(n)[1]:.2f}')
