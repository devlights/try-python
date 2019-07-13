"""
Python 3.7 で 辞書の挿入順序が保持されることを確認するサンプルです。

REFERENCES:: http://bit.ly/2VIggXP
             http://bit.ly/2VySRIe
             http://bit.ly/2VFhjI4
             http://bit.ly/2VEq058
             http://bit.ly/2VBKrzK
"""
from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        """コードのネタは http://bit.ly/2VBKrzK　から拝借"""
        languages = ['Python', 'Ruby', 'Perl', 'Python', 'JavaScript']

        # sorted + set + list.index を組み合わせて 順序キープ しながら重複削除 (from http://bit.ly/2VBKrzK)
        pr('sorted + set + list.index', sorted(set(languages), key=languages.index))

        # python 3.7 からは dict にて挿入順序が保持されることがPython 言語仕様の一部となったので、これでも良い
        pr('dict (python 3.7)', list(dict.fromkeys(languages)))

        # ちなみに 順序保証 をしない set() を使うと重複削除はできるけど、当然順序はキープできない
        pr('set (python 3.7)', list(set(languages)))


def go():
    obj = Sample()
    obj.exec()
