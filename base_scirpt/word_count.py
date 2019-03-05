def makekey1(s:str):
    chars = set(r"""!`"#./\()[],*-""")
    key = s.lower()
    ret = []
    for i,c in enumerate(key):
        if c in chars:
            ret.append(' ')
        else:
            ret.append(c)
    return ''.join(ret).split()

d = {}
with open('/tmp/sample.txt',encoding = 'utf8') as f:
    for line in f:
        words = line.split()
        for wordlist in map(makekey1,words):
            for word in wordlist:
                d[word] = d.get(word,0) + 1
for k,v in sorted(d.items(),key= lambda item:item[1],reverse=True):
    print(k,v)
    
print("************method  2**************")
def makekey2(s:str):
    chars = set(r"""!`"#./\()[],*-""")
    key = s.lower()
    ret = []
    start = 0
    length = len(key)
    
    for i,c in enumerate(key):
        if c in chars:
            if start == i:
                start += 1
                continue
            ret.append(key[start:i])
            start = i + 1
    else:
        if start < len(key):
            ret.append(key[start:])
    return ret
d = {}
with open('/tmp/sample.txt',encoding='utf-8') as f:
    for line in f:
        words = line.split()
        for wordlist in map(makekey2,words):
            for word in wordlist:
                d[word] = d.get(word,0) + 1

#print(sorted(d.items(),key=lambda item:item[1],reverse=True))
for k,v in sorted(d.items(),key= lambda item:item[1],reverse=True):
    print(k,v)
    
