import random
import pinyin

noun = open('freqword_n.txt', encoding='utf-8').read().split()
lian = open('freqword_lian.txt',encoding='utf-8').read().split()
verb = open('freqword_v.txt', encoding='utf-8').read().split()

def writeLine1():
    global nounlist
    global verblist
    global lianlist
    i=random.randint(0,len(noun)-1)
    j=random.randint(0,len(lian)-1)
    k=random.randint(0,len(verb)-1)
    return noun[i]+lian[j][1]+verb[k]
def writeLine2():
    global nounlist
    global verblist
    i=random.randint(0,len(noun)-1)
    j=random.randint(0,len(verb)-1)
    k=random.randint(0,len(noun)-1)
    return noun[i]+verb[j]+noun[k][1]
print(writeLine1(),end='，')
print(writeLine1(),end='。')
print(writeLine1(),end='，')
print(writeLine1(),end='。')

