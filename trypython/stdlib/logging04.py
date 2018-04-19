"""
logging モジュールのサンプルです。
最も基本的な使い方について (日付書式の指定)
"""
import logging

from trypython.common.commoncls import SampleBase


class Sample(SampleBase):
    def exec(self):
        """サンプルの処理を実行します。"""
        # --------------------------------------------------------
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
        # --------------------------------------------------------
        # 今回も、 logging.basicConfig() について
        # datefmt キーワードを指定して、日付文字列のフォーマットを変更する。
        # datefmt 文字列内にて指定できるキーワードについては、以下を参照。
        # (time.strftime() と同じ書式が指定できる)
        #
        #     https://docs.python.jp/3/library/time.html#time.strftime
        #
        # デフォルトは now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3] と同じ形。
        # --------------------------------------------------------
        # ミリ秒をログに出力するやり方
        # --------------------
        # Pythonの日付書式は、他の言語と比べると少し変わっていて、ミリ秒のための書式が存在しない。
        # strftime() の書式では、 %f と指定すると「マイクロ秒」が出力される。
        # そのため、通常の sftftime() の場合は、%fを指定して、前３桁を有効とするようする。
        #
        # が、loggingで指定する datefmt で %f を指定すると実行時に例外が発生する。 (ValueError)
        # (datetime.datetime.now().sftftime('%H:%M:%S.%f') はエラーとならない・・・）
        #
        # では、どのようにしてミリ秒を表示するのかという話題になるが、以下のスレッドの情報がとても有用だった。
        #     https://stackoverflow.com/a/7517430/190597
        # %(msecs)d と指定するとミリ秒が出力できる。 この場合、format と datefmt の両方を指定する必要がある。
        # %(msecs)d は、 %(asctime)s とペアで使用する必要があるので、結局以下のように指定する。
        #
        #     %(asctime)s.%(msecs)03d --> 03d は、3桁表示でゼロ埋めせよという指示 (3 --> 003)
        #
        # 間の「.」は、出力時の秒とミリ秒の間に入る文字を表す。ここをカンマにすると 15:14:23,333 となる。
        #
        # Pythonドキュメントでは、以下のところに記載がある。
        #     https://docs.python.jp/3/library/logging.html#logrecord-attributes
        # --------------------------------------------------------
        fmt = '[%(asctime)s.%(msecs)03d] | %(message)s'
        datefmt = '%Y/%m/%d %H:%M:%S'  # ここで %f を指定すると実行時にフォーマットエラーになるので注意.
        logging.basicConfig(format=fmt, datefmt=datefmt, level=logging.INFO)

        logger = logging.getLogger(__name__)
        logger.warning('warning')

        # logging を終了
        logging.shutdown()


def go():
    """処理を実行します。"""
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
