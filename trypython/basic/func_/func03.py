"""
関数についてのサンプルです

Inner Function について
"""
import typing

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        # ---------------------------------------------------------
        # inner function について
        # -------------------------------
        # Python では、関数の中で関数を定義することが出来る.
        # Python では、関数は first class object なので
        # 関数内部で定義した関数を戻り値として返すことももちろん可能.
        # 一般的に内部関数を使うのは、decorator や closure を使うときが多い.
        # ---------------------------------------------------------
        f = self.get_helloworld_func('hello world', 0.7)
        pr('f', f)
        pr('f("hello world", 0.7)', f())

        f = self.get_helloworld_func('hello world', 0.1)
        pr('f', f)
        pr('f("hello world", 0.1)', f())

    # noinspection PyMethodMayBeStatic
    def get_helloworld_func(self, text: str, volume: float) -> typing.Callable[[], str]:
        def whisper():
            """小文字にして返します"""
            return f'{text.lower()}...'

        def yell():
            """大文字にして返します"""
            return f'{text.upper()}!!!'

        if volume > 0.5:
            return yell
        else:
            return whisper


def go():
    obj = Sample()
    obj.exec()
