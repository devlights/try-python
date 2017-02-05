# coding: utf-8

"""
セットについてのサンプルです。
"""
from trypython.common.commoncls import SampleBase


class Sample(SampleBase):
    def exec(self):
        pass


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
