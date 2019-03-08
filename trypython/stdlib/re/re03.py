"""
正規表現のサンプルです。

最長一致と最短一致について
"""
import re

from trypython.common.commoncls import SampleBase
from trypython.stdlib.re import util


class Sample(SampleBase):
    def exec(self):
        # ---------------------------------------------
        # 正規表現 (最長一致と最短一致)
        #
        # 正規表現はデフォルトで閉包を表すメタキャラクタ「*」は
        # 「最長一致」を行う。「最短一致」を行うには、「*?」を
        # 使う。
        # ---------------------------------------------
        message = 'hello world hello world'
        pattern = r'h.*d'

        # 最長一致
        m = re.match(pattern, message)
        util.print_match_object(m)

        # 最短一致
        pattern = r'h.*?d'
        m = re.match(pattern, message)
        util.print_match_object(m)


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
