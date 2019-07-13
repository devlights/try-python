# coding: utf-8
"""splitlinesメソッドについてのサンプルです。"""
import os

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr

DATA = """
一行目
二行目
三行目
"""


class Sample(SampleBase):
    def exec(self):
        # ----------------------------------------
        # splitとsplitlines
        # --------------------
        # 以下をmacとlinuxで実行すると同じ結果に
        # なるが、windowsで実行するとos.linesep
        # でsplitした場合に、ちゃんと分割されない
        # ときがあった。splitlinesを利用すると
        # どのOSの場合でも同じ挙動になる。
        #
        # ちなみに、Windowsの場合は os.linesep
        # ではなくて、直接 '¥n'を指定すると
        # うまくいった。
        #
        # 参考URL
        #   http://stackoverflow.com/questions/24237524/how-to-split-a-python-string-on-new-line-characters
        # ----------------------------------------
        pr('os.linesep', [line for line in DATA.split(os.linesep) if line])
        pr('splitlines', [line for line in DATA.splitlines() if line])
        # pr('for-windows', [line for line in DATA.split('¥n') if line])


def go():
    obj = Sample()
    obj.exec()
