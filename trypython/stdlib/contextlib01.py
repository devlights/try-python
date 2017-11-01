# coding: utf-8
"""
contextlib.suppress のサンプルです。
"""
import contextlib as ctx
import os

from trypython.common.commoncls import SampleBase


class Sample(SampleBase):
    def exec(self):
        ######################################
        # 通常ファイル削除などを行う場合
        # 例外が発生する可能性があるので
        # 以下のようにチェック処理もしくは
        # 例外補足が必要となるが、例外が
        # 発生しても無視して進むときもある。
        ######################################
        target_file = 'non_exists_file'

        try:
            # 処理前にクリーニング目的で
            # やったりする場合、この処理では
            # 例外でても無視するときもある
            os.remove(target_file)
        except FileNotFoundError:
            pass

        ######################################
        # contextlib.suppress は
        # 指定した例外が発生しても暗黙で飲み込んで
        # くれるコンテキストマネージャを返す
        # 上と同じ処理を suppress を使うと以下の
        # ようになる。例外情報は複数指定できる。
        ######################################
        with ctx.suppress(FileNotFoundError):
            os.remove(target_file)
