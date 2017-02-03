# coding: utf-8

"""
バイナリの変換についてのサンプルです。
"""

import binascii

from trypython.common.commoncls import *
from trypython.common.commonfunc import *


class Sample(SampleBase):
    def exec(self):
        #
        # 基準となる数値を生成
        #
        a_number = 1024
        pr('基準の数値', a_number)

        #
        # 数値からバイナリに
        # 数値を bytes にするには to_bytes メソッドを使う
        #
        binary1 = a_number.to_bytes(4, byteorder='big')
        pr('数値->バイナリ', binary1)

        #
        # バイナリから16進文字列へ
        # bytes から hex-str にするには hex メソッドを使う
        #
        hex_string = binary1.hex()
        pr('バイナリ->16進文字列', hex_string)

        # データを変更
        hex_string = hex_string[:4] + 'ffff'

        #
        # 16進文字列からバイナリへ
        # hex-str から bytes にするには binascii.unhexlify 関数を使う
        #
        binary2 = binascii.unhexlify(hex_string)
        pr('16進文字列->バイナリ', binary2)

        #
        # バイナリから数値へ
        # bytes から int にするには from_bytes メソッドを使う
        #
        a_number2 = int.from_bytes(binary2, byteorder='big')
        pr('バイナリ->数値', a_number2)


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
