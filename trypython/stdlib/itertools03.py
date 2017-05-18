# coding: utf-8
"""
itertools モジュールについてのサンプル

以下の処理についてのサンプルです。

- repeat()
"""
import itertools

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        # -----------------------------------------------
        # itertools.repeat() は、指定したオブジェクトを
        # 指定した回数分繰り返すイテレータを生成してくれる。
        # 繰り返し回数は、第二引数の times で指定できる。
        # timesのデフォルトは None となっており、これは
        # 無限の繰り返しを表す。
        # -----------------------------------------------
        str01 = 'hello python'
        for x in itertools.repeat(str01, 2):
            pr('itertools-repeat', x)

        list01 = list(range(5))
        for i, x in enumerate(itertools.repeat(list01)):
            # そのままだと、無限ループするので10回出力で止める
            if i >= 10:
                break
            pr('itertools-repeat times=None', i, x)


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
