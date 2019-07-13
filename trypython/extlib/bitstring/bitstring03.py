# coding: utf-8

"""
bitstringモジュールに関するサンプルです。

BitArray.find()

について
"""
import bitstring as bs

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr, hr


class Sample(SampleBase):
    def exec(self):
        # ----------------------------------------------
        # BitArray には、指定したビット列を検索
        # メソッドが存在する。
        #
        # 以下の３種類がある。
        #   - find
        #   - findall
        #   - rfind
        #
        # find メソッドの結果は、1要素の tuple となる。
        # findall メソッドは、generator となる。
        # rfind メソッドの結果は、1要素の tuple となる。
        # ----------------------------------------------
        hr()
        ba01 = bs.BitArray('0x8F')
        pr('ba01.bin', ba01.bin)
        pr('ba01.uint', ba01.uint)

        hr('find 0xF')
        pos, = ba01.find('0xF')
        ba02 = ba01[pos:]
        pr('ba01.find', pos)
        pr('ba02.bin', ba02.bin)
        pr('ba02.uint', ba02.uint)

        hr('find 0b01')
        pos, = ba01.find('0b01')
        ba03 = ba01[pos:]
        pr('ba01.find', pos)
        pr('ba03.bin', ba03.bin)
        pr('ba03.uint', ba03.uint)

        hr('find 0b1111')
        pos, = ba01.find('0b1111')
        ba04 = ba01[pos:]
        pr('ba01.find', pos)
        pr('ba04.bin', ba04.bin)
        pr('ba04.uint', ba04.uint)

        hr('findall 0b1')
        gen_pos = ba01.findall('0b1')
        positions = list(gen_pos)
        pr('ba01.findall', type(gen_pos))
        pr('ba01.positions', positions)
        pr('ba01.bit_values', [ba01[x] for x in positions])


def go():
    obj = Sample()
    obj.exec()
