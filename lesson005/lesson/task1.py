# # # 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# # # --> 'Я люблю абвЖвау иабв Питон'
# # # --> 'Я люблю Питон'
# # # # включений, filter, map
# #
# # s = 'Я люблю абвДжаву иабв Питон'
# #
# # res = [i for i in s.split() if 'абв' not in i]
# # print(s)
# # print(" ".join(res))
#
#
# # res_filt = filter(lambda item: 'абв' not in item, [i for i in s.split()])
#
#
# my_string = 'Я люблю абвЖвау иабв Питон'
#
# my_li = my_string.split()
# print(my_li)
#
# my_li = list(filter(lambda el: not "абв" in el, my_li))
# print(my_li)
#
# my_string = ' '.join(my_li)
# print(my_string)
