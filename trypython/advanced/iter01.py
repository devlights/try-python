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
