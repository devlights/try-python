# coding: utf-8

"""
関数についてのサンプルです。
"""
from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        # ------------------------------------------------------------
        # オプション引数
        # ------------------------------------------------------------
        self.func_with_default_val()

        # ------------------------------------------------------------
        # *による位置引数のタプル化
        # ------------------------------------------------------------
        self.func_with_args_tuples(1, 2, 'hello', 'world')

        # ------------------------------------------------------------
        # **によるキーワード引数の辞書化
        # ------------------------------------------------------------
        self.func_with_kwargs_dict(name='hello', name2='world')

        # ------------------------------------------------------------
        # 全部入り
        # ------------------------------------------------------------
        self.func_allin('helloworld', 1, 2, 'こんにちわ世界', value1=100, value2='string value')

        # ------------------------------------------------------------
        # 関数内関数
        # ------------------------------------------------------------
        def inner_func(x, y):
            return x + y

        pr('inner-func', inner_func(10, 20))
        pr('inner-func', inner_func(50, 50))

        # ------------------------------------------------------------
        # ラムダ(匿名関数)
        # ------------------------------------------------------------
        lambda01 = lambda x, y: x + y
        pr('lambda', lambda01(10, 20))
        pr('lambda', lambda01(50, 50))

    def func_with_default_val(self, message=''):
        pr('func_with_default_val', message)

    def func_with_args_tuples(self, *args):
        pr('func_with_args_tuples', args)

    def func_with_kwargs_dict(self, **kwargs):
        pr('func_with_kwargs_dict', kwargs)

    def func_allin(self, message='', *args, **kwargs):
        pr('func_allin', (message, args, kwargs,))


def go():
    obj = Sample()
    obj.exec()
