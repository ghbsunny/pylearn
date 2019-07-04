# -*- coding: UTF-8 -*-
print("------------method 1-------------")
#用匹配特殊字符的方式取出一段nginx日志里的字段


import datetime
line = '''123.125.71.36 - - [06/Apr/2017:18:09:25 +0800] \
"GET / HTTP/1.1" 200 8642 "-" \
"Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"
'''
names = ('remote','','','datetime','request','status','length','','useragent')
ops = (None,None,None,lambda timestr:datetime.datetime.strptime(timestr,'%d/%b/%Y:%H:%M:%S %z'),lambda request:dict(zip(['method','url','protocol'],request.split())),int,int,None,None)

chars = set(" \t")
def makekey(line):
    start = 0
    skip = False
    for i,c in enumerate(line):
      #  print(i,c)
        if not skip and c in '"[':
            start = i+1
            skip = True
        elif skip and c in '"]':
            skip = False
            yield line[start:i]
            start = i+1
            continue
        if skip:
            continue
        if c in chars:
            if start == i:
                start = i+1
                continue
            yield line[start:i]
            start = i+1
    else:
        if start < len(line):
            yield line[start:]

def convert_time(timestr):
    return datetime.datetime.strptime(timestr,'%d/%b/%Y:%H:%M%S %z')

def get_request(request):
    return dict(zip(['method','url','protocol'],request.split()))

def extract(line):
    return dict(map(lambda item:(item[0],item[2](item[1]) if item[2] is not None else item[1]),zip(names,makekey(line),ops)))
            
print(list(makekey(line)))

print(extract(line))


print("~~~~~~~~~~~~~~~~~~method 2~~~~~~~~~~~~~~~~~~~~~~")
#用正则表达式取出一段nginx日志里的字段
import datetime
import re

line = '''123.125.71.36 - - [06/Apr/2017:18:09:25 +0800] \
"GET / HTTP/1.1" 200 8642 "-" \
"Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"
'''
ops = {'datetime':lambda timestr:datetime.datetime.strptime(timestr,'%d/%b/%Y:%H:%M:%S %z'),'status':int,'length':int}

#注意，以下如果多一个空格，导致模式没有匹配到，就会报错'NoneType' object has no attribute 'groupdict'
#所以，以下的代码必须根据实际的格式进行调整
pattern = '''(?P<remote>[\d.]{7,} - - \[(?P<datetime>[/\w +:]+)\]) \
"(?P<method>\w+) (?P<url>\S+) (?P<protocol>[\w/\d.]+)" (?P<status>\d+) (?P<length>\d+) .+ "(?P<useragent>.+)"
'''

regex = re.compile(pattern)

def extract(line:str) -> dict:
    matcher = regex.match(line)
    if matcher:
        return {k:ops.get(k,lambda x:x)(v) for k,v in matcher.groupdict().items()}
    else:
        return None  #没有匹配到，则返回None 
        #raise Exception('No match')  #没有匹配到，则返回No match

print(extract(line))

