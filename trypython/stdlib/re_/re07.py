"""
正規表現のサンプルです

部分正規表現（「(」と「)」）のグルーピングについて

REFERENCES:: http://bit.ly/2TVtVNY
             http://bit.ly/2TVRy8Z
             http://bit.ly/2TWQQs4
"""
import re

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr
from trypython.stdlib.re_ import util


class Sample(SampleBase):
    def exec(self):
        # ---------------------------------------------------
        # 部分正規表現のグルーピング
        # -----------------------------
        # 「(」と「)」に囲まれた正規表現をひとまとまりにして
        # 部分正規表現を定義することができる.
        #
        # 「(」と「)」を入れ子にすることも可能.
        #
        # 例えば (abc)+ という正規表現は
        # 「abcという文字列が一回以上連続した文字列」を表す.
        #
        # また、通常の四則計算と同様に優先度を変更するためにも利用する.
        #
        # 例えば、「田中|佐藤 太郎」という正規表現は
        # 「田中、または佐藤 太郎を意味する。これを
        # 「(田中|佐藤) 太郎」とすると、田中 太郎、または佐藤 太郎
        # という意味となる。
        #
        # グルーピングには、もう一つ大きな役目があり
        # 「マッチした範囲をキャプチャ（記憶）する」という事もできる.
        # キャプチャした内容は後から特別な記法により取り出す事が可能.
        # 置換などを行う際に重宝する.
        # ---------------------------------------------------
        s = '田中 太郎'
        p = r'田中|佐藤 太郎'
        r = re.compile(p)
        m = r.match(s)
        if m:
            # 田中 太郎でマッチせずに 「田中」のみがマッチする
            util.print_match_object(m)

        m = r.fullmatch(s)
        if not m:
            # fullmatch 指定した場合はマッチしないと判定される
            # fullmatch メソッドは python 3.4 で追加された
            pr(f'({p}).fullmatch({s})', 'マッチせず')

        p = r'(田中|佐藤) 太郎'
        r = re.compile(p)
        m = r.match(s)
        if m:
            # グルーピング指定しているので「田中 太郎」でマッチする
            # かつ、グルーピングにより「田中」の部分がキャプチャされる
            util.print_match_object(m)

        m = r.fullmatch(s)
        if m:
            # グルーピング指定しているので「田中 太郎」でフルマッチする
            # かつ、グルーピングにより「田中」の部分がキャプチャされる
            util.print_match_object(m)


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
