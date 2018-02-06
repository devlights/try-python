"""
reprlib についてのサンプルです。

link::
  https://docs.python.jp/3/library/reprlib.html
"""
import functools
import random
import reprlib
import string
from typing import Sequence, Callable

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class ManyFields:
    def __init__(self, field_names: Sequence[str], value_factory: Callable[[], int]):
        for name in field_names:
            self.__dict__[name] = value_factory()

    def __repr__(self) -> str:
        return ','.join(f'{k}={v}' for k, v in self.__dict__.items())


class Sample(SampleBase):
    def exec(self):
        # ------------------------------------------------
        # reprlib.repr()
        #
        # 通常のrepr()では、とても長い出力になってしまう場合に
        # 便利なメソッド。repr()は開発者用の出力を表示するので
        # どうしても長くなってしまう場合がある。
        # そのようなときに、reprlib.repr() を使うといい感じ。
        # ------------------------------------------------
        names = string.ascii_letters
        value_factory = functools.partial(random.Random().randint, 1, 100)

        many_fields = ManyFields(names, value_factory)

        pr('repr', repr(many_fields))
        pr('reprlib.repr', reprlib.repr(many_fields))


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
