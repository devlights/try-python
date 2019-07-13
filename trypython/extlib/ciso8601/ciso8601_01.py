"""
ciso8601 ライブラリのサンプル

REFERENCES::
https://github.com/closeio/ciso8601
"""
import argparse
import time
from datetime import datetime, timedelta
from typing import Any, List

import ciso8601

from trypython.common.commoncls import SampleBase


class Sample(SampleBase):

    def __init__(self, count: int, mode: str, call_unaware: bool = False):
        """オブジェクトを初期化します。"""
        self.count = count
        self.mode = mode
        self.call_unaware = call_unaware

    def exec(self):
        """サンプル処理を実行します。"""
        # -----------------------------------
        # 日付解析用にデータを生成
        # -----------------------------------
        epoch = datetime.utcfromtimestamp(0)
        datetimes = [
            (epoch + timedelta(seconds=i)).isoformat()
            for i in range(self.count)
        ]

        # -----------------------------------
        # 利用するメソッドを特定
        # -----------------------------------
        f = self._call_ciso8601 if self.mode == 'ciso8601' else self._call_datetime  # noqa

        # -----------------------------------
        # 計測
        # -----------------------------------
        start = time.perf_counter()
        f(datetimes)
        elapsed = round(time.perf_counter() - start, 3)
        print(f'[{self.mode}]\tcount: {self.count}\telapsed: {elapsed}secs')  # noqa

    def _call_ciso8601(self, datetimes: List[str]):
        """ciso8601で日付解析を実施します。"""
        f = ciso8601.parse_datetime_unaware if self.call_unaware else ciso8601.parse_datetime  # noqa

        print(f'[method] {f.__name__}')
        for d in datetimes:
            f(d)

    # noinspection PyMethodMayBeStatic
    def _call_datetime(self, datetimes: List[str]):
        """datetimeで日付解析を実施します。"""
        for d in datetimes:
            datetime.strptime(d, '%Y-%m-%dT%H:%M:%S')


def go():
    obj = Sample(100000, 'ciso8601', False)
    obj.exec()


def _go(params: Any):
    obj = Sample(params.count, params.mode, params.call_unaware)
    obj.exec()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--count', type=int, default=100000)
    parser.add_argument('--mode', default='ciso8601', choices=['ciso8601', 'datetime'])  # noqa
    parser.add_argument('--call-unaware', action='store_true', default=False)
    args = parser.parse_args()
    _go(args)
