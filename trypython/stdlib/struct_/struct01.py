"""
structモジュールのサンプルです。

- pack と unpack の使い方について
"""

import struct

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import hr


class Sample(SampleBase):
    def exec(self):
        #############################################
        # struct.pack メソッドについて
        #
        # struct.pack メソッドは指定されたフォーマットに従って
        # データをバイト列に変換してくれる。
        #
        # 指定できる書式については以下を参照。
        #   https://bit.ly/2OQucjz
        #
        # 代表的なものは以下の通り。 (https://bit.ly/2AsLaeO)
        #    < : リトルエンディアン
        #    > : ビッグエンディアン
        #    x : パディング
        #    b : char
        #    h : short
        #    i : int
        #    l : long
        #    d : double
        #    s : char[]
        #
        # どの項目も繰り返し回数を指定することができる。
        # 例えば、 int が３つの場合は「3I」と指定できる。
        #
        # たいていの項目は、大文字が unsigned を表す。
        #
        # s フォーマットの場合のみ、繰り返し回数の指定は
        # バイト長として判断される。
        #
        #
        # -------------------------------------------
        # struct.unpack メソッドについて
        #
        # struct.unpack メソッドは pack メソッドの逆を行う。
        #############################################
        hr('fmt=3I values=(2, 1, 408)')
        fmt = '3I'
        vals = (2, 1, 408)

        b = struct.pack(fmt, *vals)
        print(b)

        hr('strcut.unpack')
        print(struct.unpack(fmt, b))


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
