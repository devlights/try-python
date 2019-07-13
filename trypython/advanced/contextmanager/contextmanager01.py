# coding: utf-8

"""
PythonのContextManagerに関してのサンプルです。
"""
import contextlib as ctx

from trypython.common.commoncls import SampleBase, timetracer
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        with timetracer('contextmanager-sample'):
            #
            # クラス定義で ContextManager の動きをサポートする場合
            # dunderメソッドの __enter__() と __exit__() を実装する
            # py3.6から、contextlib.AbstractContextManagerクラスが追加された
            # ので、このクラスを基底クラスにして、オーバーライドするとラク
            #
            with HasCtxManager() as o:
                pr('inside-with', o)

            with HasCtxManager() as o:
                pr('inside-with', o)
                raise CtxTestException('this is test ex')

            #
            # 関数定義で、ContextManager の動きをサポートする場合
            # @contextlib.contextmanager デコレートを使用する
            # その上で、関数内で yield する必要がある
            #
            with return_none_ctx_manager() as o:
                pr('inside-with', o)

            with return_none_ctx_manager() as o:
                pr('inside-with', o)
                raise CtxTestException('this is test ex2')

            with return_obj_ctx_manager() as o:  # type: SayHelloWorld
                pr('inside-with', o)
                o.say()


class HasCtxManager(ctx.AbstractContextManager):
    def __enter__(self):
        pr('__enter__', 'called')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pr('__exit__.exc_type', exc_type)
        pr('__exit__.exc_value', exc_value)
        pr('__exit__.traceback', traceback)
        pr('__exit__', 'called')

        #
        # 本メソッドの戻り値にて True を返すと
        # 例外発生時にバブルアップしないように出来る
        # False を返すと、上の階層に例外がアップする
        #
        return True


class CtxTestException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class SayHelloWorld:
    def say(self):
        from datetime import datetime
        pr('say', 'hello world', datetime.now().isoformat())


@ctx.contextmanager
def return_none_ctx_manager():
    pr('yield', 'before')

    #
    # ここで yield だけにすると
    #  with xxxx() as o:
    # とした部分の o の値は None となる
    #
    try:
        yield
    except CtxTestException as e:
        pr('raise-exception', e)

    print('yield', 'after')


@ctx.contextmanager
def return_obj_ctx_manager():
    pr('yield', 'before')

    try:
        yield SayHelloWorld()
    except Exception as e:
        pr('raise-exception', e)

    pr('yield', 'after')


def go():
    obj = Sample()
    obj.exec()
