# coding: utf-8

"""
コルーチン (co-routine) についてのサンプルです。

参考:
  http://postd.cc/python-generators-coroutines-native-coroutines-and-async-await/
  https://docs.python.jp/3/library/asyncio-task.html
"""
from typing import Generator, Coroutine

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        #
        # co-routineの基本は、generatorから。
        # generatorは、値を生成する関数。
        # generatorからは、値をpullすることができる。
        # 逆に値を push したい場合は？
        # このような場合に co-routine を利用する。
        #
        # generatorに対して値を push する、つまりコルーチンの処理を
        # するには、send() を利用する。
        #
        gen01 = simple_generator()
        try:
            pr('gen01-type', type(gen01))
            pr('gen01', next(gen01))
            pr('gen01', next(gen01))
            pr('gen01', next(gen01))
        except StopIteration as e:
            pr('gen01', e)

        cor01 = simple_coroutine()
        try:
            pr('cor01-type', type(cor01))
            pr('cor01', next(cor01))
            pr('cor01', next(cor01))
            pr('cor01', next(cor01))
        except StopIteration as e:
            pr('cor01', e)

        cor02 = simple_coroutine()
        try:
            pr('cor02-type', type(cor02))
            pr('cor02-pull', next(cor02))
            pr('cor02-push', cor02.send('world'))
            pr('cor02', next(cor02))
        except StopIteration as e:
            pr('cor02', e)

        cor03 = simple_coroutine2()
        try:
            pr('cor03.pull', next(cor03))
            pr('cor03.push', cor03.send(10), 'send(10)')
            pr('cor03.push', cor03.send(20), 'send(20)')
            pr('cor03.push', cor03.send(30), 'send(30)')
            pr('cor03.push', cor03.send(40), 'send(40)')
            pr('cor03.push', cor03.send(50), 'send(50)')
            pr('cor03.push', cor03.send(-1), 'send(-1)')
        except StopIteration as e:
            pr('cor03', e)


def simple_generator():
    yield 'hello'
    yield 'world'


def simple_coroutine():
    hello = (yield 'hello')
    yield hello


def simple_coroutine2():
    total = 0
    while True:
        push_val = yield total
        pr('\tpush_val', push_val)
        if (push_val < 0):
            pr('break-cor03', push_val)
            break
        total += push_val
    pr('cor03', 'before last yield total')
    yield total

def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
