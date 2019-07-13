"""
sys モジュールに関するサンプルです.

- sys.getwindowsversion() について

REFERENCES:: http://bit.ly/2KQeJOH
"""
import sys

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        # ---------------------------------------------------------
        # sys.getwindowsversion()
        #
        # Windows のバージョン情報を返す.
        # 当然ながら、Windows の場合だけ動作する.
        #
        # Python 3.2 より、戻り値が namedtuple になった。
        # Python 3.6 で platform_version が追加となった。
        # ---------------------------------------------------------
        win_ver = sys.getwindowsversion()
        pr('win_ver', win_ver)
        pr('type()', type(win_ver))
        pr('major', win_ver.major)
        pr('minor', win_ver.minor)
        pr('platform_version', win_ver.platform_version)


def go():
    obj = Sample()
    obj.exec()
