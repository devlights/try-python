"""
sys モジュールに関するサンプルです。

- sys.executable について
"""
import sys

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        # -------------------------------------------------------
        # sys モジュール
        # -------------
        # sys.executable から、現在動作中の python インタープリタの
        # 絶対パスが取得できる。 システムに複数の python がインストールされていたり
        # venv 環境下で作業している場合に、実行パスを間違えないように
        # ここから取得するほうが良い。
        # -------------
        # subprocess モジュールを使って、内部から別プロセスで python を起動する際にも
        # sys.executable からパスを取得して起動すれば間違いがない。
        # -------------------------------------------------------
        pr('sys.executable', sys.executable)


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
