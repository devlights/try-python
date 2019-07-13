"""
組み込みクラス float のサンプルです.

float.is_integer() について
"""
from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        num = 1.00
        pr('type(num)', type(num))
        pr('is_integer', num.is_integer())  # ==> True (整数に出来るので)
        pr('int()', int(num))

        num = 1.05
        pr('is_integer', num.is_integer())  # ==> False (整数に出来ないので)
        pr('int()', int(num))


def go():
    obj = Sample()
    obj.exec()
