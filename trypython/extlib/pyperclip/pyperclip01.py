# coding: utf-8
"""
pyperclip モジュールについてのサンプルです。
"""
import pyperclip as clip

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        # ---------------------------------------------------------------
        # [link]
        # https://github.com/asweigart/pyperclip
        # http://pyperclip.readthedocs.io/en/latest/introduction.html
        # ---------------------------------------------------------------
        # pyperclip モジュールは、クリップボードとのテキストデータを簡単に
        # やり取りできるモジュール。クロスプラットフォーム対応しているため
        # windows, mac, linux で動作する。
        # ---------------------------------------------------------------
        # 利用する関数は、 copy() と paste() の二つだけ。
        # ---------------------------------------------------------------
        # 注意点として、やり取りできるのはテキストデータのみとなる。
        # テキストデータ以外を操作したい場合は、各プラットフォームのAPIを叩く必要がある。
        # (windowsの場合は、win32com とか)
        # ---------------------------------------------------------------

        # クリップボードにコピー
        clip.copy('hello world from pyperclip')

        # クリップボードから取得
        clipboard_text = clip.paste()
        pr('paste()', clipboard_text)

        #
        # この後、エディタ上で CTRL+V すると同じ文字列がペーストされる。
        #


def go():
    obj = Sample()
    obj.exec()
