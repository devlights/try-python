"""
組み込み関数 len() のサンプルです.

文字列の場合とバイト列の場合の結果の違いについて

REFERECESS:: http://bit.ly/2VkK8xI
             http://bit.ly/2VgS9DL
             http://bit.ly/2Vl8V4I
"""
from collections.abc import Sized

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class NotSupportedLen:
    pass


class SupportedLen:
    def __len__(self):
        return 100


class InheritSized(Sized):
    def __init__(self, num: int) -> None:
        super().__init__()
        self._num = num

    def __len__(self) -> int:
        return self._num


class Sample(SampleBase):
    def exec(self):
        str_en = 'hello'
        str_ja = 'はろー'
        bytes_en = str_en.encode('ascii')
        bytes_ja = str_ja.encode('utf-8')
        bytes_ja2 = str_ja.encode('sjis')

        # len() の 挙動
        # len() は 指定されたオブジェクトの長さ（要素の数）を返す。
        # 実際には、そのオブジェクトの __len__ が呼び出されている。
        # なので、 __len__ をサポートしていない場合はエラーとなる。
        #
        # 対象が str の場合は「文字数」が返る。(str.__len__)
        # 対象が bytes の場合は「バイト数」が返る。(bytes.__len__)
        pr('len(str_en)', len(str_en))  # 文字数なので 5 文字
        pr('len(str_ja)', len(str_ja))  # 文字数なので 3 文字
        pr('len(bytes_en)', len(bytes_en))  # ascii なので 5 バイト
        pr('len(bytes_ja)', len(bytes_ja))  # utf-8 なので 9 バイト
        pr('len(bytes_ja2)', len(bytes_ja2))  # sjis  なので 6 バイト

        # __len__ を実装していないオブジェクトを指定すると当然エラーとなる
        # その場合、TypeError が 発生する
        try:
            # noinspection PyTypeChecker
            pr('len(not_support)', len(NotSupportedLen()))
        except TypeError as e:
            pr('len(not_support)', e)

        # __len__ を実装している場合、それが呼び出される
        supported_len = SupportedLen()
        pr('len(support)', len(supported_len))
        pr('issubclass(support)', issubclass(type(supported_len), Sized))
        pr('isinstance(support)', isinstance(supported_len, Sized))

        # __len__ をそのまま実装するより collections.abc の基底クラスから
        # 継承しておくほうが個人的には好み。
        inherit_sized = InheritSized(10)
        pr('len(inherit)', len(inherit_sized))
        pr('issubclass(inherit)', issubclass(type(inherit_sized), Sized))
        pr('isinstance(inherit)', isinstance(inherit_sized, Sized))


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
