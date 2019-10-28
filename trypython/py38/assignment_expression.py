"""
Python 3.8 にて導入された Assignment Expression (Walrus operator) についてのサンプルです。

REFERENCES:: http://bit.ly/2NlJkSc
"""
import random

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        # ------------------------------------------------------------
        # Assignment Expression (Walrus operator)
        #
        # 通称「セイウチ演算子」 := を横から見るとセイウチに似ているのでこの名前がついている
        # := は、代入と評価を同時に行うことができる.
        # ------------------------------------------------------------
        # Python 3.7 までは以下のように記載していた
        walrus = False
        pr('walrus = True', walrus)

        # Python 3.8 からの Assignment Expression を利用すると以下のように書ける
        pr('walrus := True', walrus := True)
        pr('walrus', walrus)

        # Python 3.7 までは以下のように記載していた
        num = self._get_random_num()
        if num < 5:
            print(f'num < 5 {num}')
        else:
            print(f'num >= 5 {num}')

        # Python 3.8 では以下のように書ける
        if num := self._get_random_num() < 5:
            print(f'[walrus] num < 5 {num}')
        else:
            print(f'[walrus] num >= 5 {num}')

    # noinspection PyMethodMayBeStatic
    def _get_random_num(self):
        return random.randint(1, 10)


def go():
    obj = Sample()
    obj.exec()
