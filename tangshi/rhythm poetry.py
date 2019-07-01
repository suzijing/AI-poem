import random
import pinyin

noun = open('freqword_n.txt', encoding='utf-8').read().split()
verb = open('freqword_v.txt', encoding='utf-8').read().split()
lian = open('freqword_lian.txt', encoding='utf-8').read().split()
def writeLine1():
    global nounlist
    global verblist
rhythmlist=[]
poem=[]
while len(poem)<4:
        i = random.randint(0, len(noun) - 1)
        j = random.randint(0, len(lian) - 1)
        k = random.randint(0, len(noun) - 1)
        nounlist = noun[k][1]
        rhythmList = ["a", "e", "i", "o", "u", "v"]
        verse = pinyin.get(nounlist, format="strip")
        rhythm=''
        Ind = 0
        for p in range(len(verse)-1, -1, -1):
            if verse[p] in rhythmList:
                ind = p
                rhythm =verse[ind:]
        rhythmlist.append(rhythm)
        if len(poem)<3:
            poem.append(noun[i] + lian[j][1] + noun[k])
        elif len(poem)==3:
            if rhythmlist[1] == rhythmlist[-1]:
                poem.append(noun[i] + lian[j][1] + noun[k])
print(poem[0],end='，')
print(poem[1]+'。')
print(poem[2],end='，')
print(poem[3],end='。')



writeLine1()
