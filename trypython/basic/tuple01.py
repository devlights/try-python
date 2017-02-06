# coding: utf-8

"""
タプルについてのサンプルです。
"""
from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        #
        # タプル
        # タプルは、「組」という概念を表す。
        # (２つで1組とかいったりすることなど)
        #
        # タプルは、リストはディクショナリなどと異なり
        # イミュータブルである。
        #
        # タプルを空で作成するには () とするか、tuple() を利用する
        #
        # リストなどを利用するよりタプルの方がメモリ消費量や速度が効率が良い
        #
        # 標準モジュール collections にはフィールドに名前をつけたり出来る
        # namedtupleというものもある。
        #
        tuple1 = ()
        pr('() でタプルを作成', tuple1)

        try:
            tuple1[0] = 100
        except TypeError as e:
            pr('タプルはイミュータブル', e)

        tuple1 = tuple()
        pr('tuple() でタプルを作成', tuple1)

        #
        # 別のシーケンスからタプルを作成
        #
        list1 = list(range(10))
        tuple2 = tuple(list1)
        pr('別のシーケンスからタプルを作成', tuple2)

        #
        # 一つ以上の要素を持つタプルは、個々の要素をカンマで区切る
        # 要素が一つの場合でも末尾にカンマをつける
        #
        # この際、カッコはつけてもつけなくても良いが
        # 明示的につけたほうがタプルであると分かりやすい。
        #
        tuple3 = 'hello world',
        pr('要素が一つのタプル', tuple3)
        tuple3 = ('hello world',)
        pr('カッコをつけても同じ事になる', tuple3)

        # 要素が複数の場合
        tuple3 = 'hello', 'world'
        pr('要素が複数', tuple3)

        #
        # タプルを使って、一度に複数の値を代入する
        # 「タプルのアンパック」という
        #
        tuple4 = ('hello', 'world')
        hello, world = tuple4
        pr('hello', hello)
        pr('world', world)

        #
        # アンパックを利用すると値のスワップが簡単に出来る
        #
        x = 10
        y = 20
        y, x = x, y
        pr('x', x)
        pr('y', y)

        #
        # 指定された値のインデックスを知る
        #
        tuple5 = tuple(range(10))
        pr('値が５のインデックス', tuple5.index(5))

        #
        # 指定された値のカウントを知る
        #
        tuple6 = 1, 1, 2, 1, 3, 3, 4, 5
        pr('値が1のカウント', tuple6.count(1))


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
