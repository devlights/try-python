"""
tempfile モジュールに関するサンプルです。

tempfile.gettempdir() の使い方について

REFERENCES:: http://bit.ly/2GqvFac
"""
import tempfile

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        # ----------------------------------------------
        # tempfile.gettempdir() は
        # そのOSで安全に利用できる一時ディレクトリのパスを
        # 返してくれる。
        # ----------------------------------------------
        pr('gettempdir', tempfile.gettempdir())


def go():
    obj = Sample()
    obj.exec()
