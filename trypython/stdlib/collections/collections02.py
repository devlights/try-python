# coding: utf-8

"""
collections.defaultdictについてのサンプルです。
"""
from collections import defaultdict

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        #
        # 辞書を普通に利用する場合、存在しないキーに
        # アクセスすると KeyError が発生する
        #
        dict01 = {}
        try:
            pr('key01', dict01['key01'])
        except KeyError as e:
            pr('KeyError', e)

        #
        # 辞書には、setdefault() が存在する
        # このメソッドは、指定されたキーが存在しない場合に
        # 第二引数の値を設定する。
        #
        try:
            pr('key01', dict01.setdefault('key01', 'hello'))
            pr('key01 in dict01', 'key01' in dict01)
        except KeyError as e:
            pr('KeyError', e)

        #
        # collectionsモジュールには defaultdict クラスが存在する
        # defaultdictクラスは、dict.setdefault() と動きは似ているが
        # 辞書作成時にあらゆる新キーのためにデフォルト値を設定する部分が
        # 異なる。利用する場合、引数にファクトリを指定する必要がある。
        # (つまり、引数は「関数」となる）
        #
        # キーが存在しない場合のデフォルト値を notexists となるように設定
        dict02 = defaultdict(lambda: 'notexists')
        pr('type(dict02)', type(dict02))

        # キーが存在しなくてもエラーにはならない
        pr('key01', dict02['key01'])
        pr('key01', 'key01' in dict02)

        # 当然、普通の辞書のように利用できる
        dict02['key02'] = 'hello world'
        pr('key02', dict02['key02'])

        #
        # デフォルト値が必ず設定されることを利用して
        # 簡単なカウンターを作成することも出来る。
        # 引数に渡している int は、int() の事。
        # つまり、デフォルト値は 0 となる。
        #
        dict03 = defaultdict(int)
        for char in iter('helloworld'):
            dict03[char] += 1
        pr('dict03', dict03)


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
