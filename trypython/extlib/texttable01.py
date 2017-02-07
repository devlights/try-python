# coding: utf-8

"""
texttable モジュールについてのサンプルです。
"""
from texttable import Texttable

from trypython.common.commoncls import SampleBase


class Sample(SampleBase):
    def exec(self):
        table = Texttable()

        # 列の align
        table.set_cols_align(['r', 'l'])
        table.set_cols_valign(['m', 'm'])

        # ヘッダ
        table.header(['id', 'value'])

        # 行
        #   header=True とすると一行目をヘッダとみなす
        #   header=False とすると指定されたデータすべてを行とする
        #   デフォルトは True となっている
        #
        # (*) 日本語データだときれいに出力できなかった
        table.add_rows([
            ['1', 'value1'],
            ['3', 'value9999']
        ], header=False)

        print(table.draw())


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
