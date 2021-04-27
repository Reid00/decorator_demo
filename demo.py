# -*- encoding: utf-8 -*-
'''
@File        :demo.py
@Time        :2021/04/27 14:38:59
@Author      :Reid
@Version     :1.0
@Desc        :常见的装饰器例子
'''

# here put the import lib
import time
import logging
from functools import wraps


def timer(func):
    """时间计时装饰器
        不传递函数参数
    """
    @wraps(func)        # 原始的显示被装饰函数的名字
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f'function {func.__name__} cost time {(end - start)} seconds')
        return res      # 内部装饰器返回被装饰函数的调用
    return wrapper         # 外部装饰器返回内部装饰器的对象


def logged(level, name=None, message=None):
    """日志装饰器, 为函数添加日志
        带有函数参数
    Args:
        level (string): 日志等级，五个选择: logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL
        name : 日志名称,  Defaults to 函数的名称
        message: Defaults to 函数的名称.
    """
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorate


class Foo:
    """装饰器，用内置函数__call__ 方法实现
        无参数
    Returns:
        [type]: [description]
    """
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        res = self.func(*args, **kwargs)
        end = time.time()
        print(f'function {self.func.__name__} cost time {end-start}')
        return res


class Foo_with_para:
    """带参数的类装饰器（和不带参数的类装饰器有很大的不同）
       类装饰器的实现，必须实现__call__和__init__两个内置函数。
       __init__：不再接收被装饰函数，而是接收传入参数；
       __call__：接收被装饰函数，实现装饰逻辑

    Returns:
        [type]: [description]
    """
    def __init__(self, level='INFO'):
        self.level = level

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print("[{level}]: the function {func}() is running...".format(level=self.level, func=func.__name__))
            func(*args, **kwargs)
        return wrapper



# @Foo_with_para(level='WARNING')
# @timer
@logged(logging.DEBUG, message='GO')
def add(x, y):
    time.sleep(1)
    return x + y


if __name__ == '__main__':
    print(add(1, 3))