# coding: utf-8
"""
collections.namedtupleについてのサンプルです。
namedtupleの基本的な使い方については、collections04.py を参照。
"""
import collections as cols

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        MyVal01 = cols.namedtuple('MyVal01', ['name', 'value'])
        obj1 = MyVal01('hello world', 'value01')

        pr('obj', obj1)

        # namedtuple は、__dict__ を持たない
        try:
            pr('__dict__', obj1.__dict__)
        except AttributeError as e:
            pr('__dict__', e)

        # namedtuple は、__slots__ に 空タプルが設定される
        pr('__slots__', obj1.__slots__)

        # ------------------------------------------------------------
        # namedtuple は、通常のtupleと同様に利用できる。
        # さらに、以下の3つのメソッドを持つ。
        #   ・_make
        #   ・_asdict
        #   ・_replace
        # ------------------------------------------------------------

        # ------------------------------------------------------------
        # _make メソッド
        # --------------------
        # 既存のsequence, iterable から新しいオブジェクトを構築する。
        # csvやデータベースなどの行からオブジェクトを作成するのに便利。
        # ------------------------------------------------------------
        rows = (['hello', 'value01'], ['world', 'value02'])
        for item in (MyVal01._make(row) for row in rows):
            pr('item', item)

        # ------------------------------------------------------------
        # _asdict メソッド
        # --------------------
        # フィールド名と値のOrderedDictを返す。
        # 戻り値が OrderedDict なので、フィールドの並び順の通りに取得できる。
        # (*) OrderedDictになったのは、python 3.1 から。
        # ------------------------------------------------------------
        obj_dict = obj1._asdict()
        pr('obj_dict', obj_dict)

        # 辞書から namedtuple を構築する場合は **kwargs 形式で渡す
        obj2 = MyVal01(**obj_dict)
        pr('obj2', obj2)
        pr('eq', obj1 == obj2)

        # ------------------------------------------------------------
        # _replace メソッド
        # --------------------
        # 指定したフィールドの値を置き換えた、新しい namedtuple を返す。
        # namedtuple は、immutableなので、常に新しいオブジェクトを返す。
        # ------------------------------------------------------------
        obj3 = obj2._replace(name='world hello', value='value03')
        pr('obj3', obj3)
        pr('eq', obj3 == obj2)

        # ------------------------------------------------------------
        # namedtuple に、独自のメソッドを持たせる場合は
        # namedtuple を親クラスにしたクラスを新たに定義する。
        # ------------------------------------------------------------
        class MyVal02(cols.namedtuple('MyVal02', ['name'])):
            __slots__ = ()

            @property
            def upper_name(self):
                return self.name.upper()

        obj4 = MyVal02('hello world 2')
        pr('obj4.name', obj4.name)
        pr('obj4.upper_name', obj4.upper_name)


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
