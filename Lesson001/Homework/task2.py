# Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# эта точка. ⋀ - and ⋁ - or ¬ - not

count = 1
for x in range(2):
    for y in range(2):
        for z in range(2):
            if (not (x or y or z) == (not x and not y and not z)):
                print(
                    f'Найдено решение {count} логическое выражение верно при {x}, {y}, {z}')
                count += 1
