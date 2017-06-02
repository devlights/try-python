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

        # x + y と同じ
        pr('operator.add', list(it.accumulate(numbers, func=ope.add)))

        # x - y と同じ
        pr('operator.sub', list(it.accumulate(numbers, func=ope.sub)))

        # x * y と同じ
        pr('operator.mul', list(it.accumulate(numbers, func=ope.mul)))

        # x // y と同じ
        pr('operator.floordiv', list(it.accumulate(numbers, func=ope.floordiv)))

        # x / y と同じ
        pr('operator.truediv', list(it.accumulate(numbers, func=ope.truediv)))

        # x % y と同じ
        pr('operator.mod', list(it.accumulate(numbers, func=ope.mod)))

        Rec = coll.namedtuple('Rec', 'id name subrec')
        rec01 = Rec(1, 'name01', Rec(10, 'name10', None))

        ope_getter = ope.attrgetter('name')
        pr('operator.attrgetter', ope_getter(rec01))
        pr('operator.attrgetter', ope.attrgetter('name', 'subrec')(rec01))
        pr('operator.attrgetter', ope.attrgetter('subrec.name')(rec01))

def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
