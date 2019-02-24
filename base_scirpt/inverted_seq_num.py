num = 123487
def revert(num,target=[]):
    if num:
        target.append(num[len(num)-1])
        revert(num[:len(num)-1])
    return target
print(revert(str(num)))
print('-----------------------------------------')
data = str(123487)
def reversal(x):
    if x == -1:
        return ''
    else:
        return data[x] + reversal(x-1)
print(reversal(len(data)-1))
