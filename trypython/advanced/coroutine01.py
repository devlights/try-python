# coding: utf-8

"""
コルーチン (co-routine) についてのサンプルです。

参考:
  http://postd.cc/python-generators-coroutines-native-coroutines-and-async-await/
  https://docs.python.jp/3/library/asyncio-task.html
"""
from typing import Generator

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        gen01 = simple_generator()
        try:
            pr('gen01', next(gen01))
            pr('gen01', next(gen01))
            pr('gen01', next(gen01))
        except StopIteration as e:
            pr('gen01', e)


def simple_generator() -> Generator[str, None, None]:
    yield 'hello'
    yield 'world'


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
