# coding: utf-8
"""
itertools モジュールについてのサンプル

以下の処理についてのサンプルです。

- groupby()
"""
import collections
import itertools as it

from common.commoncls import SampleBase
from common.commonfunc import pr, hr


class Sample(SampleBase):
    def exec(self):
        # -----------------------------------------------
        # itertools.groupby()
        # ----------------------
        # 指定された条件でグルーピングを行う。
        # groupby() は、key で指定した関数が返す値が
        # 変わる度に新たなグループを生成するため
        # 通常指定するシーケンスはソート済みである必要がある。
        #
        # また、groupby() が返すデータはそれ自身もイテレータ
        # となっているため、データが後の処理で必要な場合は
        # 別途リストなどを用意して保持しておく必要がある。
        # (それか、再度 groupby() 呼ぶ)
        # -----------------------------------------------
        GroupingData = collections.namedtuple('GroupingData', ['id', 'name'])

        # 未ソートのシーケンス
        groups_not_sorted = [
            GroupingData(1, 'data1'),
            GroupingData(1, 'data2'),
            GroupingData(2, 'data3'),
            GroupingData(1, 'data4')
        ]

        def key_func(grp: GroupingData) -> int:
            return grp.id

        hr('未ソートの状態で groupby() ')

        grp_iter = it.groupby(groups_not_sorted, key=key_func)
        for k, g in grp_iter:
            pr('grp-key', k)
            pr('\tgrp-items', ','.join(_.name for _ in g))

        hr('ソート済みの状態で groupby() ')

        # ソート済み
        groups_sorted = sorted(groups_not_sorted, key=key_func)

        grp_iter = it.groupby(groups_sorted, key=key_func)
        for k, g in grp_iter:
            pr('grp-key', k)
            pr('\tgrp-items', ','.join(_.name for _ in g))


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
