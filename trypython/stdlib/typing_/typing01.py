# coding: utf-8
"""
typing.NamedTuple についてのサンプルです。
"""
import collections
import dis
import sys
import typing

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr, hr


class MyData(typing.NamedTuple):
    id: int
    name: str
    age: int


MyData2 = collections.namedtuple('MyData2', 'id name age')


# noinspection PyArgumentList
class Sample(SampleBase):
    def exec(self):
        # ------------------------------------------
        # collections.namedtupleとtyping.NamedTuple
        # -----------------------------------------
        # どちらも同じデータ構造を作り出す。
        # バイトコードも同じとなる。
        # ------------------------------------------
        m1 = MyData(1, 'name01', 33)
        m2 = MyData2(1, 'name22', 22)
        pr('typing.NamedTuple', m1)
        pr('collections.namedtuple', m2)

        pr('getsizeof(typing.NamedTuple)', sys.getsizeof(m1))
        pr('getsizeof(collections.namedtuple)', sys.getsizeof(m2))

        try:
            m1.name = 'name02'
        except AttributeError as e:
            pr('typing.NamedTuple is immutable', e)

        try:
            m2.name = 'name02'
        except AttributeError as e:
            pr('collections.namedtuple is immutable', e)

        hr('dis.dis(MyData)')
        dis.dis(MyData.__new__)

        hr('dis.dis(MyData2)')
        dis.dis(MyData2.__new__)


def go():
    obj = Sample()
    obj.exec()
