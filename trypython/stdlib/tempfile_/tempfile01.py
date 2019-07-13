"""
tempfile モジュールに関するサンプルです。

tempfile.TemporaryDirectory() の使い方について

REFERENCES:: http://bit.ly/2KIbuZC
"""
import pathlib
import tempfile

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        # ----------------------------------------------
        # tempfile モジュールを利用すると
        # 一時ファイルや一時ディレクトリに関する操作を
        # 簡単に行うことができる。またOSを問わず利用できる。
        #
        # tempfile.TemporaryDirectory() は
        # tempfile.mkdtemp() と同じ方法で安全に一時ディレクトリを
        # 作成することができる。コンテキストマネージャと併用して
        # 利用できるようになっており、これにより with ブロック内
        # のみ生存する一時ディレクトリの利用ができる。
        #
        # with ブロックを抜けた後、この一時ディレクトリは
        # 自動的に削除される。明示的に削除処理を実施したい場合は
        # cleanup() を呼び出すと削除できる。
        #
        # 同じ方法で利用できるものとして
        #   - tempfile.TemporaryFile()
        # がある。
        #
        # tempfile.TemporaryDirectory() は 3.2 で追加
        # tempfile.TemporaryFile() は 3.5 で追加された。
        # ----------------------------------------------
        with tempfile.TemporaryDirectory() as tmpdir:
            pr('tmpdir', tmpdir)
            pr('type(tmpdir)', type(tmpdir))

            # with ブロック内では一時ディレクトリは存在している
            p = pathlib.Path(tmpdir)
            pr('exists (inside with block)', p.exists())

        # with ブロックを抜けた後は一時ディレクトリが削除されている
        pr('exists (outside with-block)', p.exists())


def go():
    obj = Sample()
    obj.exec()
