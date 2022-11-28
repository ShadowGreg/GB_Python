# # # # 3. Напишите программу, в которой пользователь будет задавать две строки, 
# # # # а программа - определять количество вхождений одной строки в другой.


# # # S1 = 'sdfssf sddff svvsef xbsdf sdfwwe'
# # # S2 = 'dff'
# # # Count = S1.count(S2)
# # # if Count == 0:
# # #     print('Не входит')
# # # else:
# # #     print('Входит')


# S1 = 'sdfssf sddff svvsef xbsdf sdfwwe'
# S2 = 'df'
# i = 0
# temp = 0
# while i < len(S1):
#     if S2[0] == S1[i] and S2[1] == S1[i+1]:
#         temp +=1 
#     i +=1
# print(temp)


s1 = input()
s2 = input()
print(s1.count(s2))

s1 = 'ЯлюблюлюблюлюблюPython'
s2 = 'люблю'
i = 0
cnt = 0
while i < len(s1) - 1:
    if s1[i:len(s2) + i] == s2:
        cnt += 1
    i += 1
print(cnt)

s1 = 'ЯлюблюлюблюлюблюPython'
s2 = 'лю'
cnt = 0
while s2 in s1:
    s1 = s1.replace(s2, ' ', 1)
    print(s1)
    cnt += 1
print(cnt)

s1 = 'Я люблю люблюлюблюPython'
s2 = 'лю'
res = s1.split(s2)
print(res)
print(len(res) - 1)
