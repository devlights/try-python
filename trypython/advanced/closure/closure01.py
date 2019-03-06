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

        closure3 = Sample.make_closure_with_param('hello world')
        pr('closure3', closure3('closure parameter'))

    @staticmethod
    def make_closure_with_param(message: str) -> Callable[[str], str]:
        """
        引数を一つ受け取るクロージャを生成します。

        :param message: メッセージ
        :return: クロージャ
        """

        def new_function(option_message: str):
            return f'{message} with {option_message}'

        return new_function

    @staticmethod
    def make_closure(message: str) -> Callable[[], str]:
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
