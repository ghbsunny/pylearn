import configparser
import json

src = '/tmp/test.ini'
dst = '/tmp/test.json'

cfg = configparser.ConfigParser()
cfg.read(src)

d = {}
#遇到 'dict' object is not callable的报错，执行如下代码
#del(dict)

for k,v in cfg.items():
    d[k] = dict(cfg.items(k))

with open(dst,'w') as f:
    json.dump(d,f)
