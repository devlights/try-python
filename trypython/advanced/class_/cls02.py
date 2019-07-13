# coding: utf-8

"""
Pythonのクラスについてのサンプルです。

__contains__メソッドを実装することによる in のサポートについて
"""
from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        #
        # 特殊メソッド __contains__ を実装することにより
        # 存在判断を in で検査することが可能になる
        #
        contains_support = ContainsProtocolSupport(list(range(10)))

        pr('contains(5)', 5 in contains_support)
        pr('contains(99)', 99 in contains_support)


class ContainsProtocolSupport:
    def __init__(self, items=None):
        super().__init__()
        self.__items = items or list()

    def __contains__(self, item):
        """指定されたアイテムが存在するか否かを返します。"""
        return item in self.__items


def go():
    obj = Sample()
    obj.exec()
