"""
logging モジュールのサンプルです。
応用編 (Sentry と logging の連携)

Sentry の Python ライブラリは raven という名前のモジュールです。
インストールは、conda からでも pip からでも行なえます。以下は conda の例。

$ conda install raven -y

参考情報::
https://docs.sentry.io/
https://docs.sentry.io/clients/python/
"""
import logging

from raven import Client
from raven.conf import setup_logging
from raven.handlers.logging import SentryHandler

from trypython.common.commoncls import SampleBase


class Sample(SampleBase):
    def exec(self):
        """サンプルの処理を実行します。"""
        # --------------------------------------------------------
        # Sentry と logging の組み合わせのサンプル
        # Sentry DSN は 環境変数 SENTRY_DSN に設定してから起動します。
        #
        # ログレベルがDEBUGやINFOのものもSentryに送信するには
        # 以下のように logging 側の level と
        # SentryHandler 側の level を調整します。
        #
        # (*) Windowsの場合、一時設定するには以下のようにします。
        #
        #     $ set SENTRY_DSN=xxxxx
        #
        # (*) bashの場合、一時設定するには以下のようにします。
        #
        #     $ export SENTRY_DSN=xxxxx
        #
        # (*) PyCharmの場合、実行時構成の画面にて環境変数の設定ができます。
        #
        # https://www.jetbrains.com/help/pycharm/run-debug-configuration-python.html
        #
        # 参考情報::
        #  https://docs.python.jp/3/library/logging.config.html#logging-config-dictschema
        #  https://docs.sentry.io/clients/python/integrations/logging/
        #
        # 以下で、Sentryとの連携を行っています。
        # loggingモジュールとSentryのライブラリ (raven) の連携自体は
        #
        #     setup_logging()
        #
        # を呼び出すだけで完了します。
        #
        # その際、 SentryHanler() の設定時に
        # どのログレベルで Sentry に送るかを決めておきます。
        #
        # （以下の例では、ログレベルがERROR以上の場合のみSentryに連携しています。
        #   それよりも低いログレベルの場合は通常のログ出力が行われます。)
        #
        # --------------------------------------------------------
        fmt = '[%(asctime)s][%(levelname)-8s] %(name)s %(filename)s:%(funcName)s:%(lineno)d | %(message)s'
        logging.basicConfig(level=logging.INFO, format=fmt)

        # 引数に何も指定しない場合、環境変数[SENTRY_DSN]から読み取られる
        client = Client()
        handler = SentryHandler(client, level=logging.ERROR)
        setup_logging(handler)

        logger = logging.getLogger(__name__)

        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warning message')
        try:
            1 / 0
        except ZeroDivisionError:
            logger.error('error message', exc_info=True)


def go():
    """処理を実行します。"""
    obj = Sample()
    obj.exec()
