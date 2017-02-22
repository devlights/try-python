# coding: utf-8

"""
secretsモジュールについてのサンプルです。
"""
import secrets
import string

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        #
        # secretsモジュールは、3.6から追加された標準モジュール
        # 文字通りセキュアな値を管理することを目的としている
        #
        # パスワードやトークンの生成時に利用できる
        #
        pr('generate passwd', self.generate_password(32))
        pr('url_token', secrets.token_urlsafe(32))

    def generate_password(self, nbytes=8):
        """指定されたバイト数でパスワードを生成します。"""
        characters = string.ascii_letters + string.digits
        generate_chars = (secrets.choice(characters) for __ in range(nbytes))
        return ''.join(generate_chars)


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
