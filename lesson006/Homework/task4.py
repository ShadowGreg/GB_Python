# 2. Для натурального n создать последовательности 3n + 1.

in_num = int(input('введите число '))

nums = [n for n in range(1, in_num + 1)]
out_array = list(map(lambda x: 3 * x + 1, nums))
print(out_array)
