# coding: utf-8

"""
タプルと辞書のアンパックについてのサンプルです。
"""
from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        t1 = (10, 20)
        self.output_args(*t1)

        l1 = [30, 40]
        self.output_args(*l1)

        d1 = dict(apple=10, pineapple=20)
        self.output_kwargs(**d1)

    def output_args(self, *args):
        pr('args', args)

    def output_kwargs(self, **kwargs):
        pr('kwargs', kwargs)


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
