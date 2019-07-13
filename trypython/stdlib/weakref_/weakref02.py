# coding: utf-8
"""
weakref モジュールについてのサンプルです。

弱参照がオブジェクトの __weakref__ に設定されることを確認するサンプルです。
"""
import weakref

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


# noinspection PyUnusedLocal,SpellCheckingInspection,PyUnresolvedReferences
class Sample(SampleBase):
    def exec(self):
        # ------------------------------------------------
        # 弱参照は、オブジェクトの
        #   __weakref__
        # に設定される。
        #
        # ただし、この属性が存在するのは
        #   ユーザ定義クラス　
        # の場合のみ。
        # ------------------------------------------------
        set01 = {1, 2}
        wref = weakref.ref(set01)
        pr('__weakref__ exists?', hasattr(set01, '__weakref__'))

        a = A()
        wref = weakref.ref(a)
        pr('__weakref__ exists?', hasattr(a, '__weakref__'))
        pr('a.__weakref__ is wref', a.__weakref__ is wref)

        # ------------------------------------------------
        # ユーザ定義クラスで弱参照をサポートするためには
        # __weakref__ 属性が必要となる。__slots__ 属性を
        # つかって、オブジェクトのメモリサイズを最適化している
        # 場合、この属性を含めていないと弱参照が作れない。
        # ------------------------------------------------
        b = NotContainsWeakrefAttr(100)
        try:
            bref = weakref.ref(b)
        except TypeError as e:
            pr('NotContainsWeakrefAttr', e)

        c = ContainsWeakrefAttr(100)
        cref = weakref.ref(c)
        print(cref)


class A:
    pass


class NotContainsWeakrefAttr:
    __slots__ = ('val',)

    def __init__(self, val):
        self.val = val


class ContainsWeakrefAttr:
    __slots__ = ('val', '__weakref__',)

    def __init__(self, val):
        self.val = val


def go():
    obj = Sample()
    obj.exec()
