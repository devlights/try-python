# coding: utf-8

"""
ジェネレータについてのサンプルです。
"""
from typing import Iterator

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        #
        # ジェネレータは、Pythonのシーケンスを作成するオブジェクト
        # ジェネレータを使うと、シーケンス全体をメモリに格納しなくても
        # シーケンスを反復処理出来る
        #
        # 大きくなる可能性があるシーケンスを作りたいが
        # ジェネレータ内包表記に収めるいはコードが大きすぎる際は
        # ジェネレータ関数を利用する
        #
        # ジェネレータ関数を作るには、値を return で返す代わりに
        # yield を利用する
        #

        # make_generator自身は普通の関数
        pr('make_generator', type(Sample.make_generator))

        # 返す値は ジェネレータ となる
        gen01 = Sample.make_generator(1, 5)
        pr('make_generator_result', type(gen01))

        # 通常通り利用できる
        for x in gen01:
            pr('generator', x)

    @staticmethod
    def make_generator(start: int, end: int) -> Iterator[int]:
        # ジェネレータは、反復処理の度に最後に呼び出されたときに
        # どの値だったのかを管理して、次の値を返す。一つ前の状態のみを覚えている
        number = start
        while number < end:
            # yield で返すことで generator となる
            yield number
            number += 1


def go():
    obj = Sample()
    obj.exec()
