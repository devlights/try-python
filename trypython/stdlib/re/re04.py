"""
正規表現のサンプルです。

アトミックグループ (Atomic Groups) について

REFERENCES:: http://bit.ly/2O3jVNn
             http://bit.ly/2NXqocl
"""
import re

import regex

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import stopwatch, pr

_message = '1' * 300000000


# noinspection PyMethodMayBeStatic
class Sample(SampleBase):
    def exec(self):
        # ------------------------------------------------------------------------
        # アトミックグループについて
        # -----------------------------------------
        # 正規表現で処理する場合、処理速度に差がでるのは以下の部分
        #     - バックトラックの発生頻度
        # バックトラックの発生を以下に防ぐかによって処理速度に差が出る。
        # 通常の正規表現は「最長一致」であり、指定されたパターンで「可能な限り」
        # 前に進んでいく。例えば, 「123456」という文字列があった場合に
        # 「\d*」というパターンを指定すると、数字の連続をすべて飲み込む。
        # 「\d*:」というパターンを指定した場合でも、最初の「\d*」が
        # 数字部分全部を飲み込み、その後で、残りの「:」についてマッチするかどうかを
        # 判定することになる。マッチしないので、正規表現エンジンはバックトラックして
        # 位置を探しなおす。このバックトラックが発生すればするほど処理に時間がかかる。
        #
        # このような場合に、「ここまできて失敗したのなら、バックトラックする必要なし」
        # ということを事前に通知することができる。
        # このときに指定するのが「アトミックグループ」となる。
        # アトミックグループの挙動は、「グループ内のパターンに一旦マッチした後は
        # その中のステートを全て破棄し、バックトラックさせないようにする」というもの。
        #
        # アトミックグループは、以下の書式で定義する
        #     (?>pattern)
        # 上のパターンをアトミックグループの指定に変更すると以下のようになる。
        #     (?>\d*):
        #
        # ただし、問題が一つあって、python の標準モジュール re は
        #     アトミックグループに対応していない
        # 無理矢理同じことを行うようには出来るみたい。(http://bit.ly/2O3jVNn 参照)
        #
        # 標準モジュールではないが、PYPI に regex というモジュールがあり
        # こちらは、アトミックグループに対応している。(http://bit.ly/2NXqocl 参照)
        # インストールする場合は以下を実行
        #   $ python -m pip install regex
        #
        # アトミックグループ指定している場合、バックトラックが発生しないので
        # マッチしない場合の判定がとても速くなる。(通常のモードだとマッチしないか
        # どうかを最終判定するまでにバックトラックを繰り返さないといけないため)
        # ------------------------------------------------------------------------

        # アトミックグループ指定なし
        stopwatch(self.normal)()

        # 標準モジュール re で、無理矢理
        stopwatch(self.atomic_stdlib_re)()

        # 外部ライブラリ rexex でアトミックグループ指定
        stopwatch(self.atomic_regex_module)()

    def normal(self):
        global _message
        m = re.match(r'\d*:', _message)
        if m:
            pr('normal', 'マッチした')
        else:
            pr('normal', 'マッチしない')

    def atomic_stdlib_re(self):
        global _message
        m = re.match(r'(?=(?P<tmp>\d*:))(?P=tmp)', _message)
        if m:
            pr('atomic_stdlib_re', 'マッチした')
        else:
            pr('atomic_stdlib_re', 'マッチしない')

    def atomic_regex_module(self):
        """Python の 標準モジュール re は、アトミックグループをサポートしていない。
        http://bit.ly/2O3jVNn に記載されているように、無理やり評価させることも可能
        らしいのだが、「regex」モジュールを pip でインストールして利用する方が楽。
        「regex」モジュールは、(?>pattern)の書式をサポートしている。
        """
        global _message
        m = regex.match(r'(?>\d*):', _message)
        if m:
            pr('atomic_regex_module', 'マッチした')
        else:
            pr('atomic_regex_module', 'マッチしない')


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
