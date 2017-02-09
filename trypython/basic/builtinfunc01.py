# coding: utf-8

"""
組み込み関数についてのサンプルです。
"""
from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        #
        # abs()
        # 絶対値を返す
        #
        int01 = -1024
        pr('abs()', abs(int01))

        #
        # all(iterable)
        # 指定した iterable の全要素が True の場合に True を返す
        #
        list01 = list(range(1, 10))  # 要素に 0 がいると False となる
        pr('all()', all(list01))

        #
        # any(iterable)
        # 指定した iterable のどれかの要素が True の場合に True を返す
        #
        pr('any()', any(list01))

        #
        # ascii()
        # 印字可能な文字列を返す。非asciiな文字はエスケープされる
        #
        str01 = 'こんにちわ世界'
        pr('ascii()', ascii(str01))

        #
        # bin()
        # 指定された整数を2進数文字列にして返す
        #
        int02 = 1024
        pr('bin()', bin(int02))

        #
        # bool()
        # 指定したオブジェクトを判定して bool値 を返す
        #
        pr('bool()', bool(int02))

        #
        # bytearray()
        # bytearrayオブジェクトを生成する
        # bytearrayは、ミュータブルなバイト配列を表す
        # (bytesはイミュータブル)
        #
        ba01 = bytearray(5)  # 初期容量が 5バイト のbytearray生成
        ba01[0] = 0xff
        pr('bytearray()', ba01)

        #
        # bytes()
        # bytesオブジェクトを生成する
        # 使い方は bytearray() と同様だが、bytesはイミュータブル
        #
        b01 = bytes([1, 11, 16])
        pr('bytes()', b01)

        try:
            b01[0] = b'10'
        except TypeError as e:
            pr('bytesはイミュータブル', e)

        #
        # callable()
        # 呼び出し可能オブジェクトかどうかを返す
        # クラスは呼び出し可能
        # インスタンスは __call__() を持っている場合は呼び出し可能
        #
        pr('callable()', callable(Sample))
        pr('callable()', callable(self))  # __call__を定義していないのでFalse


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
