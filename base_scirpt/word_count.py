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
    
print("****************method 3 recommend and take the top 10****************")
def makekey(line:str, chars=set("""!'"#./\()[]- \r\n""")):

    start = 0
    
    for i,c in enumerate(line):
        if c in chars:
            if start == i:
                start += 1
                continue
            yield line[start:i]
            start = i+1
    else:
        if start < len(line):
            yield line[start:]

def wordcount(filename,encoding='utf8',ignore=set()):
    d = {}
    
    with open(filename,encoding=encoding) as f:
        for line in f:
            for word in map(str.lower,makekey(line)):
                if word not in ignore:
                    d[word] = d.get(word,0) + 1
    return d

def top(d:dict,n=10):
    for i,(k,v) in enumerate(sorted(d.items(),key=lambda item:item[1],reverse=True)):
        if i>n:
            break
        print(k,v)

top(wordcount('/tmp/sample.txt',ignore={'the','a'}))

print("****************method 4 make key with re and take the top 10****************")
from collections import defaultdict
import re

regex = re.compile('[^\w-]+')
def makekey3(line:str):
    for word in regex.split(line):
        if len(word):
            yield word

def wordcount(filename,encoding='utf8',ignore=set()):
    d = defaultdict(lambda:0)
    with open(filename,encoding=encoding) as f:
        for line in f:
            for word in map(str.lower,makekey3(line)):
                if word not in ignore:
                    d[word] += 1
    return d

def top(d:dict,n=10):
    for i,(k,v) in enumerate(sorted(d.items(),key=lambda item:item[1],reverse=True)):
        if i>n:
            break
        print(k,v)

top(wordcount('/tmp/sample.txt',ignore={'the','a'})) 
