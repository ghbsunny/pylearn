#判断目录是否为目录，为目录，判断是否为空目录
from pathlib import Path
p = Path('/tmp/a/b/c/d/f.txt')
for x in p.parents[len(p.parents)-3].iterdir():
    print(x,end = '\t')
    if x.is_dir():
        flag = False
        for _ in x.iterdir():
            flag = True
            break
        print('dir',x,'is not empty' if flag else 'Empty',sep='\t')
    elif x.is_file():
        print('file')
    else:
        print('other file')
