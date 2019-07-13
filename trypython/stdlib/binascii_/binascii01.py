# coding: utf-8

"""
標準モジュール binascii についてのサンプルです。
"""

import binascii as ba

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        #
        # binascii モジュールは 文字列とバイナリを変換する
        #
        # 変換元の数値
        a_number = 1024
        pr('元の数値', a_number)

        #
        # 数値をバイナリに変換
        #
        binary1 = a_number.to_bytes(4, byteorder='big')
        pr('数値をバイナリに変換', binary1)

        #
        # バイナリを16進文字列に変換
        #
        hex_string = ba.hexlify(binary1)
        pr('バイナリを16進文字列に変換 (hexlify)', hex_string)

        #
        # 16進文字列をバイナリに変換
        #
        binary2 = ba.unhexlify(hex_string)
        pr('16進文字列をバイナリに変換 (unhexlify)', binary2)


def go():
    obj = Sample()
    obj.exec()
