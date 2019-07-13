"""
logging モジュールのサンプルです。
最も基本的な使い方について (ファイルへの出力)
"""
import logging
import pathlib
import tempfile

from trypython.common.commoncls import SampleBase


class Sample(SampleBase):
    def exec(self):
        """サンプル処理を実行します。"""
        # --------------------------------------------------------
        # logging モジュールは、python 標準ライブラリで他の言語でいう
        # log4jやlog4netなどと同様にロギング処理を提供するもの。
        # 公式ドキュメントでは以下のURLで説明が記載されている。
        #
        # https://docs.python.jp/3/library/logging.html
        #
        # 非常に多機能であるため以下のチュートリアルが用意されている。
        #
        # 基本：https://docs.python.jp/3/howto/logging.html#logging-basic-tutorial
        # 上級：https://docs.python.jp/3/howto/logging.html#logging-advanced-tutorial
        #
        # --------------------------------------------------------
        # 今回も、 logging.basicConfig() について
        # filename キーワードを指定して、出力するファイル名を指定する。
        # --------------------------------------------------------
        logdir = pathlib.Path(tempfile.gettempdir())
        logfile = logdir / 'logging02.log'
        logging.basicConfig(level=logging.INFO, filename=str(logfile))
        logger = logging.getLogger(__name__)

        # それぞれのログレベルで出力
        logger.debug('debug')
        logger.info('info')
        logger.warning('warn')
        logger.error('error')
        logger.critical('critical')

        # ロギングを終了。強制的に flush を実施。
        # 基本必要ないが、大量にログを入れた後にすぐに終了や
        # 対象ログファイルを開こうとすると、PermissionErrorが発生
        # する場合があるため。
        #
        # 今回のサンプルのように、ログ・ファイルに出力して、すぐにそのファイルを
        # 開こうとすると PermissionError が発生する場合がある。
        # (丁度 logging が、そのファイルに出力している最中に開くと例外となる)
        logging.shutdown()

        with logfile.open(mode='r', encoding='utf-8') as f:
            for l in f:
                print(l, end='')

        logfile.unlink()


def go():
    """処理を実行します。"""
    obj = Sample()
    obj.exec()
