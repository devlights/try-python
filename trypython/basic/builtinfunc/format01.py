"""
数値フォーマットについてのサンプルです.

数値のフォーマットについて
"""
from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        num = 7.125
        pr('.2f', format(num, '.2f'))  # ==> 7.12
        pr(',', format(num, ','))  # ==> 7.125
        pr(',.2f', format(num, ',.2f'))  # ==> 7.12

        ratio = 0.9
        pr('.1%', format(ratio, '.1%'))  # ==> 90.0%


def go():
    obj = Sample()
    obj.exec()
