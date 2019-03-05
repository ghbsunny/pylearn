file1 = '/tmp/test1.txt'
file2 = '/tmp/test2.txt'

f = open(file1,'w+')
lines = ['abcde','123456','sunny']
f.writelines('\n'.join(lines))
f.seek(0)
print(f.read())
f.close()

def copy(src,dest):
    with open(src) as f1:
        with open(dest,'w') as f2:
            f2.write(f1.read())
            f2.write('\n')

copy(file1,file2)
