import re


def find_item(yo):
    with open('book.txt', encoding='UTF-8') as f:
        data = f.read().replace('\n', '')
        word_num = re.findall(yo, data)
 #       print('词语 %s 出现 %s 次' %(yo, len(word_num)))

    return word_num


# 读取词语的信息
word_dict = {}
with open('word.txt', encoding='UTF-8') as f:
    for line in f:
        words = line.split('|')
        for n in words:
            # print(n)
            word_num = find_item(n)
            word_dict[n] = word_num

word_sorted = sorted(word_dict.items(), key=lambda item: item(1), reverse=True)
print(word_sorted[0:10])