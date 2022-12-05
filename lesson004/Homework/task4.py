# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
#
# Пример:
#
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# - k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.
import random
from pathlib import Path


def coefficient_generator():
    return str(random.randrange(0, 100))


def create_equation(in_num: int):
    equation = ''
    for i in range(in_num + 1):
        coeff = coefficient_generator()
        if i == 0 and coeff != '0':
            equation = coeff + ' = 0'
        if i > 1 and coeff != '0':
            equation = coeff + f'*(x**{i}) + ' + equation
        if i == 1 and coeff != 0:
            equation = coeff + '*x + ' + equation
    return equation


def write_file(file_name):
    folder = 'task'
    path = Path(folder)
    filepath = path / file_name
    with filepath.open("w", encoding="utf-8") as f:
        f.write(line)
    return filepath


k = int(input('Введите k  > '))
line = create_equation(k)
print(f'k={k} => {line}')
print(f'Файл сформирован по пути > {write_file("polynomial02.txt")}')
