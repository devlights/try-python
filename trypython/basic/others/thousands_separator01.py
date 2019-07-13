# coding: utf-8

"""
1000区切りのカンマで書式出力するための方法についてのサンプルです。
"""
from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        i = 123456789
        pr('thousands separator', str.format('{0:,d}', i))
        pr('thousands separator', str.format('{0:20,d}', i))


def go():
    obj = Sample()
    obj.exec()
