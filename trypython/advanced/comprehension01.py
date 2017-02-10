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
        #
        pr('list-comprehension', [x ** 2 for x in seq01 if x < 5])

        #
        # 辞書内包表記
        #

        #
        # 集合内包表記
        #

        #
        # ジェネレータ内包表記
        #


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
