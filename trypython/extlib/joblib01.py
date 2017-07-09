# coding: utf-8
"""
joblib モジュールについてのサンプルです。
"""

import datetime
import os
import random
import time

import joblib

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr

NOW = datetime.datetime.now
RND = random.Random()


class Sample(SampleBase):
    def exec(self):
        start_dt = NOW()

        results = joblib.Parallel(n_jobs=-1)(
            [
                joblib.delayed(heavy_proc)(f'value-{i}', RND.randrange(1, 10))
                for i in range(1, 5)
            ]
        )

        end_dt = NOW()

        pr('job-results', results)
        pr('total elapsed', (end_dt - start_dt).seconds)


def heavy_proc(value: str, sleep_seconds: int) -> dict:
    start_dt = NOW()
    pid = os.getpid()
    pr('start', f'pid: {pid} [{value}] sleep: {sleep_seconds}')
    time.sleep(sleep_seconds)
    pr('end', f'pid: {pid} [{value}]')
    end_dt = NOW()

    return {
        'pid': pid,
        'elapsed': (end_dt - start_dt).seconds
    }


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
