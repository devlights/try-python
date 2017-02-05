#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
リストの基本サンプルです。
"""

from trypython.common.commoncls import *
from trypython.common.commonfunc import *


class Sample(SampleBase):
    def exec(self):
        #
        # リスト初期生成
        #   空のリストを作成するには, []とするかlist()とする
        #   空のリストは、ifでFalse扱いとなる
        #
        # 空リスト生成
        list1 = []
        pr('[]で生成', list1)

        if not list1:
            pr('[]のif判定', 'False')

        # 空リスト生成
        list1 = list()
        pr('list()で生成', list1)

        if not list1:
            pr('list()のif判定', 'False')

        # 値を指定して初期化
        list1 = [1, 2, 3, 4, 5]
        pr('値を指定して初期化', list1)

        #
        # 要素の追加
        #
        list1.append(10)
        pr('appendで要素の追加', list1)

        #
        # 要素の挿入
        #
        list1.insert(0, -1)
        pr('insertで要素の挿入', list1)

        # insertの場合、インデックスが要素数を超えていても例外は出ず、末尾に追加される。
        list1.insert(99, -100)
        pr('insertで範囲外のインデックス指定', list1)

        #
        # 要素の削除
        #
        # 特定のインデックスを削除する場合は del 文
        del list1[-1]
        pr('del文で要素の削除', list1)

        # リスト内の該当する値を削除するには remove メソッド
        list1.remove(10)
        pr('removeメソッドで値の削除', list1)

        #
        # クリア
        #
        list1.clear()
        pr('要素のクリア', list1)

        #
        # 他のリストからの更新
        #
        list2 = list(range(10))
        list1.extend(list2)
        pr('extendで他のリストの要素を取込む', list1)

        # +=を利用しても同じ
        list1.clear()
        list1 += list2
        pr('+=で他のリストを指定', list1)

        #
        # list()にデータを渡してリスト生成
        # 指定できるデータは iterable なものとなる
        #
        original_data1 = 'helloworld'
        list3 = list(original_data1)
        pr('list()にデータを指定してリスト生成', list3)

        # not iterableなデータを渡すと例外 (TypeError)
        try:
            list(100)
        except TypeError as e:
            pr('list()に not iterableを指定', e)


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
