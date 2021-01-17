# # 读取任务名称
# f = open('word.txt', encoding='UTF-8')
# data = f.read()
# print(data.split("|"))
#
# # 读取书txt的内容
# f2 = open('book.txt', encoding='UTF-8')
# # data2 = f2.read()
# # i = 1
# # for line in f2.readlines():
# #     # print(line)
# #     if i % 2 == 1:
# #         line2 = line.strip('\n')
# #     i += 1
#
# print(f2.read().replace('\n', ''))

# i = 1
# for line in f2.readlines():
#     if i >0:
#         line2 = line.replace('\n', '')
#         len(line2) == i
#         print(line2)


        # print('halfalfajlafajl')
        # print(line)
        # newLine = line.replace(' ', '')
        # line1 = newLine.replace('\n', '')
        #
        # print(line1)
        # if len(line1) != 0:
        #     print(line1)
    #    #  print(line.strip('\n'))
    #    # print(line.replace(' ', ''))
    # i += 1


def func(filename):
    print(open(filename, encoding='UTF-8').read())
    print('test func')


func('book.txt')


