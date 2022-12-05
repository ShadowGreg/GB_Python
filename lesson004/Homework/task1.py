# Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141
# Ввод: 0.01
# Вывод: 3.14
#  Ввод: 0.001
#  Вывод: 3.141


def self_pi():
    # Initialize denominator
    k = 1
    # Initialize sum
    s = 0
    for i in range(1000000):
        # even index elements are positive
        if i % 2 == 0:
            s += 4 / k
        else:
            # odd index elements are negative
            s -= 4 / k
        # denominator is odd
        k += 2
    return s


def count_accuracy():
    return len(input('Введите точность с которой хотите получить число pi вида 0.001 > ').split('.')[1])


def to_fixed(num_obj, digits=0):
    return f"{num_obj:.{digits}f}"


print(to_fixed(self_pi(), count_accuracy()))
