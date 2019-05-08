"""
組み込み関数 round() のサンプルです.

python3 から round の丸め方について変更されているので、そのサンプルです。

REFERENCERS:: http://bit.ly/2H4CBZT
              http://bit.ly/2H69SUB
              http://bit.ly/2H4CE81
              http://bit.ly/2GZBz12
"""
from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        # --------------------------------------------------------------------
        # 組み込み関数 round() は、Python3 にて丸め方が変更となっている.
        # Python3 からは
        #   「最近接偶数への丸め」
        #      - round half to even
        #      - round ties to even
        # に変わった。
        #
        # これは、丸め対象の値が tie つまり、ど真ん中の場合に
        # 最も近い偶数の方に丸めるという方式。
        #
        # なので、round(2.5) は、tie であるので、最近接偶数 が適用されて 2 となる。
        # --------------------------------------------------------------------
        pr('round(0.5)', round(0.5))  # 最近接偶数 は 0
        pr('round(1.5)', round(1.5))  # 最近接偶数 は 2
        pr('round(2.5)', round(2.5))  # 最近接偶数 は 2
        pr('round(3.5)', round(3.5))  # 最近接偶数 は 4
        pr('round(1.3)', round(1.3))  # ど真ん中 (tie) ではないので、通常の丸めで 1
        pr('round(1.7)', round(1.7))  # ど真ん中 (tie) ではないので、通常の丸めで 2


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
