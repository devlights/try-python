"""
logging モジュールのサンプルです。
応用編 (ハンドラの指定)

参考情報::
https://docs.python.jp/3/howto/logging-cookbook.html#using-file-rotation
https://aoishi.hateblo.jp/entry/2017/10/09/021054
https://stackoverflow.com/questions/6167587/the-logging-handlers-how-to-rollover-after-time-or-maxbytes
https://stackoverflow.com/questions/29602352/how-to-mix-logging-handlers-file-timed-and-compress-log-in-the-same-config-f
"""
import io
import logging
import sys

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
        #   最も基本的なハンドラ。ストリームを指定してログを出力することが出来る。
        #   デフォルトは、 sys.stderr となっている。 loggingモジュールにてハンドラを設定ていない状態で
        #   利用すると自動的に追加されるのが、このハンドラ。
        # -----------------------------------------------------------------------------------
        logger = logging.getLogger('default_streamhandler')

        # ハンドラを設定しないまま利用するので、 StreamHandler(sys.stderr) が自動で追加される
        logger.warning('[StreamHandler] default')

        # sys.stdout の StreamHandler を追加して出力。
        logger = logging.getLogger('stdout_streamhandler')
        handler = logging.StreamHandler(sys.stdout)
        logger.addHandler(handler)

        logger.warning('[StreamHandler] add StreamHandler(sys.stdout)')

        # io.StringIO を使うとユニットテスト時などに便利
        logger = logging.getLogger('stringio_streamhandler')
        buf = io.StringIO()
        handler = logging.StreamHandler(buf)
        logger.addHandler(handler)

        logger.warning(logger.name)

        handler.flush()
        buf.seek(io.SEEK_SET)
        message = buf.read().rstrip()  # ログ出力時に末尾に改行文字が追加されているため除去

        assert logger.name == message

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
