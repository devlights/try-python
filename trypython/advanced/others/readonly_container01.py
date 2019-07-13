"""
基本コンテナオブジェクトの読み取り専用モードオブジェクトについてのサンプルです。
"""
import types

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr, hr


class Sample(SampleBase):
    def exec(self):
        ###################################################################
        #
        # 基本コンテナオブジェクトと読み取り専用オブジェクト
        #
        # Python の基本コンテナとして
        #   * リスト (list)
        #   * ディクショナリ (dict)
        #   * セット (set)
        # が存在するが、それぞれ読み取り専用として扱えるオブジェクトが
        # 対で存在する。対応としては以下のようになる。
        #
        # リスト
        #    tuple に変更すると読み取り専用のリストとして使える
        # ディクショナリ
        #    types.MappingProxyType オブジェクトが読み取り専用として使える
        # セット
        #    frozenset が読み取り専用として使える
        #
        ##################################################################
        #
        # listとtuple
        #
        a_list = list(range(10))
        pr('list', a_list)

        a_list.append(100)
        a_list.insert(0, 101)
        del a_list[1]

        pr('list is mutable', a_list)

        a_tuple = tuple(a_list)
        pr('tuple', a_tuple)

        try:
            # noinspection PyUnresolvedReferences
            a_tuple.append(102)
        except AttributeError as attr_ex:
            pr('tuple is immutable', attr_ex)

        try:
            # noinspection PyUnresolvedReferences
            del a_tuple[0]
        except TypeError as type_ex:
            pr('tuple is immutable2', type_ex)

        # tupleは生成時に元データをコピーして生成されるので
        # 元のデータに変更があっても影響はない
        a_list.clear()
        a_list.append(999)
        pr('tuple', a_tuple)

        hr()

        #
        # dictとtypes.MappingProxyType
        #
        a_dict = dict(hello=1, world=2)
        pr('dict', a_dict)

        a_dict['spam'] = 100
        del a_dict['world']

        pr('dict is mutable', a_dict)

        a_proxy = types.MappingProxyType(a_dict)
        try:
            # noinspection PyUnresolvedReferences
            a_proxy['hello'] = 200
        except TypeError as type_ex:
            pr('MappingProxyType is immutable', type_ex)

        try:
            # noinspection PyUnresolvedReferences
            del a_proxy['hello']
        except TypeError as type_ex:
            pr('MappingProxyType is immutable2', type_ex)

        # MappingProxyTypeのみの特殊動作。
        # このオブジェクト自体が動的ビューなので
        # 元オブジェクトの変更は即座に反映される。
        # (tupleやfrozensetの場合は元の値がコピーされているため元データ
        #  変更しても影響はない。)
        a_dict['world'] = 999
        pr('proxy', a_proxy['world'])

        hr()

        #
        # setとfrozenset
        #
        a_set = set(a_tuple)
        pr('set', a_set)

        a_set.add(10)
        a_set.add(3)
        a_set.remove(2)

        pr('set is mutable', a_set)

        a_frozenset = frozenset(a_set)

        try:
            # noinspection PyUnresolvedReferences
            a_frozenset.add(4)
        except AttributeError as attr_ex:
            pr('frozenset is immutable', attr_ex)

        try:
            # noinspection PyUnresolvedReferences
            a_frozenset.remove(10)
        except AttributeError as attr_ex:
            pr('frozenset is immutable2', attr_ex)

        # frozensetは生成時に元データをコピーして生成されるので
        # 元のデータに変更があっても影響はない
        a_set.clear()
        a_set.add(999)
        pr('frozenset', a_frozenset)

        hr()


def go():
    obj = Sample()
    obj.exec()
