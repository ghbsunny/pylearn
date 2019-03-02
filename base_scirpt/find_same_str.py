#方法一：把一个字符串中从最大的字符串开始拆分，依次和第二个字符串对比，最大没找到，长度减去1个继续找，找到同样的字符串立即返回

s1 = 'abcafedf'
s2 = 'defadaabcsdfes'
s3 = 'aaadfd123aab'
print('method 1')
def findstr(str1,str2):
    count = 0
    length = len(str1)
    
    for sublen in range(length,0,-1):
        for start in range(0,length - sublen+1):
            substr = str1[start:start + sublen]
            count += 1
            if str2.find(substr) > -1:
                print("count = {},substrlen = {},substr = {}".format(count,sublen,substr))
                return substr
print(findstr(s1,s2))
print(findstr(s1,s3))

#方法二 利用矩阵，依次把一个字符串每个字符和第二个字符串进行对比，相同，则标注1

print('method 2')
s1 = 'abcafedf'
s2 = 'defadaabcsdfes'
s3 = 'aaadfd123aab'

def findstr(str1,str2):
    matrix = []
    xmax = 0
    xindex = 0
    for i,x in enumerate(str2):
        matrix.append([])
        for j,y in enumerate(str1):
            if x != y:
                matrix[i].append(0)
            else:
                if i == 0 or j ==0:
                    matrix[i].append(1)
                else:
                    matrix[i].append(matrix[i-1][j-1]+1)
                if matrix[i][j] > xmax:
                    xmax = matrix[i][j]
                    xindex = j
                    xindex += 1
    return str1[xindex - xmax:xindex]
    
print(findstr(s1,s2))
print(findstr(s1,s3))

print("注意，这里两个方法都是判断最长的字符串长度，所以取出来的字符串可能不一样，但是对比两个不同的字符串长度一定是相等的")
