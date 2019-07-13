# coding: utf-8

"""
__slots__についてのサンプルです。
"""

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        #
        # Pythonでは、デフォルトでインスタンス属性のための辞書を持っており
        # __dict__で参照できる。この中に属性が全て記録されている。
        # __dict__はただの辞書なので、実行時に追加することも削除することも可能。
        #
        # __slots__を利用すると、__dict__が生成されなくなり
        # 属性の追加を制限出来る。予め属性が決まっているクラス定義の
        # 場合に有効な手段。
        #

        #
        # 通常のクラスの場合
        # 好きなタイミングで属性を追加したり出来る
        #
        without_slots = WithoutSlots()
        pr('without_slots.__dict__', without_slots.__dict__)
        pr('without_slots.x', without_slots.x)
        without_slots.z = 100
        pr('without_slots.z', without_slots.z)
        pr('without_slots.__dict__', without_slots.__dict__)

        #
        # クラス定義時に__slots__を追加している場合
        # __slots__に定義していない属性を追加しようとしたり
        # すると例外が発生する。また、__slots__が定義されている場合
        # __dict__が生成されないので、アクセスすると例外が発生する。
        #
        with_slots = WithSlots()
        pr('with_slots.x', without_slots.x)

        try:
            with_slots.z = 100
        except AttributeError as e:
            pr('with_slots.z', e)

        try:
            pr('with_slots.__dict__', with_slots.__dict__)
        except AttributeError as e:
            pr('with_slots.__dict__', e)


class WithoutSlots:
    """通常のクラス定義"""

    def __init__(self):
        super().__init__()
        self.x = 10
        self.y = 20


class WithSlots:
    """__slots__を追加したクラス定義"""

    __slots__ = ['x', 'y']

    def __init__(self):
        super().__init__()
        self.x = 10
        self.y = 20


def go():
    obj = Sample()
    obj.exec()
