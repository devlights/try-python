# coding: utf-8

"""
組み込み関数についてのサンプルです。
"""
from collections import namedtuple

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
            # noinspection PyUnresolvedReferences
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

        #
        # chr()
        # 指定された値が示すコードポイントに対応する文字を返す
        #
        # 兄弟として、ord() がある。こっちは文字を与えて整数を返す
        pr('chr()', chr(98))

        #
        # divmod()
        # 商と余りを同時に返す
        #
        pr('divmod()', divmod(9, 5))

        #
        # enumerate()
        # 指定された iterable の要素と ループカウント を返す
        #
        list02 = list(range(3))
        for i, x in enumerate(list02):
            pr('enumerate()', (i, x))

        # 以下でも同じ事になる
        pr('enumerate() -- 2', list(enumerate(range(3))))

        #
        # filter()
        # 指定された iterable に対して filter-function を適用する
        #
        list03 = list(range(10))
        for x in filter(lambda _: _ % 2 == 0, list03):
            pr('filter()', x)

        # 以下でも同じ事になる
        pr('filter()', (*filter(lambda _: _ % 2 == 0, list03),))

        #
        # getattr()
        # 指定されたオブジェクトの属性値を取得する
        #
        # 兄弟として、setattr(), delattr(), hasattr() がある
        #
        TestData = namedtuple('TestData', 'name')
        data = TestData(name='hello world')

        pr('getattr()', getattr(data, 'name'))

        #
        # hex()
        # 指定された数値の16進数文字列を返す
        #
        # 兄弟として、bin(), oct() がある
        #
        pr('hex()', hex(255))

        #
        # hash()
        # オブジェクトのハッシュ値を返す
        # __hash__をオーバーライドして変更することが可能
        #
        # listをこの関数に渡すと例外が出るので注意
        # unhashable type: 'list'
        #
        # つまり、ミュータブルなものをこの関数に渡すと例外となる
        tuple01 = tuple(list03)
        pr('hash()', hash(tuple01))

        #
        # id()
        # オブジェクトの識別子を返す
        # ハッシュ値と異なることに注意
        # CPythonの場合はメモリアドレス
        #
        pr('id()', id(tuple01))

        #
        # iter()
        # 指定されたシーケンスをイテレータにする
        # 第二引数を使ったやり方もあるが、よくわからん。。。
        #
        list04 = [1, 2, 3]
        it01 = iter(list04)

        try:
            pr('iter() -- __next__()', next(it01))
            pr('iter() -- __next__()', next(it01))
            pr('iter() -- __next__()', next(it01))
            pr('iter() -- __next__()', next(it01))
        except StopIteration as e:
            pr('iter() -- StopIteration', e)

        #
        # len()
        # オブジェクトの長さを返す
        #
        pr('len()', len('hello'))
        pr('len()', len(list04))
        pr('len()', len(tuple01))

        #
        # map()
        # iterable の各要素に map-function を適用する
        #
        for x in map(lambda _: _ ** 2, list04):
            pr('map()', x)

        #
        # max()
        # iterable の中で最大の要素を返す
        #
        # 兄弟として、min() がある
        pr('max()', max(list04))
        pr('min()', min(list04))

        #
        # reversed()
        # シーケンスを逆順にしたものを返す
        #
        # 兄弟として sorted() がある
        pr('reversed()', (*reversed(list04),))

        #
        # sum()
        # 合計を返す
        #
        pr('sum()', sum(list04))

        #
        # zip()
        # 指定されたN個の iterable から要素を一つずつ取得した
        # イテレータを構築して返す。
        #
        # 注意点として、zip() は、要素数が最も少ないものに合わせる
        # 要素数が最も多いものに合わせるには itertools.zip_longest()
        # を利用する
        #
        list05 = reversed(range(5))
        for x, y in zip(list04, list05):
            pr('zip()', (x, y))


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
