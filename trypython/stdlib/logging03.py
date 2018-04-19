"""
logging モジュールのサンプルです。
最も基本的な使い方について (フォーマッタの指定)
"""
import logging

from trypython.common.commoncls import SampleBase


class Sample(SampleBase):
    def exec(self):
        """サンプル処理を実行します。"""
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
        # format キーワードを指定して、出力文字列のフォーマットを変更する。
        # format 文字列内にて指定できるキーワードについては、以下を参照。
        #
        #     https://docs.python.jp/3/library/logging.html#logrecord-attributes
        #
        # 追加で指定できる属性値については、以下を参照。
        #
        #     https://docs.python.jp/3/library/string.html#formatstrings
        #
        # つまり、左寄せで8文字表示にするには以下のように指定する。
        #
        #     %(levelname)-8s
        #
        # 逆に、右寄せで8文字表示にするには以下のように指定する。
        #
        #     %(levelname)8s
        #
        # --------------------------------------------------------
        fmt = '[%(asctime)s][%(levelname)-8s] %(name)s %(filename)s:%(funcName)s:%(lineno)d | %(message)s'
        logging.basicConfig(level=logging.WARNING, format=fmt)
        logger = logging.getLogger(__name__)

        # それぞれのログレベルで出力
        logger.debug('debug')
        logger.info('info')
        logger.warning('warn')
        logger.error('error')
        logger.critical('critical')

        # logging を終了
        logging.shutdown()


def go():
    """処理を実行します。"""
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
