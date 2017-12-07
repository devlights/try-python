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


class A:
    pass


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
