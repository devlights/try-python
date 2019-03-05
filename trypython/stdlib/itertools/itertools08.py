# coding: utf-8
"""
itertools モジュールについてのサンプル

以下の処理についてのサンプルです。

- product()
"""
import datetime as dt
import itertools as it

import pandas as pd

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr, hr


class Sample(SampleBase):
    def exec(self):
        # -----------------------------------------------
        # itertools.product()
        # ----------------------
        # デカルト積を求める。とドキュメントに記載されているが
        # 要は list01 と list02 が存在する場合
        #     (x, y) for x in list01 for y in list02
        # と同じことになる。
        #
        # キーワード引数の repeat を利用すると直積も求められる。
        # -----------------------------------------------
        hr('it.product()')

        list01 = list('ABC')
        list02 = list('DEF')

        pr('it.product(*iterable)', list(it.product(list01, list02)))
        pr('listcomp', [(x, y) for x in list01 for y in list02])

        pr('it.product(*iterable, repeat=2)', list(it.product('AB', repeat=4)))

        # テストデータを一気に生成するときに便利
        date_range = pd.date_range(dt.date.today(), periods=3, freq='D')
        values = (10, 11, 12)

        pr('it.product', list(it.product(date_range, values)))
        pr('listcomp', [(d, v) for d in date_range for v in values])  # 同じ

        # -----------------------------------------------
        # itertools.permutations()
        # ----------------------
        # 順列を生成する。(e.g. 5! = 5*4*3*2*1 = 120)
        # 第二引数に順列の長さを指定できる。省略可能
        # 長さにNone(これがデフォルト)を指定すると
        # 可能な最長の順列が生成される。
        # -----------------------------------------------
        hr('it.permutations()')
        pr('it.permutations(r=None)...(3!=3*2*1)', list(it.permutations('ABC')))

        # 長さを指定することで、シーケンスからいくつ選ぶのかを指定できる
        pr('it.permutations(r=3)...(4p3=4*3*2)', len(list(it.permutations('ABCD', r=3))))
        pr('it.permutations(r=2)...(4p2=4*3)', len(list(it.permutations('ABCD', r=2))))

        # -----------------------------------------------
        # itertools.combinations()
        # ----------------------
        # 組合せを生成する。
        # 第二引数は必須。
        #
        # 並べる際の順序を無視した結果を返す。
        # つまり、(a, b, c)と(b, a, c)と(c, b, a)は同じとみなす。
        # -----------------------------------------------
        hr('it.combinations()')
        pr('it.combinations(r=2)...(4c2=4p2/2!)', list(it.combinations('ABCD', r=2)))
        pr('it.combinations(r=2)...(4c2=4p2/2!)', len(list(it.combinations('ABCD', r=2))))

        # combinations_with_replacement() は、それぞれの要素が重複することを許す
        pr('it.combinations_with_replacement(r=2)', list(it.combinations_with_replacement('ABCD', r=2)))
        pr('it.combinations_with_replacement(r=2)', len(list(it.combinations_with_replacement('ABCD', r=2))))


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
