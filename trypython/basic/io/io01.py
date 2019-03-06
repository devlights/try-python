# coding: utf-8

"""
IO関連のサンプルです。
"""
import os
import tempfile
from typing import TextIO

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        #
        # ファイルIO
        # ファイルは open() などで開いて ファイルオブジェクトを
        # 取得するところから始まる。取得したファイルオブジェクト
        # に対して write() や read() を行い、最後に close() で閉じる
        # (mode に何を指定しているのかで 読み込み可能、書き込み可能が異なる)
        #

        #
        # 最もオーソドックスな形
        #
        fp = self.get_file_obj()
        try:
            fp.write('hello world')

            fp.seek(os.SEEK_SET)
            data = fp.read()

            pr('io.read()', data)
        finally:
            fp.close()

        #
        # with による自動クローズ
        # Pythonはオープンファイルなどをクリーンアップするために
        # コンテキストマネージャという仕組みを持っている。
        #
        # 形式は以下となる
        #   with expression as variable:
        #
        # 以下の場合、ブロックを抜けたタイミングでファイルを閉じる
        # (C# などの using と同じ)
        with self.get_file_obj() as fp2:
            fp2.write('こんにちわ世界')
            fp2.seek(os.SEEK_SET)
            pr('io.read() with contextmanager', fp2.read())

    # noinspection PyMethodMayBeStatic
    def get_file_obj(self) -> TextIO:
        # mode に指定している w+t の意味は
        #   w: 書き込み用にファイルを開いてファイルを切り詰める
        #   +: ファイルを更新用に開く (読み書きOK）
        #   t: テキストモード
        return tempfile.TemporaryFile(mode='w+t', encoding='utf-8')


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
