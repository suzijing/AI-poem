import pinyin
rhythm = ""
nounlist=input()
rhythmList = ["a", "e", "i", "o", "u", "v"]
verse = pinyin.get(nounlist, format="strip")
Ind=0
for p in range(len(verse)-1):
    if verse[p] in rhythmList:
        ind = p
        rhythm = verse[ind:]

print(rhythm)
