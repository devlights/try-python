# coding: utf-8

"""
vars()についてのサンプルです。
"""
from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        #
        # vars() は、引数無しで呼ぶと locals() と同じ
        # 引数を付与して呼ぶと、そのオブジェクトの __dict__ を返す
        #
        x = 10
        y = 20
        pr('vars()', vars())

        self.fn01(10, 20, 30, **dict(apple=100, pineapple=200))
        Sample.fn02(10, 20, 30, **dict(apple=100, pineapple=200))
        Sample.fn03(10, 20, 30, **dict(apple=100, pineapple=200))

    def fn01(self, *args, **kwargs):
        pr('vars() in method', vars())

    @classmethod
    def fn02(cls, *args, **kwargs):
        pr('vars() in class method', vars())

    @staticmethod
    def fn03(*args, **kwargs):
        pr('vars() in static method', vars())


def go():
    obj = Sample()
    obj.exec()
