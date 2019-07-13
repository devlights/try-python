"""
リストのサンプルです.

リストの flatten について

REFERENCES:: http://bit.ly/2L7yfq1
             http://bit.ly/2Li2N8S
"""
import itertools

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        # リストの要素が tuple になってるデータを生成
        nested = [(chr(x), chr(x + 1)) for x in range(65, 70)]
        pr('nested', nested)

        # itertools.chain を使って flatten
        flattened = list(itertools.chain.from_iterable(nested))
        pr('flatten', flattened)

        # ついでに、並び順をキープしたままで重複削除 (python 3.7 以降で有効)
        dup_deleted = list(dict.fromkeys(flattened))
        pr('dup_deleted', dup_deleted)


def go():
    obj = Sample()
    obj.exec()
