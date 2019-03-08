"""
* と ** のアンパック演算子についてのサンプルです

PEP484 の動作について

REFERENCES:: http://bit.ly/2VMowpQ
"""
from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


# noinspection PyMethodMayBeStatic
class Sample(SampleBase):
    def exec(self):
        # -----------------------------------------------------------------------
        # PEP 448 「* イテラブルアンパック演算子と ** 辞書アンパック演算子の利用方法拡張」
        #
        # 1. 関数呼び出しにて任意の数のアンパックが利用可能になった
        # 2. タプル、リスト、集合、辞書表現でも複数のアンパックが利用可能になった
        # -----------------------------------------------------------------------

        # 1
        self.pep448_01(*[1, 2], *[5], 3, *[9, 10])
        self.pep448_02(**{'a': 100, 'b': 200}, c=300, **{'d': 400})
        self.pep448_02(*range(2), 2, *range(3, 4))

        # 2
        r1 = *range(2), 2
        pr('r1', r1)

        r2 = [*range(2), 2, *range(3, 10)]
        pr('r2', r2)

        d1 = {'a': 100, 'b': 200}
        d2 = {'f': 999}
        d3 = {**d1, 'c': 300, 'd': 400, **d2}
        pr('d3', d3)

    def pep448_01(self, *args):
        pr('pep448_01', args)

    def pep448_02(self, a, b, c, d):
        pr('pep448_02', a, b, c, d)


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
