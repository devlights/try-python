# coding: utf-8

"""
collections.namedtupleのサンプルです。
"""
import collections

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        #
        # namedtupleは、「名前つきタプル」を作成する
        # 通常のタプルに、型名と名前つきのフィールドを付与出来るイメージ。
        # 通常のタプルと同様に、イミュータブルであることは同じ。
        # 値は、コンストラクト時に指定する。
        #
        # フィールド名は、カンマ区切りの文字列で渡すか
        # シーケンスを指定する
        #
        Person = collections.namedtuple('Person', 'name,age')
        p = Person(name='test', age=30)
        pr('Person', p)

        try:
            p.name = 'test2'
        except AttributeError as e:
            pr('namedtupleはイミュータブル', e)

        #
        # フィールド名にはシーケンスを指定することも出来る
        #
        field_names = ('name', 'age')
        Person2 = collections.namedtuple('Person2', field_names=field_names)
        p2 = Person2(name='test2', age=30)
        pr('Person2', p2)

        #
        # 存在しないフィールド名を指定するとエラー
        #
        try:
            p3 = Person2(name='test3', age=33, hoge=10)
        except TypeError as e:
            pr('存在しないフィールド名を指定', e)

        #
        # verbose引数にTrueを指定するとクラス宣言を標準出力に出してくれる
        #
        collections.namedtuple('Person3', 'name', verbose=True)


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
