#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
print関数のサンプルです.
"""
from trypython.common.commoncls import *


class Sample(SampleBase):
    def exec(self) -> None:
        import tempfile

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
        tmp_file_path = tempfile.mktemp()
        with open(tmp_file_path, "wt") as writer:
            print(message, message2, file=writer)
        with open(tmp_file_path, "r") as reader:
            print(reader.read())


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()