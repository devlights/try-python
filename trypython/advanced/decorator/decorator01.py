# coding: utf-8

"""
デコレータについてのサンプルです。
"""
import functools

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


def log_it(func):
    """
    デコレータ関数

    :param func: 元の関数
    :return: デコレータ関数
    """

    def decorator_function(*args, **kwargs):
        pr('decorator', func.__name__, 'func-name')
        pr('decorator', args, '*args')
        pr('decorator', kwargs, '**kwargs')

        result = func(*args, **kwargs)
        pr('decorator', result, 'result')
        pr('----------------------------------', '')

        return result

    return decorator_function


def sum_it(func):
    """
    デコレータ関数

    :param func: 元の関数
    :return: デコレータ関数
    """

    def decorator_function(*args, **kwargs):
        func_result = func(*args, **kwargs)

        result = sum(range(1, func_result + 1))
        pr('sum_it', result)

        return result

    return decorator_function


def upper(func):
    # functools.wraps() を利用するとオリジナル関数のメタデータが上書きされない
    @functools.wraps(func)
    def decorator_function(*args, **kwargs):
        result: str = func(*args, **kwargs)
        return result.upper()

    return decorator_function


class Sample(SampleBase):
    def exec(self):
        #
        # デコレータは、入力として関数を取り
        # 別の関数を返す関数のこと
        #
        # 元の関数をラップして、付加操作を追加する
        #

        #
        # そのまま利用
        #
        decorator_function = log_it(self.test_func)
        decorator_function(1, 2)

        #
        # 元の関数に @log_it を付与した版
        #
        self.test_func2(name='test value')

        #
        # @log_it を付与せずに
        # 関数をデコレータ関数で上書きした版
        #
        self.test_func3()

        #
        # @xxxxx を複数付与することも可能
        # 関数に最も近いデコレータから先に実行される
        #
        self.test_func4(1, 9)

        #
        # functools.wrap()を利用した版
        #
        pr('test_func5', self.test_func5('hello decorator'))

        #
        # 関数の名前がどのようになるか
        #
        pr('test_func.__name__', self.test_func.__name__)
        pr('test_func2.__name__', self.test_func2.__name__)
        pr('test_func3.__name__', self.test_func3.__name__)
        pr('test_func4.__name__', self.test_func4.__name__)
        pr('test_func5.__name__', self.test_func5.__name__)

    def test_func(self, x, y):
        pr('test-func', f'hello world {x} {y}')

    @log_it
    def test_func2(self, **kwargs):
        pr('test-func2', f'hello world {kwargs}')

    def test_func3(self):
        pr('test-func3', 'test-func3')

    test_func3 = log_it(test_func3)

    @sum_it
    @log_it
    def test_func4(self, *args):
        return sum(args)

    # 以下と同じことになる
    # test_func4 = sum_it(log_it(test_func4))

    @upper
    def test_func5(self, message: str):
        return message


def go():
    obj = Sample()
    obj.exec()
