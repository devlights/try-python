#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
リストの基本サンプルです。
"""

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


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

        #
        # pop() を利用して要素の取り出し
        # pythonのListはキューやスタックとしても利用可能
        #   (1) appendしてpop(-1)すると、スタック
        #   (2) appendしてpop(0)すると、キュー
        #
        list4 = list(range(10))
        pr('pop()呼び出し前', list4)
        pr('指定なしでpop()呼び出し', list4.pop())  # 引数なしはインデックスに -1 を指定した事になる
        pr('pop()呼び出し後', list4)
        pr('インデックス指定でpop()呼び出し', list4.pop(2))
        pr('pop()呼び出し後', list4)

        # スタック的な使い方 (LIFO)
        a_stack = list(range(2))
        a_stack.append(5)
        pr('要素の追加 (append)(Stack)', a_stack)
        pr('要素の取得 (pop)(Stack)', a_stack.pop())

        # キュー的な使い方 (FIFO)
        a_queue = list(range(2))
        a_queue.append(5)
        pr('要素の追加 (append)(Queue)', a_queue)
        pr('要素の取得 (pop)(Queue)', a_queue.pop(0))

        #
        # リストのスライス
        # [start:end:step]で指定できる
        # 負のインデックスは末尾からのインデックスとなる
        #   ex) -1は最終要素, -2は最終要素の一つ前
        # 通常のインデックス指定の場合は、要素数よりも大きい数を
        # 指定すると例外が発生するが、スライスの場合は発生しない。
        # stepを指定すると、指定した数分飛ばして要素取得する。
        # stepに負の値を指定すると、最終要素からとなる。
        # stepに -1 を指定すると、リストを reverse することになる
        #
        list5 = list(range(10))
        pr('最初から5番目まで取得', list5[:5])  # startを指定しない場合は 0 を指定した事になる
        pr('最初から5番目まで２つずつ取得', list5[:5:2])
        pr('3番目から末尾まで取得', list5[2:])  # endを指定しない場合は 末尾まで を指定した事になる
        pr('逆順で取得(reverse)', list5[::-1])
        pr('逆順で２つずつ取得', list5[::-2])
        pr('末尾の2番めから正順の2番目まで３つずつ取得', list5[-2:1:-3])

        #
        # 要素のインデックスを取得
        #
        list6 = [1, 100, 99, 3, 6]
        pr('値が 99 のインデックス', list6.index(99))

        #
        # 指定した値が存在するか
        #
        list7 = list(range(20))
        pr('値が 11 はリスト内に存在するか', 11 in list7)
        pr('値が 99 はリスト内に存在するか', 99 in list7)

        #
        # ソート
        # ソートには2種類のやり方がある
        #   sort() -- リストの内容を直接ソートする破壊的メソッド
        #   sorted() -- ソートした内容を返す組み込み関数
        # どちらの場合も、デフォルトは昇順ソート。降順にする場合はオプション引数で指定する。
        #
        list8 = list(range(10))[::-1]
        pr('ソートする前', list8)

        list8.sort()
        pr('ソート後 (sort())(asc)', list8)

        list8 = list8[::-1]
        sorted_list = sorted(list8)
        pr('ソート後 (sorted())(asc)', sorted_list)
        pr('sorted()の場合は、元リストは変更無し', list8)

        #
        # 要素数の取得
        #
        list9 = list(range(10000))
        pr('要素数の取得', len(list9))

        #
        # リストのコピー
        # リストのコピーにはいくつかやり方がある
        #   スライスを利用
        #   copy()を利用
        #
        list10 = list(range(10))
        copy_slice = list10[:]
        copy_method = list10.copy()

        # リストの値を変更
        list10[5] = 999
        copy_slice[5] = 998
        copy_method[5] = 997

        # 確認
        pr('元リスト (リストのコピー)', list10)
        pr('スライスコピー (リストのコピー)', copy_slice)
        pr('copy()コピー (リストのコピー)', copy_method)


def go():
    obj = Sample()
    obj.exec()
