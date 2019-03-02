#这个解码程序仅能解码4位数，否则会报错
from collections import OrderedDict

base_tbl = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
alphabet = OrderedDict(zip(base_tbl,range(64)))
def base64decode(src:bytes):
    ret = bytearray()
    length = len(src)
    step = 4
    for offset in range(0,length,step):
        tmp = 0x00
        block = src[offset:offset + step]
        
        #开始移位计算
        for i in range(4):
            index = alphabet.get(block[-i-1])
            if index is not None: #如果是none，即找不到值，就不用移位
                tmp += index << i*6
        ret.extend(tmp.to_bytes(3,'big'))
    return bytes(ret.rstrip(b'\x00'))
#base64的decode
txt = "TWFu"
txt = txt.encode()
print("解码")
print(base64decode(txt).decode())
print('和自带的函数base64对比')
import base64
print(base64.b64decode(txt).decode())
