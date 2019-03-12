# coding: utf-8
"""tracemallocモジュールについてのサンプルです。"""
import secrets
import string
import tracemalloc

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def __init__(self) -> None:
        super().__init__()
        self._data_list = None
        self._characters = string.ascii_letters + string.digits

    def exec(self):
        # ----------------------------------------------
        # tracemallocモジュールは、割り当てられたメモリ
        # をトレースするために利用できる。
        #
        # このモジュールを利用すると
        #   トレースバック
        #   メモリブロック
        # などが取得できる。
        #
        # また、メモリリークを検出する際などに便利なのが
        # 2つのスナップショットの差を計算してくれる機能がある。
        #
        # 今回のサンプルでは、メモリ使用量のトップ10を出力
        # (ほぼPythonのドキュメントのサンプルまんま)
        # ----------------------------------------------

        # ------------------------------
        # tracemallocに開始を通知
        # ------------------------------
        tracemalloc.start()

        # 時間とメモリを食う処理を行ってみる
        self._heavy_proc()

        # ------------------------------
        # 現在のスナップショットを取得
        # ------------------------------
        snapshot = tracemalloc.take_snapshot()

        # ------------------------------
        # 統計情報を取得
        #
        # 指定できるのは
        #   'filename' : ファイル名
        #   'lineno'   : ファイル名と行番号
        #   'traceback': トレースバック
        # ------------------------------
        top_stat = snapshot.statistics('lineno')
        for item in top_stat[:10]:
            pr('snapshot-item', item)

    def _heavy_proc(self, count=1000) -> None:
        self._data_list = [self._generate_password() for _ in range(count)]

    def _generate_password(self, nbytes=32) -> str:
        return ''.join(secrets.choice(self._characters) for _ in range(nbytes))


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
