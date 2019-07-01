import os, codecs
import jieba
from collections import Counter
import csv
import xlwt

file = open('analysis.csv','w',encoding='utf-8',newline='')
writer=csv.writer(file)
print('请输入想要统计的词频数量：')
aa=int(input())
def get_words(txt):
    seg_list = jieba.cut(txt)
    c = Counter()
    for x in seg_list:
        if len(x) > 1 and x != '\r\n':
            c[x] += 1
    file.write('常用词频度统计结果:')
    for (k, v) in c.most_common(aa):
        writer.writerow([k,v])
if __name__ == '__main__':
    with codecs.open('cut.txt', 'r', encoding='utf-8') as f:
        txt = f.read()
    get_words(txt)
file.close()


def csv_to_xlsx():
    with open('analysis.csv', 'r', encoding='utf-8') as f:
        read = csv.reader(f)
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet('data')  # 创建一个sheet表格
        l = 0
        for line in read:
            print(line)
            r = 0
            for i in line:
                print(i)
                sheet.write(l, r, i)  # 一个一个将单元格数据写入
                r = r + 1
            l = l + 1

        workbook.save('analysis.xlsx')  # 保存Excel



if __name__ == '__main__':
    csv_to_xlsx()
