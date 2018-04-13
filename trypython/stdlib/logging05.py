"""
logging モジュールのサンプルです。
応用編 (ハンドラの指定)

参考情報::
https://stackoverflow.com/questions/6167587/the-logging-handlers-how-to-rollover-after-time-or-maxbytes
https://stackoverflow.com/questions/29602352/how-to-mix-logging-handlers-file-timed-and-compress-log-in-the-same-config-f
https://docs.python.jp/3/howto/logging-cookbook.html#using-file-rotation
"""

from trypython.common.commoncls import SampleBase


class Sample(SampleBase):
    """サンプルクラス"""

    def exec(self):
        """サンプル処理を実行します"""
        # -----------------------------------------------------------------------------------
        # logging モジュールは、python 標準ライブラリで他の言語でいう log4jやlog4netなど
        # と同様にロギング処理を提供するもの。公式ドキュメントでは以下のURLで説明が記載されている。
        #
        #     https://docs.python.jp/3/library/logging.html
        #
        # このモジュールは、非常に多機能であるため以下のチュートリアルが用意されている。
        #
        #     基本： https://docs.python.jp/3/howto/logging.html#logging-basic-tutorial
        #     上級： https://docs.python.jp/3/howto/logging.html#logging-advanced-tutorial
        #
        # -----------------------------------------------------------------------------------
        # 今回も、 ハンドラ について
        # loggingモジュールにおける、ハンドラの役目はログをどこに出力するか？という役割を持つ。
        # loggingモジュールは、デフォルトでいろいろな用途に利用できるハンドラを持っている。ハンドラの一覧については以下を参照。
        #     https://docs.python.jp/3/howto/logging.html#useful-handlers
        # -----------------------------------------------------------------------------------
        # StreamHandler

        # FileHandler

        # RotatingFileHandler

        # TimedRotatingFileHandler

        # MemoryHandler

        # NullHandler


def go():
    """処理を実行します"""
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
