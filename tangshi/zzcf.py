import re
poemfile=open('poem.txt',encoding='utf-8').read()
p1 = r"[\u4e00-\u9fa5]{5,7}[\u3002|\uff0c]"  
pattern1 = re.compile(p1)


result=pattern1.findall(poemfile)

f=open('zzcf.txt','w',encoding='utf-8')
for x in result:
    f.write(x)
f.close()
