import argparse
import stat
from pathlib import Path
from datetime import datetime

parser = argparse.ArgumentParser(prog='ls',add_help=True,description='list directory contents')
parser.add_argument('path',nargs='?',default='.',help="path help")
parser.add_argument('-l',action='store_true',help="use a long listing format")
parser.add_argument('-a','--all',action='store_true',help="show all files")
parser.add_argument('-H','--human-readable',action='store_true',help = 'with -l,print size in human readable format.')

#print(args)
#parser.print_help()

def listdir(path,all=False,detail=False,human=False):
    #列出文件类型
    def _getfiletype(f:Path):
        if f.is_dir():
            return 'd'
        elif f.is_block_device():
            return 'b'
        elif f.is_char_device():
            return 'c'
        elif f.is_socket():
            return 's'
        elif f.is_symlink():
            return 'l'
        else:
            return '-'



    #将权限位对应为rwxrwxrwx
    modelist = ['r','w','x','r','w','x','r','w','x']
    def _getmodestr(mode:int):
        m = mode & 0o777
        mstr = ''
        for i,v in enumerate(bin(m)[-9:]):
            if v == '1':
                mstr += modelist[i]
            else:
                mstr += '-'
        return mstr
    #文件大小单位转换
    def _gethuman(size:int):
        units = ' KMGTP'
        depth = 0
        while size >= 1000:
            size = size // 1000
            depth += 1
        return '{}{}'.format(size,units[depth])
    #列出本目录下非隐藏目录
    def _listdir(path,all=False,detail=False,human=False):
        p = Path(path)

        for i in p.iterdir():
            if not all and i.name.startswith('.'):
                continue
            if not detail:
                yield (i.name,)
            else:
                st = i.stat()
                mode = _getfiletype(i) + _getmodestr(st.st_mode)
                atime = datetime.fromtimestamp(st.st_atime).strftime('%Y %m %d %H:%M:%S')
                size = str(st.st_size) if not human else _gethuman(st.st_size)
                yield(mode,st.st_nlink,st.st_uid,st.st_gid,size,atime,i.name)

    yield from sorted(_listdir(path,all,detail,human),key=lambda x:x[len(x)-1])

if __name__ == '__main__':
    args = parser.parse_args()#这里可以用[] 中括号表示当前路径，用于解决ls: error: unrecognized arguments: -f 的报错
    print(args)
    #parser.print_help()
    files = listdir(args.path,args.all,args.l,args.human_readable)
    print(list(files))
