import time
import inspect
from functools import wraps
import datetime
"""
函数最终会返回key 和 local_cache[key]
并把超过10s的值进行清0
"""

def sunny_cache(duration):
    def _cache(fn):
        local_cache = {}

        @wraps(fn)
        def wrapper(*args, **kwargs):
            def clear_expire(cache):
                expire_keys = []
                for k, (_, stamp) in cache.items(): #记住时间戳
                    now = datetime.datetime.now().timestamp()
                    if now - stamp > duration: #计算是否超过规定的时间范围
                        expire_keys.append(k)
                for k in expire_keys:
                    cache.pop(k)

            clear_expire(local_cache)

            def make_key():
                sig = inspect.signature(fn)
                params = sig.parameters
                param_names = list(params.keys())
                params_dict = {}

                for i, v in enumerate(args):
                    k = param_names[i]
                    params_dict[k] = v
                params_dict.update(kwargs)

                for k, v in params.items():
                    if k not in params_dict.keys():
                        params_dict[k] = v.default

                return tuple(sorted(params_dict.items()))

            key = make_key()

            if key not in local_cache.keys():
                local_cache[key] = (fn(*args, **kwargs), datetime.datetime.now().timestamp())

            return key, local_cache[key] # 这里是内部函数返回的值

        return wrapper

    return _cache


def logger(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        ret = fn(*args, **kwargs)
        delta = (datetime.datetime.now() - start).total_seconds()
        print(fn.__name__, delta)  #返回执行的函数名 和 该函数执行的时间
        return ret
    
    return wrapper


@logger
@sunny_cache(10)
def add(x, z, y=6):
    time.sleep(2)
    return x + y + z


result = []
result.append(add(4, 5))
result.append(add(4, z=5))
result.append(add(4, y=8, z=5))
result.append(add(y=6, z=5, x=4))
result.append(add(4, 5, 6))
result.append(add(4, 6))
result.append(add(y=6, z=5, x=4))
result.append(add(y=7, z=5, x=4))
result.append(add(y=8, z=5, x=4))
result.append(add(y=9, z=5, x=4))
result.append(add(y=10, z=5, x=4))
result.append(add(y=11, z=5, x=4))
print("after 10s")
result.append(add(4, y=8, z=5))
for x in result:
    print(x)
print(result)
