# coding: utf-8
"""
組み込み関数 iter(callable, sentinel) についてのサンプルです。
"""

import os

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class MySentinel:
    def __eq__(self, o: object) -> bool:
        return 'sentinel' == str(o).replace('\n', '')


class Sample(SampleBase):
    def __init__(self) -> None:
        super().__init__()
        self._file = '/tmp/test.txt'

    def exec(self):
        ####################################################
        # iter(callable, sentinel)
        #
        # 組み込み関数の iter は、引数が一つの場合と
        # 二つの場合で挙動が異なる。
        #
        # 引数が一つの場合、要求される引数は iterable だが
        # 引数が二つの場合、要求される引数は
        #    callable と sentinel
        # となる。
        #
        # sentinel は、日本語で言うと「番兵」の事。
        # iter(callable, sentinel) は、毎回 calable を
        # 呼び出して、その値が sentinel と等しいかを判定する。
        #
        # 等しい場合は、StopIteration が発生して
        # イテレーションが終わる。
        #
        # なので、何かの値が出てくるまで継続するという
        # 処理と記述する時に使える。
        ####################################################
        try:
            self._write_dummy_file()

            with open(self._file, mode='r', encoding='utf-8') as f:
                sentinel = MySentinel()
                it = iter(f.readline, sentinel)

                for i, line in enumerate(it):
                    pr(f'line-{i:02}', line)
        finally:
            self._delete_dummy_file()

    def _write_dummy_file(self):
        with open(self._file, mode='w', encoding='utf-8', newline='') as f:
            print('helloworld', file=f)
            print('sentinel', file=f)
            print('helloworld', file=f)

    def _delete_dummy_file(self):
        if os.path.exists(self._file):
            os.remove(self._file)


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
