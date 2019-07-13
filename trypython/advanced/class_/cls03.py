"""
Python のクラスについてのサンプルです。

サブクラス側で __init__ を定義した場合の注意点について。
"""
from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr, hr


class B:
    """
    ベースクラス
    """

    def __init__(self) -> None:
        self.x = 10


class C(B):
    """
    サブクラス１

    自分の __init__ を定義していないバージョン
    """
    pass


class D(B):
    """
    サブクラス２

    自分の __init__ を定義しているが
    super().__init__() を呼んでいないバージョン
    """

    # noinspection PyMissingConstructor
    def __init__(self):
        self.y = 20


class E(B):
    """
    サブクラス３

    自分の __init__ を定義していて
    super().__init__() も呼んでいるバージョン
    """

    def __init__(self):
        super().__init__()
        self.y = 20


class Sample(SampleBase):
    """
    サンプルとなるクラスです。
    """

    def exec(self):
        """
        処理を実行します。
        """
        # ------------------------------------------------------------
        # (1) サブクラス側が __init__ を定義していない場合
        #     既定で、 super().__init__() が呼ばれた状態となる
        # ------------------------------------------------------------
        obj1 = C()
        pr('C.x', obj1.x)

        hr()

        # ------------------------------------------------------------
        # (2) サブクラス側が __init__ を定義しているが super().__init__() を
        #     呼んでいない場合、親クラスの __init__ は呼ばれない。
        #
        # 他の言語に慣れている場合、デフォルトのコンストラクタが呼ばれるのが暗黙的なので
        # よく間違えてしまう。注意が必要。
        #
        # PyCharmで作業している場合、IDE側が警告を出してくれるので気付ける。
        # ------------------------------------------------------------
        try:
            obj2 = D()
            pr('D.x', obj2.x)
            pr('D.y', obj2.y)
        except AttributeError as e:
            pr('D', e)

        hr()

        # ------------------------------------------------------------
        # (3) サブクラス側が __init__ を定義していて super().__init__() を
        #     呼んでいる場合、親クラスの __init__ も呼ばれる。
        # ------------------------------------------------------------
        obj3 = E()
        pr('E.x', obj3.x)
        pr('E.y', obj3.y)


def go() -> None:
    """
    サンプルを実行します。
    """
    obj = Sample()
    obj.exec()
