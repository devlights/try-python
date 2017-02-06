# coding: utf-8

"""
クロージャのサンプルです。
"""
from typing import Callable

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        #
        # クロージャとは、他の関数によって動的に生成される関数
        # その関数の外で作られた変数の値を覚えていて、変更したりできるもの
        #
        closure1 = Sample.make_closure('hello world')
        closure2 = Sample.make_closure('this is message')

        pr('closure1', closure1())
        pr('closure2', closure2())

    @staticmethod
    def make_closure(message: str) -> Callable:
        """
        クロージャを生成します。

        :param message: メッセージ
        :return: クロージャ
        """
        def new_function():
            return message.upper()

        return new_function


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
