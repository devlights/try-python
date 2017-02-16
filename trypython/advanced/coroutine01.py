# coding: utf-8

"""
コルーチン (co-routine) についてのサンプルです。
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
