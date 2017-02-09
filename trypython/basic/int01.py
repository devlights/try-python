# coding: utf-8

"""
int についてのサンプルです。
"""
from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        #
        # Python2 では int と long が別れていたが
        # Python3 では long が無くなり int は任意のサイズを表現できる
        #
        googol = 10 ** 100
        pr('googol', googol)

        #
        # 0b or 0B から始まる値は ２進数
        # 0o or 0O から始まる値は ８進数
        # 0x or 0X から始まる値は １６進数
        #
        base_2 = 0b1011
        pr('0bから始まる', base_2)

        base_8 = 0o13
        pr('0oから始まる', base_8)

        base_16 = 0xb
        pr('0xから始まる', base_16)

        #
        # 値が使用しているビット数
        # 正確には、符号と先頭の 0 は除いて二進法で表すために必要なビットの数
        #
        i01 = 1024
        pr('1024のビット数', i01.bit_length())
        pr('googolのビット数', googol.bit_length())

        #
        # bytes に変換
        #
        b01 = i01.to_bytes(2, byteorder='big')
        pr('bytes に変換', b01)

        #
        # bytes から変換
        #
        i02 = int.from_bytes(b01, byteorder='big')
        pr('bytes から変換', i02)

        #
        # Python 3.6 から 数値リテラルを _ で区切ることが可能になった
        # 単純に見た目だけの話。２進数を表現する際などに便利。
        #
        i02 = 1000_0000_0000
        pr('数値リテラルを_で区切る', i02)

        i03 = 0b0011_1110_1000
        pr('数値リテラルを_で区切る', i03)


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
