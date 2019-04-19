#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
print関数のサンプルです.
"""
import tempfile

from trypython.common.commoncls import *


class Sample(SampleBase):
    def exec(self) -> None:
        ##################################
        # print関数
        # python3からprintが関数になったため
        # カッコの付与が必須となっている。
        message = 'first value'
        print(message)

        ##################################
        # 複数の値を指定することができる
        # デフォルトは空白でつながる
        message2 = 'second value'
        print(message, message2)

        ##################################
        # 区切り文字を指定
        print(message, message2, sep=',')

        ##################################
        # 出力先はデフォルトで標準出力
        # 変更可能
        # -------------------------------------------------------------------
        # mktemp 関数を利用していると CodeFactor で以下の警告を指摘された。
        #
        # Use of insecure and deprecated function (mktemp).
        # Use of this function may introduce a security hole in your program.
        # By the time you get around to doing anything with the file name it returns,
        # someone else may have beaten you to the punch. Use mkstemp()
        # instead or replace with NamedTemporaryFile(), passing it the delete=False parameter.
        #
        # mktemp 関数はセキュアな関数ではないので代わりに mkstemp 関数を利用せよとのこと。
        # -------------------------------------------------------------------
        _, tmp_file_path = tempfile.mkstemp()
        with open(tmp_file_path, "wt") as writer:
            print(message, message2, file=writer)
        with open(tmp_file_path, "r") as reader:
            print(reader.read())


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
