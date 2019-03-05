"""
keyword モジュールについてのサンプル

以下の処理についてのサンプルです。

- iskeyword()
"""
import keyword

from common.commoncls import SampleBase
from common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        """サンプル処理を実行します。"""
        # --------------------------------------------------------
        # keyword モジュール
        #
        # keyword モジュールはとてもシンプルなモジュールで
        # iskeyword() という関数のみがある。
        #
        # 名前の通り、指定された文字列がキーワードとして予約されている
        # ものかどうかを判定してくれる。
        # --------------------------------------------------------
        pr('iskeyword("for")', keyword.iskeyword('for'))
        pr('iskeyword("foreach")', keyword.iskeyword('foreach'))


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
