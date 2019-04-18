"""
tempfile モジュールに関するサンプルです。

tempfile.TemporaryFile() の使い方について

REFERENCES:: http://bit.ly/2GqQLVY
"""
import os
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
        # tempfile.TemporaryFile() は
        # 一時的な記憶領域として利用できる file-like オブジェクトを返す.
        # コンテキストマネージャと併用して
        # 利用できるようになっており、これにより with ブロック内
        # のみ生存する一時ファイルの利用ができる。
        #
        # with ブロックを抜けた後、この一時ファイルは
        # 自動的に削除される。明示的に削除処理を実施したい場合は
        # cleanup() を呼び出すと削除できる。
        #
        # 注意点として、デフォルトのmodeが w+b となっているため
        # データを読み書きする場合は bytes で扱うことに注意。
        #
        # tempfile.TemporaryFile() は 3.5 で追加された。
        # ----------------------------------------------
        with tempfile.TemporaryFile() as tmpfile:
            pr('tmpfile', tmpfile)
            pr('type', type(tmpfile))
            pr('name', tmpfile.name)

            # 通常のファイルのように読み書きすることができる
            # ただし、デフォルトの mode は w+b なので bytes 経由で
            # データをやり取りする必要がある
            lines = [f'{i}:helloworld{os.linesep}' for i in range(5)]
            for line_str in lines:
                # bytes へ エンコード
                b = line_str.encode('utf-8')
                tmpfile.write(b)

            tmpfile.seek(os.SEEK_SET)
            for line_bytes in tmpfile:
                # bytes から デコード
                s = line_bytes.decode('utf-8')
                pr('line_str', s)

            # with ブロックの中にいる間、ファイルは開いている
            pr('closed', tmpfile.closed)
        # with ブロックを抜けると、ファイルは閉じている
        pr('closed', tmpfile.closed)


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
