import random
import datetime
import time
from queue import Queue
import threading
import re
from pathlib import Path
from user_agents import parse
"""
这段代码，实现了再一段时间内获得数据，通过不同的handler（即消费端函数）
对获取到的同一份数据进行处理，主要是两段消费函数，网页返回的code的统计和浏览器的分析
这段代码，窗口函数中，data = src.get(),使得没有新的数据产生时，该代码会阻塞，直到有新的数据生成，再次进行处理
"""
pattern = '''(?P<remote>[\d.]{7,}\s-\s-\s\[(?P<datetime>[^\[\]]+)\])\s\
"(?P<method>.*)\s(?P<url>.*)\s(?P<protocol>.*)"\s(?P<status>\d{3})\s(?P<size>\d+)\s"[^"]+"\s"(?P<useragent>[^"]+)"'''

#编译
regex = re.compile(pattern)

#构造字典
ops = {
    'datetime': lambda datestr: datetime.datetime.strptime(datestr, '%d/%b/%Y:%H:%M:%S %z'),
    'status': int,
    'size': int,
    'useragent': lambda ua: parse(ua)
}

#提取信息
def extract(line: str) -> dict:
    matcher = regex.match(line)
    if matcher:
        return {name: ops.get(name, lambda x: x)(data) for name, data in matcher.groupdict().items()}


# 打开文件
def openfile(path: str):
    """装载日志文件"""
    with open(path) as f:
        for line in f:
            fields = extract(line)
            if fields:
                yield fields
            else:
                continue

#装载文件，判断文件类型已经是否存在
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


# 随机生成100以内的数字
def source(second=1):
    """生成数据"""
    while True:
        yield {
            'datetime': datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))),
            'value': random.randint(1, 100)
        }
        time.sleep(second)


# 滑动窗口函数
def window(src: Queue, handler, width: int, interval: int):
    '''
    窗口函数，表示间隔一段时间取出一定的数据进行处理
    :param src:数据源，这里是缓存队列，用于获取数据
    ：param handler:数据处理的函数
    ：param width:时间窗口函数，秒
    ：param interval:处理时间间隔，秒
    '''
    start = datetime.datetime.strptime('20170101 000000 +0800', '%Y%m%d %H%M%S %z')
    current = datetime.datetime.strptime('20170101 010000 +0800', '%Y%m%d %H%M%S %z')
    buffer = []
    delta = datetime.timedelta(seconds=width - interval)

    while True:
        # 从数据源获取数据
        data = src.get()  # 这个代码会阻塞，等待数据输入，没有数据输入就阻塞
        if data:
            buffer.append(data)
            current = data['datetime']  # 存入临时缓冲等待计算

        # 每隔interval重新计算buffer中的一次数据
        if (current - start).total_seconds() >= interval:
            ret = handler(buffer)
            start = current
            # 清除超出width的数据
            buffer = [x for x in buffer if x['datetime'] > current - delta]


# 随机数平均的测算函数
source()
def handler(iterable):
    #return sum(map(lambda x: x['value'], iterable)) / len(iterable)
    print(sum(map(lambda x:x['value'],iterable))/len(iterable))


# 测试函数
def donothing_handler(iterable):
    #return iterable
    print(iterable)


# 状态码占比
def status_handler(iterable):
    # 时间窗口内的一批数据
    status = {}
    for item in iterable:
        key = item['status']
        status[key] = status.get(key, 0) + 1
    total = len(iterable)
    print({k:float( "{:.2f}".format(status[k] / total)) for k, v in status.items()})
    return {k: status[k] / total for k, v in status.items()}


# 浏览器分析
allbrowsers = {}


def browser_handler(iterable):
    browsers = {}
    for item in iterable:
        ua = item['useragent']
        key = (ua.browser.family, ua.browser.version_string)
        browsers[key] = browsers.get(key, 0) + 1
        allbrowsers[key] = allbrowsers.get(key, 0) + 1

    print(sorted(allbrowsers.items(), key=lambda x: x[1], reverse=True)[:10])
    return browsers


# 分发器
def dispatcher(src):
    # 分发器中记录handler,同时保存各自的队列
    handlers = []
    queues = []

    def reg(handler, width: int, interval: int):
        """
        注册窗口处理函数
        ：param handler:注册数据处理函数
        ：param width:时间窗口宽度
        ：param interval:时间间隔
        """
        q = Queue()
        queues.append(q)
        # 多线程，数据并行
        h = threading.Thread(target=window, args=(q, handler, width, interval))
        handlers.append(h)

    def run():
        # 启动线程处理数据
        for t in handlers:
            t.start()

        # 将获取到的数据分发到所有的队列中
        for item in src:
            for q in queues:
                q.put(item)
                # print(q.get())

    return reg, run


if __name__ == "__main__":
    import sys

    path = '/tmp/test.log'
    """
    以下的代码为测试用的，用于统计每隔5s统计10s内的随机数字的平均值
    reg, run = dispatcher(source())
    reg(handler, 10, 5)
    """

    reg, run = dispatcher(load(path))

    #每隔5s返回过去10s的数据，但是不做处理
    reg(donothing_handler, 10, 5)
    #每隔5s统计10s内的返回状态码的占比情况
    reg(status_handler, 10, 5)
    # 每隔5s统计10s内的浏览器类型占比情况，展示排行10s内访问量前十的浏览器
    reg(browser_handler,10,5)
    run()
