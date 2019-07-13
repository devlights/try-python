# coding: utf-8

"""
itertools モジュールについてのサンプル

以下の処理についてのサンプルです。

- chain()
- zip_longest()
"""
import itertools as it

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr, hr


class Sample(SampleBase):
    def exec(self):
        # -----------------------------------------------
        # itertools.chain()
        # ----------------------
        # 複数のシーケンスを繋いで一つのようにする。
        # -----------------------------------------------
        hr('it.chain()')

        list01 = ['hello', 'world']
        list02 = list(range(10))

        for x in it.chain(list01, list02, 'abc'):
            pr('value', x)

        # -----------------------------------------------
        # itertools.zip_longest()
        # ----------------------
        # 組み込み関数 zip() の別バージョン
        # 要素数が多い方に合わせる。
        #
        # zip() は、要素が最も少ない方になる。
        # -----------------------------------------------
        hr('it.zip_longest()')

        for x, y in zip(list01, list02):
            pr('zip()', (x, y))

        # zip_longest()は、要素が最も多い方になる
        for x, y in it.zip_longest(list01, list02):
            pr('zip_longest()', (x, y))


def go():
    obj = Sample()
    obj.exec()
