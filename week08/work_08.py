"""
作业一：

区分以下类型哪些是容器序列哪些是扁平序列，哪些是可变序列哪些是不可变序列：

list
tuple
str
dict
collections.deque
作业二：
自定义一个 python 函数，实现 map() 函数的功能。

作业三：
实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。

"""

"""

容器序列：可以存放不同类型的数据，即存放的是对象引用，包括以下： list,tuple,dict,collection.deque

扁平序列：存放的是相同类型的数据，是一段连续的内存空间。扁平序列更加的紧凑，只能存放一种类型比如 str,bytes,bytearray,memoryview 包括以下：str


可变序列：存储的内容可变，但地址不一定变。在改变地址的前提下改变自身存储的内容 包括以下：list,dict,collection.deque

不可变序列：存储的内容可变，地址一定变。只能通过改变自己的地址，来改变存储的内容 包括以下：tuple,str,


"""
from typing import Callable, Iterable
import datetime
import time


def my_map(my_func: Callable, iterables: Iterable):
    # map()
    """
    自定义一个 python 函数，实现 map() 函数的功能。
    :param my_func:
    :param iterables:
    :return:
    """
    if hasattr(iterables, '__iter__'):
        """
            参数 iterables 是一个可以迭代的对象
            可迭代对有属性 __iter__
        """
        for p in iterables:
            yield my_func(p)


def timer(func):
    def int_time(*args, **kwargs):
        start_time = datetime.datetime.now()
        func(*args, **kwargs)
        end_time = datetime.datetime.now()
        ts = (end_time - start_time).total_seconds()
        print('total time:{}s'.format(ts))

    return int_time


@timer
def main():
    print('main is running...')
    for i in range(1, 3):
        time.sleep(i)


@timer
def main_2(num):
    print(f'main2 num:{num} is running...')
    for n in range(1, num):
        time.sleep(n)


@timer
def main_3(num, str):
    print(f'main2 num:{num},str:{str} is running...')
    for n in range(1, num):
        time.sleep(n)


if __name__ == '__main__':
    # main()

    for j in range(1, 5):
        # main_2(j)
        main_3(j, 'guo')
