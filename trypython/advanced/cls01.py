# coding: utf-8

"""
Pythonのクラスについてのサンプルです。

__iter__メソッドを実装することによるイテレータプロトコルのサポートについて
"""
from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        #
        # 特殊メソッド __iter__ を実装することにより
        # イテレータプロトコルをサポート出来る
        #
        iter_support = IterProtocolSupport(list(range(10)))
        for item in iter_support:
            pr('item', item)


class IterProtocolSupport:
    def __init__(self, items=None):
        super().__init__()
        self.__items = items or list()

    def __iter__(self):
        """イテレータを返します。"""
        for item in self.__items:
            yield item

            #
            # 以下でも同じ事になる
            # yieldを利用する代わりに、ジェネレータ式を返している
            #
            # return (item for item in self.__items)


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
