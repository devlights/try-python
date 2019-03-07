"""
ディクショナリについてのサンプルです。

dict の マージ について (Python 3.5 以降で有効)
"""
from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        # ------------------------------------------------------------
        # ディクショナリのマージ
        #
        # python 3.5 以降であれば以下のようにして
        # 2つのディクショナリをマージできる。(いくつでも可能)
        # ------------------------------------------------------------
        dict_a = {'a': 1, 'b': 2}
        dict_b = {'c': 3, 'd': 4}

        merged = {**dict_a, **dict_b}
        pr('merged', merged)

        dict_c = {'f': 5, 'g': 6}
        pr('merged2', {**merged, **dict_c})

        # 同じ要素がある場合、後の要素で上書きされる
        dict_d = {'a': 10, 'd': 40}
        pr('merge3', {**merged, **dict_d})


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
