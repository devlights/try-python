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
        #
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


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
