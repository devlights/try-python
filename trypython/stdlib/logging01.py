"""
logging モジュールのサンプルです。
最も基本的な使い方について (ログレベルの変更）
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
        # logging モジュールで定義されている ログレベル は、以下の５つ。
        #
        #   DEBUG
        #   INFO
        #   WARNING
        #   ERROR
        #   CRITICAL
        #
        # 下にいくほど、ログレベルが高い。
        # デフォルトのログレベルは、 WARNING となっている。 なので、何の設定もしないまま logging　モジュールを使うと
        # WARNING 以上のログレベルのみ出力が行われる。 出力先は、デフォルトでは 標準エラー に出力される。
        # --------------------------------------------------------
        # logging モジュールを利用する際に最も簡単に設定が行えるやり方は
        #
        #     logging.basicConfig()
        #
        # を利用することである。この関数は、多くのキーワード引数を備えており、指定することで logging モジュールの全体設定が
        # 行えるようになっている。
        #
        #     https://docs.python.jp/3/library/logging.html#logging.basicConfig
        #
        # --------------------------------------------------------
        # 今回は最も簡単なところの、ログレベルの調整から。
        # WARNING がデフォルトレベルなので、変更する
        logging.basicConfig(level=logging.INFO)
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
        logging.shutdown()

        # [結果]
        # --------------------------------------
        # INFO: __main__:info
        # WARNING: __main__:warn
        # ERROR: __main__:error
        # CRITICAL: __main__:critical


def go():
    """処理を実行します。"""
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
