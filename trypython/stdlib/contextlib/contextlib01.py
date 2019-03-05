# coding: utf-8
"""
contextlib.suppress のサンプルです。
"""
import contextlib as ctx
import os
from typing import Generator

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
        except FileNotFoundError as e:
            print(e)

        ######################################
        # contextlib.suppress は
        # 指定した例外が発生しても暗黙で飲み込んで
        # くれるコンテキストマネージャを返す
        # 上と同じ処理を suppress を使うと以下の
        # ようになる。例外情報は複数指定できる。
        ######################################
        with ctx.suppress(FileNotFoundError):
            with log('存在しないファイルを削除'):
                os.remove(target_file)


@ctx.contextmanager
def log(message: str) -> Generator:
    """指定したメッセージ付きで開始と終了のログを出力するコンテキストマネージャを返します。

    >>> with log('hello'):
    ...     print('world')
    START: hello
    world
    END: hello

    :type message: str
    :param message: メッセージ
    :rtype: typing.Generator
    :return: コンテキストマネージャ
    """
    print(f'START: {message}')
    try:
        yield
    finally:
        print(f'END: {message}')


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
