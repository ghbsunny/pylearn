import random
import datetime
import time
from queue import Queue
import threading


def source(second=1):
    '''
    以下函数用于生成数据
    '''
    while True:
        yield {
            'datetime':datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))),
            'value':random.randint(1,100)
        }
        time.sleep(second)
        
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
        data = src.get()
        if data:
            buffer.append(data)
            current = data['datetime']
        
        #每间隔interval时间就计算一次buffer里的数据
        if (current - start).total_seconds() >= interval:
            ret = handler(buffer)
            print('{:.2f}'.format(ret))
            start = current
        
        #清除超出width的数据
        buffer = [x for x in buffer if x['datetime'] > current-delta ]
        
def handler(iterable):
    '''
    处理函数，计算一个buffer里取得数值的平均值
    '''
    return sum(map(lambda x:x['value'],iterable))/len(iterable)

def dispatcher(src):
    #分发器中记录handler,同时保存在各自的队列里
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
        
    return reg,run

reg,run = dispatcher(source())

reg(handler,10,5)
run()
    
