# coding: utf-8

"""
組み込み関数についてのサンプルです。
"""
from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        pass


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
