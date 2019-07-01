import jieba
import jieba.analyse

poetry_file ='zzcf.txt'
n_file = 'freqword_n.txt'
content = open(poetry_file, encoding='utf-8').read()
result_n = open(n_file,'w',encoding='utf-8')

for x in jieba.analyse.textrank(content, topK=600, allowPOS=('n', 'nr', 'ns', 'nt', 'nz', 'm')):
    result_n.writelines(x+" ")
result_n.close()
