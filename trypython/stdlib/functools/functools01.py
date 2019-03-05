# coding: utf-8

"""
functools.partial()を利用した「関数の部分適用」についてのサンプルです。
"""
import functools

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        #
        # 通常の関数呼び出し
        #
        func01('hello world', 'func01')

        #
        # functools.partial() にて第二引数を予め適用した状態
        #
        func02('hello world')

        #
        # functools.partial() で生成した部分適用関数は
        # __name__をもっていない。
        #
        pr('func01.__name__', func01.__name__)

        try:
            pr('func02.__name__', func02.__name__)
        except AttributeError as attrEx:
            pr('func02.__name__', attrEx)

        #
        # functools.update_wrapper() をかぶせると
        # 元の関数からの情報を引き継ぐ
        #
        func03 = functools.update_wrapper(func02, func01)
        pr('func03.__name__', func03.__name__)
        func03('hello world from func03')


def func01(message: str, prefix: str) -> None:
    pr('func01', f'{prefix}--{message}')


#
# 関数の部分適用
# 予め定義されている func01 に対して prefix が設定済みの
# 新しい定義を生成する
#
func02 = functools.partial(func01, prefix='partial')


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
