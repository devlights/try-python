# coding: utf-8
"""
itertools モジュールについてのサンプル

以下の処理についてのサンプルです。

- cycle()
"""
import itertools as it

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr, hr


class Sample(SampleBase):
    def exec(self):
        # -----------------------------------------------
        # itertools.cycle()
        # ----------------------
        # itertools.cycleは、名前の通り
        # 最初に指定したシーケンスを繰り返しサイクルする
        # イテレータを生成してくれる。
        #
        # これで生成したイテレータは無限にサイクルするので
        # ストップさせるのは、利用者側の責任になる。
        # -------------------------------------------
        numbers = list(range(0, 9))
        cycle_iter = it.cycle((1, 2, 3))

        hr('itertools.cycle()')

        for i, j in zip(numbers, cycle_iter):
            pr("i,j", f'{i}-{j}')


def go():
    obj = Sample()
    obj.exec()
