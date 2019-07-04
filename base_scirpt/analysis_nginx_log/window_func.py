#取出一段区间内的随机数的和的平均值，该函数无限循环
import random
import datetime
import time

def source(second=1):
    while True:
        yield {
            'datetime':datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))),
            'value':random.randint(1,100)
        }
        time.sleep(second)

def window(iterator,handler,width:int,interval:int):
    """
    窗口函数
    ：param iterator : 数据源，生成器，用来获取数据
    ：param handler:数据处理函数
    ：param width:时间窗口宽度，秒
    ：param interval:处理时间间隔，秒
    """
    
    start = datetime.datetime.strptime('20170101 000000 +0800','%Y%m%d %H%M%S %z')
    current = datetime.datetime.strptime('20170101 010000 +0800','%Y%m%d %H%M%S %z')
    buffer = []
    delta = datetime.timedelta(seconds = width-interval)
    
    while True:
        data = next(iterator)
        #以下判断是将数值追加到buffer里
        if data:
            buffer.append(data)
            print(buffer)
            current = data['datetime']
            print(current)
        #如果当前时间减去
        #开始时间大于区间，则返回handler函数处理的值，并对函数值进行格式化，重新赋值给start，将后续的的值存入到buffer里,超出width区间的值会被清除    
        if (current-start).total_seconds() >= interval:
            ret = handler(buffer)
            print(ret)
            print('{:.2f}'.format(ret))
            start = current
	   #清除超出width区间的数据
            buffer = [x for x in buffer if x['datetime']>current-delta]
            
def handler(iterable):
    return sum(map(lambda x:x['value'],iterable))/len(iterable)

window(source(),handler,10,2)
