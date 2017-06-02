# coding: utf-8
"""
operator モジュールについてのサンプルです。

以下の関数について記述しています。

- add
- attrgetter
- floordiv
- getitem
- itemgetter
- methodcaller
- mod
- mul
- setitem
- sub
- truediv
"""
import collections as coll
import itertools as it
import operator as ope

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        numbers = list(range(1, 11))

        # ----------------------------------------------
        # operator.add
        # -------------------------------
        # x + y と同じ
        # ----------------------------------------------
        pr('operator.add', list(it.accumulate(numbers, func=ope.add)))

        # ----------------------------------------------
        # operator.add
        # -------------------------------
        # x - y と同じ
        # ----------------------------------------------
        pr('operator.sub', list(it.accumulate(numbers, func=ope.sub)))

        # ----------------------------------------------
        # operator.mul
        # -------------------------------
        # x * y と同じ
        # ----------------------------------------------
        pr('operator.mul', list(it.accumulate(numbers, func=ope.mul)))

        # ----------------------------------------------
        # operator.floordiv
        # -------------------------------
        # x // y と同じ
        # ----------------------------------------------
        pr('operator.floordiv', list(it.accumulate(numbers, func=ope.floordiv)))

        # ----------------------------------------------
        # operator.truediv
        # -------------------------------
        # x / y と同じ
        # ----------------------------------------------
        pr('operator.truediv', list(it.accumulate(numbers, func=ope.truediv)))

        # ----------------------------------------------
        # operator.mod
        # -------------------------------
        # x % y と同じ
        # ----------------------------------------------
        pr('operator.mod', list(it.accumulate(numbers, func=ope.mod)))

        # ----------------------------------------------
        # operator.attrgetter
        # -------------------------------
        # x.y と同じ
        # 一度に複数のメンバーを指定することも可能
        # ネストしたメンバー指定も可能
        # ----------------------------------------------
        Rec = coll.namedtuple('Rec', 'id name subrec')
        rec01 = Rec(1, 'name01', Rec(10, 'name10', None))

        ope_getter = ope.attrgetter('name')
        pr('operator.attrgetter', ope_getter(rec01))
        pr('operator.attrgetter', ope.attrgetter('name', 'subrec')(rec01))
        pr('operator.attrgetter', ope.attrgetter('subrec.name')(rec01))

        # ----------------------------------------------
        # operator.getitem
        # -------------------------------
        # x[y] と同じ
        # ----------------------------------------------
        dict01 = dict(id=100, name='name100')
        pr('operator.getitem', ope.getitem(dict01, 'name'))

        # tuple はインデックスアクセスしか出来ないのでインデックスを指定する
        pr('operator.getitem', ope.getitem(rec01, 1))

        # ----------------------------------------------
        # operator.setitem
        # -------------------------------
        # x[y] = z と同じ
        # ----------------------------------------------
        ope.setitem(dict01, 'name', 'hello world')
        pr('operator.setitem', dict01)

        try:
            ope.setitem(rec01, 1, 'hello world')
            pr('operator.setitem', rec01)
        except TypeError as e:
            pr('namedtupleはイミュータブルなのでsetitemは無理', e)

        # ----------------------------------------------
        # operator.methodcaller
        # -------------------------------
        # x.y() と同じ
        # ----------------------------------------------
        WithFuncRec = coll.namedtuple('WithFuncRec', 'id name func')
        with_func = WithFuncRec(1, 'with func', func=ope.add)

        ope_caller = ope.methodcaller('func', 10, 20)
        pr('operator.methodcaller', ope_caller(with_func))


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
