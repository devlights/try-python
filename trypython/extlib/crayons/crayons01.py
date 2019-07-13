"""
コンソール上に色付き文字列を表示してくれるライブラリ crayons のサンプルです。

REFERENCES::
https://github.com/kennethreitz/crayons
"""
import crayons

from trypython.common.commoncls import SampleBase


class Sample(SampleBase):
    """ライブラリ crayons のサンプルです。"""

    def exec(self):
        """サンプル処理を実行します。"""
        # 赤色で太字な文字列を構築
        red_bold_string = crayons.red('[RED] helloworld', bold=True)
        # 黄色な文字列を構築
        yellow_normal_string = crayons.yellow('[YELLOW] hellowworld', bold=False)

        print(red_bold_string)
        print(yellow_normal_string)


def go():
    """サンプルを実行します。"""
    obj = Sample()
    obj.exec()
