"""
logging モジュールのサンプルです。
応用編 (logging.config.dictConfig() の使用)

REFERENCES::
https://docs.python.jp/3/library/logging.config.html#logging-config-dictschema
https://docs.sentry.io/clients/python/integrations/logging/
https://stackoverflow.com/questions/38323810/does-pythons-logging-config-dictconfig-apply-the-loggers-configuration-setti
"""
import json
import logging
import logging.config
import pathlib

from trypython.common.commoncls import SampleBase


class Sample(SampleBase):
    def exec(self):
        """サンプルの処理を実行します。"""
        # --------------------------------------------------------
        # logging.config.dictConfig() の使用
        # loggingでは、設定情報を外部に出して実行時に読み込む機能があります。
        #
        # logging.config.dictConfig() も
        # その一つで 辞書形式になっているデータを読み込み設定を行います。
        #
        # json形式をそのまま読み込めるので便利です。
        # 本サンプルでの設定内容に関しては
        # logging_config.json ファイルを参照ください。
        # --------------------------------------------------------
        config_file = pathlib.Path('logging_config.json')
        with config_file.open(mode='r', encoding='utf-8') as fd_conf:
            logging.config.dictConfig(json.load(fd_conf))

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
