"""
正規表現のサンプルです。

絶対最大量指定子 (possessive quantifier) について
(絶対最大量指定子は、強欲な量指定子ともいう)

REFERENCES:: http://bit.ly/2NW2TAq
             http://bit.ly/2NXU6Ow
             http://bit.ly/2NXUcFS
             http://bit.ly/2NZDm9v
             http://bit.ly/2NXxyNQ
"""
import re

import regex

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):

    def exec(self):
        # ------------------------------------------------------------------------
        # 絶対最大量指定子 (possessive quantifier) について
        # -----------------------------------------
        # アトミックグループ (atomic groups) と同じ考え方で導入されたのが
        # 「*+」というメタキャラクタが従う「強欲」という考え方。
        #
        # 「*+」は「*」と似ているが、アトミックグループと同様に、マッチした範囲のステートを
        # 破棄してバックトラックをしないようになる
        #
        # アトミックグループと同様に、この絶対最大量指定子も標準モジュール re ではサポート
        # されていない。 regex モジュールではサポートされている。
        # ------------------------------------------------------------------------

        # 標準 re モジュールは 「*+」をサポートしていない
        s = 'aaaabbbb'
        p = r'.*+b+'
        try:
            re.compile(p)
        except re.error as e:
            pr('re.error', '標準モジュール re では 「*+」はサポートされていない', e)

        # regex モジュールは　「*+」をサポートしている
        #   この場合、パターンとして指定している「.*+b+」の「.*+」が aaaabbbb 全体に
        #   マッチするが、まだパターンとして「b+」が残っているためバックトラックしようと
        #   するが、絶対最大量指定子を指定しているため、バックトラックが発生せずにここで
        #   マッチ失敗と判定される。
        r = regex.compile(p)
        m = r.match(s)
        if not m:
            pr('.*+b+', '絶対最大量指定子を使っているのでマッチしない (正解)')

        # パターンから絶対最大量指定子をなくして、「.*b+」とすると当然マッチする
        p = r'.*b+'
        r = regex.compile(p)
        m = r.match(s)
        if m:
            pr('.*+b+', '絶対最大量指定子を使っていないのでマッチする (正解)')


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
