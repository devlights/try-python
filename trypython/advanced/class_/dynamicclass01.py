"""
type() を利用して動的にクラスを生成するサンプルです.

REFERENCES:: http://bit.ly/2HSBbSG
             http://bit.ly/2HUeeP3
             http://bit.ly/2HWSYb8
             http://bit.ly/2I7IJBh
             http://bit.ly/2HSPZkd
"""
import numbers

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    # noinspection PyPep8Naming,PyUnresolvedReferences
    def exec(self):
        # -------------------------------------------------
        # Python では、「全てがオブジェクト」である。
        # この「全て」には、クラスも含まれる。
        # クラスは type のインスタンスである。
        # つまり、通常行っているクラス定義は type インスタンスを
        # 作成することと同じ。
        #
        # クラスインスタンスが属しているクラスは
        # Class.__class__ で取得することが出来る
        #
        # 組み込み関数 type() は、 __class__ を呼び出している
        # (Pythonのドキュメントには 組み込み関数と記載されているが
        #  実際にはtypeはクラスである。)
        # -------------------------------------------------
        class MyClass1:
            pass

        pr('type(MyClass1)', type(MyClass1))  # => <class 'type'>

        # type() に type を渡すと type となる
        # つまり、type は type クラス自身に属している
        pr('type(type)', type(type))  # => <class 'type'>

        # typeクラスは引数が一つのものと三つのものが存在する
        # 一つのものが通常利用しているもの。三つのものを利用すると
        # 新しい型オブジェクトを作成することが出来る。
        # つまり、クラス定義をしているのと同じことになる。
        # noinspection PyUnusedLocal,PyTypeChecker
        def func1(s, val):
            if isinstance(val, numbers.Number):
                return val + 1
            return 0

        clsname = 'DynClass1'
        baseclasses = (object,)
        classdict = dict(method1=func1)

        # 動的にクラス定義し、インスタンスを生成
        DynClass1 = type(clsname, baseclasses, classdict)
        d1 = DynClass1()
        pr('d1.method1(10)', d1.method1(10))  # => 11

        # 追記：
        # type() を利用する他に types モジュールを利用する方法もある
        # types モジュールは「動的な型生成と組み込み型に対する名前」と
        # タイトルが付いているので、そのまま動的型生成に利用できる
        # 動的に型生成する場合は、 types.new_class() を利用する
        import types

        # types.new_class() に渡す引数の exec_body にはちょっと注意が必要。
        # この引数は「新規で作成されたクラスの名前空間を構築するためのコールバック」となっている
        # つまり、引数に 名前空間（イコール dict) を受け取り、更新した名前空間を返すようにする必要がある
        # 基本的には lambda ns: ns.update(classdict) のようになる。
        def update_ns(ns: dict):
            ns.update(classdict)

        clsname = 'DynClass2'
        DynClass2 = types.new_class(clsname, baseclasses, exec_body=update_ns)
        d2 = DynClass2()
        pr('d2.method1(11)', d2.method1(11))  # => 12

        # types.new_class() で メタクラスを指定する場合は kwds 引数に指定する
        class DynMeta(type):
            _count: int = 0

            def __call__(cls, *args, **kwargs):
                cls._count += 1
                return super().__call__(*args, **kwargs)

            @property
            def creation_count(cls):
                return cls._count

        clsname = 'DynClass3'
        kwds = dict(metaclass=DynMeta)
        DynClass3 = types.new_class(clsname, baseclasses, kwds=kwds, exec_body=update_ns)

        # 10 回 生成を繰り返してみる
        instances = [DynClass3() for _ in range(10)]
        pr('DynClass3.creation_count', DynClass3.creation_count)  # => 10

        # 10 回 メソッドを呼び出してみる
        _ = [instance.method1(index) for index, instance in enumerate(instances)]
        pr('DynClass3.creation_count', DynClass3.creation_count)  # => 10


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
