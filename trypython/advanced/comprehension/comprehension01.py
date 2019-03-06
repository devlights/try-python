# coding: utf-8

"""
内包表記についてのサンプルです。
"""
from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        #
        # 内包表記
        # 内包表記 (comprehension) は、一つ以上のイテレータから
        # Pythonデータ構造をコンパクトに生成出来る形式。
        #
        # 内包表記には以下が存在する。
        # 　　・リスト内包表記
        # 　　・辞書内包表記
        # 　　・集合内包表記
        # 　　・ジェネレータ内包表記
        # タプルの内包表記は存在しない
        #
        seq01 = tuple(range(10))

        #
        # リスト内包表記
        # 以下の形式となる
        #
        # [ expression for item in iterable [if condition] ]
        #
        pr('list-comprehension', [x ** 2 for x in seq01 if x < 5])

        # 2つのシーケンスを使う内包表記も可能
        seq02 = tuple(range(10, 20))
        pr('list-comprehension', [(x, y) for x in seq01 for y in seq02])

        #
        # 辞書内包表記
        # 以下の形式となる
        #
        # { key_item: value_item for item in iterable }
        #
        str01 = 'hello world'
        pr('dict-comprehension', {c: str01.count(c) for c in str01})

        # 上の処理では、同じ文字が存在する場合に同じエントリに対して上書きしているので
        # 少しだけ無駄となる。最適化すると以下のように出来る
        pr('dict-comprehension', {c: str01.count(c) for c in set(str01)})

        #
        # 集合内包表記
        # 以下の形式となる
        #
        # { item for item in iterable }
        #
        pr('set-comprehension', {c for c in str01})

        #
        # ジェネレータ内包表記
        # 以下の形式となる
        #
        # ( item for item in iterable )
        #
        # 注意点：ジェネレータは一度しか利用できない
        gen01 = (c for c in set(str01))
        pr('generator-comprehension', type(gen01))

        for x in gen01:
            pr('generator', x)


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
