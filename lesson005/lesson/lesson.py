# Luckily, Python has this built-in :)
#
# import re
# re.split('; |, ', string_to_split)
# Update:
# Following your comment:
#
# >>> a='Beautiful, is; better*than\nugly'
# >>> import re
# >>> re.split('; |, |\*|\n',a)
# ['Beautiful', 'is', 'better', 'than', 'ugly']

# включения фильтры и map


# # что сделать с чем *при каком условии\
# numbers = [20, 50, 100]
# res = [item for item in numbers if item > 30]
# print(res)

# map создаёт коллекцию - генерирует
numbers = ['20', '50', '100']
res = tuple()

def f(a, b, c, d, e):
    return a + b + c + d + e


print(f(*[1, 2, 3, 4, 5]))


def func(a_1, a_2, a_3):
    return a_1, a_2, a_3


args = {
    'a_1': 1,
    'a_3': 3,
    'a_2': 2
}
print(func(a_1=1, a_2=2, a_3=3))
print(func(**args))



li = [-1, 0, 8, 5, 4, 8, 0, 12]
my_li = [li[0]]

for i in range(1, len(li)):
    if my_li[-1] < li[i]:
        my_li.append(li[i])
print(my_li)

[my_li.append(li[i]) for i in range(1, len(li)) if my_li[-1] < li[i]]
print(my_li)
