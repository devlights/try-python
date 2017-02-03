#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
リストの基本サンプルです。
"""


class Sample:
    def exec(self):
        #
        # リスト初期生成
        #   空のリストを作成するには, []とするかlist()とする
        #   空のリストは、ifでFalse扱いとなる
        #
        # 空リスト生成
        list1 = []
        print(list1)

        if not list1:
            print('False')

        # 空リスト生成
        list1 = list()
        print(list1)

        if not list1:
            print('False')

        # 値を指定して初期化
        list1 = [1, 2, 3, 4, 5]
        print(list1)

        #
        # 要素の追加
        #
        list1.append(10)
        print(list1)

        #
        # 要素の削除
        #
        list1.remove(10)
        print(list1)

        #
        # クリア
        #
        list1.clear()
        print(list1)

        #
        # 他のリストからの更新
        #
        list2 = list(range(10))
        list1.extend(list2)
        print(list1)

        # +=を利用しても同じ
        list1.clear()
        list1 += list2
        print(list1)

def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
