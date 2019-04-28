"""
sys モジュールについてのサンプルです.

venv 環境での
  - sys.prefix
  - sys.exec_prefix
  - sys.base_prefix
  - sys.base_exec_prefix
の値について.

REFERENCES:: http://bit.ly/2Vun6U9
             http://bit.ly/2Vuvqn6
"""
import sys

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr, hr


class Sample(SampleBase):
    def exec(self):
        # --------------------------------------------
        # venv で仮想環境を作り、 activate している状態だと
        # sys モジュールの prefixとbase_prefixの値が異なる
        # 状態となる。仮想環境を使っていない場合、同じ値となる.
        # --------------------------------------------
        pr('prefix', sys.prefix)
        pr('exec_prefix', sys.exec_prefix)
        hr()
        pr('base_prefix', sys.base_prefix)
        pr('base_exec_prefix', sys.base_exec_prefix)

        pr('venv 利用している？', sys.prefix != sys.base_prefix)


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
