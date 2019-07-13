"""
文字列に対する in 操作で複数の項目に対して一発で含むものが存在するかのサンプル
"""
from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        # 基本的なやり方
        target_str = 'abcede hello world 12345'

        items = 'z y x hello'.split()
        for x in items:
            if x in target_str:
                pr('basic', f'found: {x}')

        # any を使ったやり方
        found = any(x in target_str for x in items)
        if found:
            pr('any', f'found')


def go():
    obj = Sample()
    obj.exec()
