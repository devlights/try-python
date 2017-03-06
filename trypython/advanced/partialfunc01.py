# coding: utf-8

"""
functools.partial()を利用した「関数の部分適用」についてのサンプルです。
"""
import functools

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        func01('hello world', 'func01')
        func02('hello world')


def func01(message, prefix):
    pr('func01', f'{prefix}--{message}')


#
# 関数の部分適用
# 予め定義されている func01 に対して prefix が設定済みの
# 新しい定義を生成する
#
func02 = functools.partial(func01, prefix='partial')


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
