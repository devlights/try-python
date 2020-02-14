"""
ライブラリ [rich](https://github.com/willmcgugan/rich) のサンプルです.
"""
from trypython.common.commoncls import SampleBase


class Sample(SampleBase):
    def exec(self):
        # ---------------------------------------------------------------
        # rich は、出力を綺麗に見せてくれるライブラリ
        #
        # 出力する文字の色付けや pretty print なオブジェクト出力ができる
        # 最もシンプルな使い方は rich.print を利用すること
        #
        # ref: https://rich.readthedocs.io/en/latest/introduction.html#quick-start
        # ---------------------------------------------------------------
        from rich import print
        print("Hello [bold red]World[/bold red]", locals())

        # 上の例だと python の ビルドイン print() を shadowing してしまうので
        # それが嫌な場合は、以下のように エイリアスをつけて利用する
        from rich import print as rprint
        rprint("Hello [bold red]World[/bold red]", locals())


def go():
    obj = Sample()
    obj.exec()
