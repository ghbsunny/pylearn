import random
import datetime
import time
from queue import Queue
import threading
import re
from pathlib import Path

pattern = '''(?P<remote>[\d.]{7,}\s-\s-\s\[(?P<datetime>[^\[\]]+)\])\s\
"(?P<method>.*)\s(?P<url>.*)\s(?P<protocol>.*)"\s(?P<status>\d{3})\s(?P<size>\d+)\s"[^"]+"\s"(?P<useragent>[^"]+)"'''

regex = re.compile(pattern)

ops = {
    'datetime':lambda datestr:datetime.datetime.strptime(datestr,'%d/%b/%Y:%H:%M:%S %z'),
    'status':int,
    'size':int
}

def extract(line:str) -> dict:
    matcher = regex.match(line)
    if matcher:
        return {name:ops.get(name,lambda x:x)(data) for name,data in matcher.groupdict().items()}

#装载文件
def openfile(path:str):
    """装载日志文件"""
    with open(path) as f:
        for line in f:
            fields = extract(line)
            if fields:
                yield fields
            else:
                continue

def load(*paths):
    for item in paths:
        p = Path(item)
        if not p.exists():
            continue
        if p.is_dir():
            for file in p.iterdir():
                if file.is_file():
                    yield from openfile(str(file))
        elif p.is_file():
            yield from openfile(str(p))

#数据处理
def source(second=1):
    """生成数据"""
    while True:
        yield {
            'datetime':datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))),
            'value':random.randint(1,100)
        }
        time.sleep(second)

            
#滑动窗口函数
def window(src:Queue,handler,width:int,interval:int):
    '''
    窗口函数，表示间隔一段时间取出一定的数据进行处理
    :param src:数据源，这里是缓存队列，用于获取数据
    ：param handler:数据处理的函数
    ：param width:时间窗口函数，秒
    ：param interval:处理时间间隔，秒
    '''
    start = datetime.datetime.strptime('20170101 000000 +0800','%Y%m%d %H%M%S %z')
    current = datetime.datetime.strptime('20170101 010000 +0800','%Y%m%d %H%M%S %z')
    buffer = []
    delta =datetime.timedelta(seconds=width-interval)
    
    while True:
        #从数据源获取数据
        data = src.get() #这个代码会阻塞，等待数据输入，没有数据输入就阻塞
        if data:
            buffer.append(data)
            current = data['datetime'] #存入临时缓冲等待计算
        
        #每隔interval重新计算buffer中的一次数据
        if(current - start).total_seconds() >=interval:
            ret = handler(buffer)
            print('{}'.format(ret))
            start = current
            #清除超出width的数据
            buffer = [x for x in buffer if x['datetime'] > current-delta]
        
#随机数平均的测算函数
source()

def handler(iterable):
    return sum(map(lambda x:x['value'],iterable)) / len(iterable)
    #print(sum(map(lambda x:x['value'],iterable))/len(iterable))

#测试函数
def donothing_handler(iterable):
    return iterable

#状态码占比
def status_handler(iterable):
    #时间窗口内的一批数据
    status = {}
    for item in iterable:
        key = item['status']
        status[key] = status.get(key,0) + 1
    total = len(iterable)
    return {k:status[k]/total for k,v in status.items()}

#分发器
def dispatcher(src):
    #分发器中记录handler,同时保存各自的队列
    handlers = []
    queues = []
    
    def reg(handler,width:int,interval:int):
        """
        注册窗口处理函数
        ：param handler:注册数据处理函数
        ：param width:时间窗口宽度
        ：param interval:时间间隔
        """
        q = Queue()
        queues.append(q)
        h= threading.Thread(target=window,args=(q,handler,width,interval))
        handlers.append(h)
        
    def run():
        #启动线程处理数据
        for t in handlers:
            t.start()
        
        #将获取到的数据分发到所有的队列中
        for item in src:
            for q in queues:
                q.put(item)
                #print(q.get())
    return reg,run


if __name__ == "__main__":
    import sys
    path = '/tmp/test.log'
    reg,run = dispatcher(load(path))
    reg(status_handler,10,5)
    run()
