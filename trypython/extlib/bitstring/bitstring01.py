# coding: utf-8

"""
bitstringモジュールに関するサンプルです。
BitArrayについて(1)。
"""
import bitstring as bs

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        # ---------------------------------------------------------------
        # [link]
        # http://pythonhosted.org/bitstring/walkthrough.html
        # ---------------------------------------------------------------
        # BitArray は、バイナリデータを保持するコンテナ
        # BitStream は、ポジションや読み込みの操作を行うことが出来るストリーム
        # ---------------------------------------------------------------
        # BitArray は、mutable
        # インスタンスから2進数や16進数など様々な形で取り出せる
        # ---------------------------------------------------------------
        # hex は、ビットが4の倍数でないとエラーとなる
        # oct は、ビットが3の倍数でないとエラーとなる
        # ---------------------------------------------------------------
        # 初期化の方法はいろいろある
        #   BitArray(bin='0b11111111')
        #   BitArray(hex='0xff')
        #   BitArray(uint=255, length=8)
        # 上記はどれも同じデータをつくる
        # ---------------------------------------------------------------
        ba01 = bs.BitArray('0xff01')

        pr('ba01', ba01)
        pr('ba01.bin', ba01.bin)
        pr('ba01.hex', ba01.hex)
        pr('ba01.int', ba01.int)
        pr('ba01.uint', ba01.uint)
        pr('ba01.bytes', ba01.bytes)

        try:
            # 8進数はビットが3の倍数分存在しないと駄目
            pr('ba01.oct', ba01.oct)
        except bs.InterpretError as e:
            pr('ba01.oct', e)

        ba02 = ba01 + '0b00'
        pr('ba02.oct', ba02.oct)

        ba03 = bs.BitArray(bin='0b11111111')
        pr('ba03', ba03)
        pr('ba03.uint', ba03.uint)

        ba04 = bs.BitArray(hex='0xff')
        pr('ba04', ba04)
        pr('ba04.uint', ba04.uint)

        ba05 = bs.BitArray(uint=255, length=8)
        pr('ba05', ba05)
        pr('ba05.uint', ba05.uint)


def go():
    obj = Sample()
    obj.exec()
