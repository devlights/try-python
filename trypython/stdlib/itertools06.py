# coding: utf-8
"""
itertools モジュールについてのサンプル

以下の処理についてのサンプルです。

- islice()
"""
import itertools as it

from common.commoncls import SampleBase
from common.commonfunc import pr, hr


class Sample(SampleBase):
    def exec(self):
        # -----------------------------------------------
        # itertools.islice()
        # ----------------------
        # 指定されたイテレータブルに対してスライスを行う。
        # islice() には、キーワード引数が存在せず位置引数のみ。
        # なので、値の指定数で挙動が変わる。
        # 戻り値も当然イテレータとなっている。
        #
        # 引数が一つの場合、stopが指定された状態となる。
        # 引数が二つの場合、start, stopが指定された状態となる。
        # 引数が三つの場合、start, stop, stepが指定された(略
        # -----------------------------------------------
        hr('it.islice()')

        data01 = list(range(10))
        pr('it.islice(8)', list(it.islice(data01, 8)))
        pr('it.islice(5,8)', list(it.islice(data01, 5, 8)))
        pr('it.islice(2,8,2)', list(it.islice(data01, 2, 8, 2)))

        # stop には、None が指定可能。None を指定した場合は最後までという意味となる。
        pr('it.islice(5,None)', list(it.islice(data01, 5, None)))


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
