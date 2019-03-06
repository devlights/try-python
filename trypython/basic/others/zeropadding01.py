# coding: utf-8

"""
数値をゼロパディングするサンプルです。
"""
from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        i01 = 1
        i02 = 11
        i03 = 111

        pr('zero-padding-3', f'{i01:03d}')
        pr('zero-padding-3', f'{i02:03d}')
        pr('zero-padding-3', f'{i03:03d}')

        pr('space-padding-3', f'{i01: 3d}')
        pr('space-padding-3', f'{i01:3d}')
        pr('space-padding-3', f'{i01:>3}')


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
