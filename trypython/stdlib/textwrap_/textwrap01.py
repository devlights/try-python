"""
textwrap モジュールに関するサンプルです。

link::
    https://docs.python.jp/3/library/textwrap.html
"""
import textwrap

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        # -----------------------------------------------------
        # textwrap モジュールは、名前の通り テキストの折り返しなどの
        # 便利関数を持っているモジュール。
        #
        # 所定文字数で折り返したりする必要がある場合に有効
        #
        # 主に利用するのは、以下の3つの関数
        #   - wrap   : 指定したテキストに折り返し処置をして結果をリストで返す
        #   - fill   : 指定したテキストに折り返し処理をして結果を文字列で返す
        #   - shorten : 指定したテキストを指定した幅で切って、残りをプレースホルダにする
        # -----------------------------------------------------
        str01 = 'hello world'
        pr('textwrap.wrap', textwrap.wrap(str01, width=5))
        pr('textwrap.fill', textwrap.fill(str01, width=5))
        pr('textwrap.shorten', textwrap.shorten(str01, width=10, placeholder='...'))


def go():
    obj = Sample()
    obj.exec()
