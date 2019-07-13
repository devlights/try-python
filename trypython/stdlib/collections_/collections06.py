# coding: utf-8

"""
collections.ChainMapについてのサンプルです。
"""
import collections

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        #
        # collections.ChainMap は、複数の dict() をまとめて
        # 一つの辞書のように扱うようにするクラス。
        #
        # dict() の持つ全ての機能を持つ。
        # キーを指定した探索は内部で持つ複数の dict() に対して実施される
        # 対して、書込みや更新、削除は、最初に指定した dict() に対してのみ実施される。
        #
        map01 = dict(apple=100, pineapple=200)
        map02 = dict(hello='world', world='hello')
        map03 = collections.ChainMap(map01, map02)

        pr('ChainMap', map03)
        pr('ChainMap[apple]', map03['apple'])
        pr('ChainMap[world]', map03['world'])

        map03['new_key'] = 999
        pr('ChainMap[new_key]', map03)

        map03['world'] = 'new value'
        pr('ChainMap[world]', map03)

        del map03['world']
        pr('del ChainMap[world]', map03)


def go():
    obj = Sample()
    obj.exec()
