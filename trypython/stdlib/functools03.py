# coding: utf-8
"""
functoolsモジュールについて
singledispatch関数についてのサンプルです.
"""
import functools
import html
import numbers

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


# ---------------------------------------------
# singledispatch化したい関数に対して
# @functools.singledispatch デコレータを適用する
# 同じ呼び出しで呼び先を分岐させたい関数に対して
# @関数名.register(型) を付与すると登録される。
# ---------------------------------------------
@functools.singledispatch
def htmlescape(obj):
    content = html.escape(repr(obj))
    return f'<pre>{content}</pre>'


@htmlescape.register(str)
def _(text):
    return f'<p>{text}</p>'


@htmlescape.register(numbers.Integral)
def _(n):
    return f'<pre>0x{n}</pre>'


class Sample(SampleBase):
    def exec(self):
        pr('singledispatch(obj)', htmlescape((1, 2, 3)))
        pr('singledispatch(str)', htmlescape('hello world'))
        pr('singledispatch(int)', htmlescape(100))


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
