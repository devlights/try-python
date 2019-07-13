"""
list の コピー（クローン） についてのサンプルです.

python における リスト に対しての 浅いコピー と 深いコピー のやり方について

REFERENCES:: http://bit.ly/2OgPdAf
"""
import copy

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr, hr


class Data:
    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return str(self.val)


class Sample(SampleBase):
    def exec(self):
        # ----------------------------------------------------------------
        # リストを コピー or クローン する場合、以下の選択肢がある
        #
        # (1) list.copy() を使う (Python 3.3 から追加)
        # (2) [:] のスライス
        # (3) list() を使う
        # (4) copy.copy() を使う
        # (5) copy.deepcopy() を使う
        #
        # ただし、 (5) 以外は、 「浅いコピー (shallow copy)」 となる.
        # 速度面からみると、当然 (5) が一番時間がかかる.
        # ----------------------------------------------------------------
        a = Data(100)
        b = Data(200)

        original = [1, 'hello world', a, b]
        pr('orig', original)
        hr()

        # (1)
        no_1 = original.copy()
        # (2)
        no_2 = original[:]
        # (3)
        no_3 = list(original)
        # (4)
        no_4 = copy.copy(original)
        # (5)
        no_5 = copy.deepcopy(original)

        # 元の値を変更
        original[0] = 999
        original[1] = original[1].upper()
        a.val = 111
        b.val = 222

        pr('orig', original)
        hr()

        # 結果出力
        pr('No.1', no_1)
        pr('No.2', no_2)
        pr('No.3', no_3)
        pr('No.4', no_4)
        pr('No.5', no_5)


def go():
    obj = Sample()
    obj.exec()
