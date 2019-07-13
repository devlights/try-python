"""
正規表現のサンプルです

「ブラケット表現」について
"""
import re

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr
from trypython.stdlib.re_ import util


class Sample(SampleBase):
    def exec(self):
        # -----------------------------------------------------------
        # ブラケット表現
        # --------------------------
        # [ と ] で括られた内部に指定された文字のいずれかにマッチする.
        # マッチするのは、その中の「1文字」だけという点に注意.
        #
        # ブラケット表現内の正規表現を否定する場合は
        #   [^abc]
        # という風に、内部のパターンの先頭に ^ を付与する.
        # このように ^ を利用して否定の意味を持たせたものを
        # 「非マッチングリスト」と呼ぶ。
        #
        # [from-to] という表現もサポートしている
        # [a-z]とすると a から z までマッチする
        # -----------------------------------------------------------
        s = 'a'
        p = r'[abc]'
        r = re.compile(p)
        m = r.match(s)
        if m:
            util.print_match_object(m)

        s = 'z'
        m = r.match(s)
        if not m:
            pr('[abc].match("z")', 'マッチしない')

        p = r'[^abc]'
        r = re.compile(p)
        m = r.match(s)
        if m:
            util.print_match_object(m)

        p = r'[a-z]'
        r = re.compile(p)
        m = r.match(s)
        if m:
            util.print_match_object(m)


def go():
    obj = Sample()
    obj.exec()
