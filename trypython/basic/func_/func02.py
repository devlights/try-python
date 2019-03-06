# coding: utf-8

"""
関数についてのサンプルです。
"""
from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import hr, pr


class Sample(SampleBase):
    def exec(self):
        # -----------------------------------------
        # 最も基本的な関数の形
        # -----------------------------------------
        func = Sample.normal_func
        hr(func.__name__)
        pr(func.__name__, func(10, 20))

        # -----------------------------------------
        # 可変引数あり
        # 可変引数は、慣習的に *args と記述する
        # -----------------------------------------
        func = Sample.with_args
        hr(func.__name__)
        pr(func.__name__, func(10, 20, 30, 40, 50))

        # -----------------------------------------
        # デフォルト値あり
        # -----------------------------------------
        func = Sample.with_default_value
        hr(func.__name__)
        pr(func.__name__, func(10, 20))

        # -----------------------------------------
        # キーワード引数あり
        # キーワード引数は、慣習的に **kwargs と記述する
        # -----------------------------------------
        func = Sample.with_kwargs
        hr(func.__name__)
        pr(func.__name__, func(10, 20, z=100, zz=200))

        # -----------------------------------------
        # 特殊な アスタリクスのみ引数 を持つ関数
        # -----------------------------------
        # 引数リストの中に「*」のみの引数を定義すると
        # それ以降の引数について強制的にキーワード指定
        # をして呼び出すように出来る。
        #
        # 通常 func(x, y, z=100) のように定義して
        # いると、 func(10, 20, z=111) のように
        # 呼ぶことも出来るし、 func(10, 20, 111) と
        # 呼ぶことも出来る。
        #
        # だが、func(x, y, *, z=100) と定義した場合
        # func(10, 20, 111)と呼ぶとエラーとなり
        # func(10, 20) か func(10, 20, z=111) と
        # いうようにキーワード引数を明示的に指定しないと
        # 受け付けないように出来る。
        # -----------------------------------------
        func = Sample.with_asterisk_sentinel
        hr(func.__name__ + '(sentinel)')
        pr(func.__name__, func(10, 20))
        pr(func.__name__, func(10, 20, z=500))

        try:
            pr(func.__name__, func(10, 20, 300))
        except TypeError as err:
            pr('with_asterisk_sentinel', err)

    @staticmethod
    def normal_func(x, y):
        return x + y

    @staticmethod
    def with_args(x, y, *args):
        return sum((x, y, *args))

    @staticmethod
    def with_default_value(x, y, z=100):
        return x + y + z

    @staticmethod
    def with_kwargs(x, y, **kwargs):
        return sum((x, y, *(kwargs.values())))

    @staticmethod
    def with_asterisk_sentinel(x, y, *, z=100, zz=200):
        return x + y + z + zz


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
