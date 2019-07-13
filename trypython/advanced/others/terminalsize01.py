"""
ターミナルの行列のサイズを取得するサンプルです。

REFERENCES: http://bit.ly/2Vw6asZ
            http://bit.ly/2VutNSI
            http://bit.ly/2VsJOZi
            http://bit.ly/2VrpMhR
"""
import shutil
from os import terminal_size

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        # ----------------------------------------------------------
        # shutil.get_terminal_size() を利用することで
        # 現在実行しているターミナルの行と列のサイズを取得することができる。
        #
        # shutil.get_terminal_size() は、内部で os.get_teminal_size()
        # を呼び出すようになっている。
        #
        # 戻り値は、 os.terminal_size オブジェクト
        #
        # 対応しているOSは、 unix, windows となっている。
        # この関数が追加されたのは、 python 3.3
        # ----------------------------------------------------------
        ts: terminal_size = shutil.get_terminal_size()
        pr('terminal size', ts)
        pr('\tcolumns', ts.columns)
        pr('\tlines', ts.lines)


def go():
    obj = Sample()
    obj.exec()
