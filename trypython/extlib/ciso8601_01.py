"""
ciso8601 ライブラリのサンプル

REFERENCES::
https://github.com/closeio/ciso8601
"""
import time
from datetime import datetime, timedelta

import ciso8601
from trypython.common.commoncls import SampleBase


class Sample(SampleBase):

    def __init__(self, count, mode, call_unaware=False):
        self.count = count
        self.mode = mode
        self.call_unaware = call_unaware

    def exec(self):
        epoch = datetime.utcfromtimestamp(0)
        datetimes = [
            (epoch + timedelta(seconds=i)).isoformat()
            for i in range(self.count)
        ]

        f = self._call_ciso8601 if self.mode == 'ciso8601' else self._call_datetime  # noqa

        start = time.perf_counter()
        f(datetimes)
        elapsed = round(time.perf_counter() - start, 3)
        print(f'[{self.mode}]\tcount: {self.count}\telapsed: {elapsed}secs')  # noqa

    def _call_ciso8601(self, datetimes):
        f = ciso8601.parse_datetime_unaware if self.call_unaware else ciso8601.parse_datetime  # noqa

        print(f'[method] {f.__name__}')
        for d in datetimes:
            f(d)

    def _call_datetime(self, datetimes):
        for d in datetimes:
            datetime.strptime(d, '%Y-%m-%dT%H:%M:%S')


def go():
    obj = Sample(100000, ciso8601.__name__)
    obj.exec()


if __name__ == '__main__':
    go()
