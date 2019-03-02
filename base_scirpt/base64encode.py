#base64编码，每次取出3个字节，把8位字符编码成6位，6位不足一个字节，故前面补2个0，即ASCII的3个字节编程base64的4个字节，末尾不足3个字节的用0补满3个字节
#假设一个字符串最后剩下小写字节a,小写字母a,ASCII码为0x61, 110000001,从最高位开始取6位，高位补0，剩余 01 为第二个6位的高位，同时，后面4位补0，另外，第二个6位的高位2个也补0
#即 a  11000001 首先补2个0(即0x00），a 的base64 为 110000001 000000000  000000000
#把a 的最高位开始，取6位 1100000  0100000   000000  0000000
#把6位再补成8位，即a的base64为  00110000  000100000   00000000  000000000,注意这里补2个0，用等号表示，等号的字节为0x3D,
#即a最终需要有两个24 16 0x3D 0x3D ,编码表中，Y为24，Q为16 ，即a编码结果为 b'YQ=='

alphabet = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
teststr = "abddhmk"

def base64(src):
    ret = bytearray()
    length = len(src)
    #r表示最终不足3位补0的个数
    r=0
    for offset in range(0,length,3):
        if offset +3 <= length:
            triple = src[offset:offset+3]
        else:
            triple = src[offset:]
            r = 3-len(triple)
            triple = triple + '\x00'*r
        b=int.from_bytes(triple.encode(),'big')
        #print(hex(b))
        for i in range(18,-1,-6):
            if i ==18:
                index = b >> i
            else:
                index = b>>i & 0x3F
            ret.append(alphabet[index])
        for i in range(1,r+1):
            ret[-i] = 0x3D
    return ret

print(base64(teststr))

#对比base64实现
import base64
print(base64.b64encode(teststr.encode()))
