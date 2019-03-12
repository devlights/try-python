"""
正規表現のサンプルです。

先頭を表す ^ と 末尾を表す $ について
"""
import re

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr
from trypython.stdlib.re import util


class Sample(SampleBase):
    def exec(self):
        # ---------------------------------------------
        # 正規表現 (^ と $)
        #
        # ^ は先頭を表し、$ は末尾を表す
        # ---------------------------------------------
        message = 'hello world'
        pattern = r'^h.*d$'

        r = re.compile(pattern)
        m = r.match(message)

        pr('r', r)
        util.print_match_object(m)


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
