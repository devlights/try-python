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
        # (*) 同じ用途で利用できる PrettyTable の方はちゃんと出力できる
        # (*) 2017/02/07 マルチバイト対応した版をプルリクしておいた。
        #     https://github.com/foutaise/texttable/pull/12
        # (*) 2017/04/07 最新版 0.8.8 がリリースされており、日本語対応
        #
        table.add_rows([
            ['1', 'value9999'],
            ['2', 'value12'],
            ['3', '日本語データ']
        ], header=False)

        print(table.draw())


def go():
    obj = Sample()
    obj.exec()
