# coding: utf-8
"""
itertools モジュールについてのサンプル

以下の処理についてのサンプルです。

- starmap()
"""
import itertools as it
import operator as ope

from common.commoncls import SampleBase
from common.commonfunc import pr, hr


class Sample(SampleBase):
    def exec(self):
        # -----------------------------------------------
        # itertools.starmap()
        # ----------------------
        # グループ化済みの iterable に対して function を適用する。
        # 例えば、zipした後の結果に対して、更に function 適用するなど。
        #
        # 正直使ったことがない
        # -----------------------------------------------
        hr('it.starmap()')

        list01 = [9, 8, 7]
        list02 = [1, 2, 3]
        list03 = list(zip(list01, list02))

        starmap = it.starmap(ope.sub, list03)
        pr('it.starmap', list(starmap))

        list04 = list(zip(list01, list02, *list03))
        pr('it.starmap', list(it.starmap(lambda *args: sum(args), list04)))

        # -----------------------------------------------
        # itertools.takewhile()
        # ----------------------
        # 指定した条件を満たす間、要素を返す。
        # dropwhile() の 逆。
        #
        # なので、一度でも条件から外れた場合、それ以降に
        # 条件を満たす値があっても要素は返らない。
        # -----------------------------------------------
        hr('it.takewhile()')

        list05 = sorted(it.chain(list01, list02))
        pr('list05', list05)

        takewhile = it.takewhile(lambda x: x < 5, list05)
        pr('it.takewhile', list(takewhile))

        # -----------------------------------------------
        # itertools.tee()
        # ----------------------
        # 指定された iterable を複数の独立した iterable にして返す。
        # つまり、n=2 とすると、元の iterable を複製した
        # 二つの iterable が取得できる。(tuple(iterable, iterable))
        #
        # 公式ドキュメントに記載されているように、一度 tee() を
        # 使用して分割した original iterable は、内部状態を共有しているので
        # もう別の場所では利用しないほうがいい。
        #
        # 引用：
        # Once tee() has made a split,
        # the original iterable should not be used anywhere else;
        # otherwise, the iterable could get advanced
        # without the tee objects being informed.
        # -----------------------------------------------
        hr('it.tee()')

        list06 = list('helloworld')

        it_tee = it.tee(list06, 2)
        it_asc, it_desc = it_tee[0], reversed(list(it_tee[-1]))
        for it01, it02 in zip(it_asc, it_desc):
            pr('it.tee', f'{it01}, {it02}')


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
