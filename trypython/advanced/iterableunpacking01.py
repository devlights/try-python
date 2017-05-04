# coding: utf-8
"""
PEP-3132 Extended Iterable Unpacking のサンプルです。

PEP 3132
  https://www.python.org/dev/peps/pep-3132/
"""
from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        # -----------------------------------------------
        # PEP 3132 Extended Iterable Unpacking は
        # Python 3.0 から追加された機能。
        #
        # 「*」を付けた変数に残りの値がアンパックされる
        # -----------------------------------------------
        # 以下のように iterable を右辺において
        # 左辺に複数の変数で受ける記述は昔からあったが
        # そこに、「*」を付与した変数を置くと
        # ここでアンパックされる。また、後ろに
        # アンパックではない通常の変数を置いても
        # 適切に解釈して値を設定してくれる。
        # -----------------------------------------------
        str01 = 'hello world'
        first, *rest, last = str01

        pr('first', first)
        pr('rest', rest)
        pr('last', last)

        # なので、シーケンスの先頭とそれ以外を分ける場合に
        seq01 = list(range(10))
        first, rest = seq01[0], seq01[1:]

        pr('first', first)
        pr('rest', rest)

        # とする必要がなく、以下のように書ける
        first, *rest = seq01

        pr('first', first)
        pr('rest', rest)

        # 同じことが for ステートメントでも適用できて以下のように書ける
        it01 = [tuple('hello'), tuple('world')]
        for _, *x, _ in it01:
            print(x)

        # 一つしか要素がない iterable の場合もちゃんと動く
        oneitem = [1]
        first, *rest = oneitem

        pr('first', first)
        pr('rest', rest)

        # さすがに要素がゼロの場合はエラーになる
        try:
            noitem = []
            first, *rest = noitem

            pr('first', first)
            pr('rest', rest)
        except ValueError as e:
            pr('noitem', e)


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
