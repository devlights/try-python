"""
Python 3.8 にて導入された f-string での {xxx=} 表記についてのサンプルです。

REFERENCES:: http://bit.ly/2NlJkSc
"""
from trypython.common.commoncls import SampleBase


class Sample(SampleBase):
    def exec(self):
        # ------------------------------------------------------------
        # f-string debugging specifier
        #
        # f-string 内にて {xxx=} と イコールを付与した場合に
        # "xxx=値" を出力してくれるようになった。
        #
        # {xxx = } とすると、"xxx = 値"と表示してくれる
        #
        # フォーマット指示子も付与できる.
        # {xxx = :>10}
        # ------------------------------------------------------------
        s1 = "hello"
        s2 = "world"
        s3 = "hoge"

        print(f'{s1=}\t{s2 = }\t{s3=:>10}')


def go():
    obj = Sample()
    obj.exec()
