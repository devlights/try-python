# coding: utf-8

"""
collections.OrderedDictについてのサンプルです。
"""
import collections

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        #
        # collections.OrderedDictは、キーが最初に追加された順序を
        # 記憶する辞書。新しい項目が既存の項目を上書きしても、元の挿入位置は変わらない。
        # 項目を削除して再設定すると末尾に移動する
        #
        dict01 = collections.OrderedDict()
        dict01['first'] = 100
        dict01['second'] = 200
        dict01['third'] = 300

        # 挿入順序を保っている
        pr('dict01', dict01)

        # 値を変更しても位置は変わらない
        dict01['second'] = 999
        pr('dict01', dict01)

        # 削除して再設定すると末尾に追加
        del dict01['second']
        pr('dict01', dict01)

        dict01['second'] = 888
        pr('dict01', dict01)
        pr('dict01', [(key, val) for key, val in dict01.items()])

        #
        # reversed() をサポート (3.5から追加)
        #
        pr('reversed()', tuple(reversed(dict01)))

        #
        # 元の辞書が存在する場合
        # コンストラクタに指定することで、新規のOrderedDictを作成できる
        # 予め sorted() してから設定することで、初期位置を設定できる
        #
        # キーの末尾の数値でソートしたものを初期データとする
        normal_dict = {'word03': 'from python', 'word01': 'hello', 'word02': 'world'}
        sorted01 = sorted(normal_dict.items(), key=lambda x: x[0][-1])
        dict02 = collections.OrderedDict(sorted01)

        pr('sorted01', sorted01)
        pr('dict02', dict02)


def go():
    obj = Sample()
    obj.exec()
