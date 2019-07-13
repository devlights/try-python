"""
文字列型についてサンプルです。

文字列のインデックスとスライスに関して
"""
from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        # --------------------------------------------
        # 文字列のインデックスに関しては以下のように捉える
        #
        # apple という文字列があるとして
        #
        #     |a|p|p|l|e|
        #      0 1 2 3 4
        #
        # という感じ。
        #
        # 文字列のスライスに関しては以下のように捉える
        #
        # apple という文字列があるとして
        #
        #     |a|p|p|l|e|
        #     0 1 2 3 4 5
        #
        # という感じ。文字の境界部分にオフセットがあるイメージ。
        # なので、[0:2] と指定するとその間にある文字をスライス
        # するので、ap となる。
        #
        # どちらの場合も負のインデックスは右から割り振られている
        # と捉える。
        # --------------------------------------------
        s = 'apple'
        pr('index', s[3])
        pr('slice', s[0:3])
        pr('index(negative)', s[-2])
        pr('slice(negative)', s[-5:-2])
        pr('slice', s[-3:])
        pr('slice', s[:-3])


def go():
    obj = Sample()
    obj.exec()
