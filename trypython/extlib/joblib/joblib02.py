# coding: utf-8
"""
joblibモジュールについてのサンプルです。

joblib.Parallel の利用にて joblib側のログを出力する方法について。
"""
import datetime
import os
import random
import time

import joblib as job

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr, hr

NOW = datetime.datetime.now
RND = random.Random()
CPU_COUNT = -1

# ログ出力 (簡易)
LOG_VERBOSE = 1
# ログ出力 (詳細)
LOG_VERBOSE_ALL_ITERATION_REPORT = 10


class Sample(SampleBase):
    def exec(self):
        start_dt = NOW()

        # ----------------------------------------------------------
        # joblibのParallel() は、CPU数とは別にいくつかのオプション引数
        # を持つ。verboseもその一つで、値を指定することでjoblibの内部ログを
        # 出力することが出来る。値は、intとなっており、以下の値域を持つ。
        #
        # [verboseの値域]
        #   0以外: 進捗ログを出力する (簡易)
        #  10以上: 進捗ログを出力する (各イテレーション毎に出力してくれる)
        # ----------------------------------------------------------
        results = job.Parallel(n_jobs=CPU_COUNT, verbose=LOG_VERBOSE)(
            [
                job.delayed(heavy_proc)(f'value-{i}', RND.randrange(1, 3), True)
                for i in range(1, 5)
            ]
        )

        end_dt = NOW()

        pr('job-results', results)
        pr('total elapsed', (end_dt - start_dt).seconds)

        hr('log-verbose-all-iteration-report')
        start_dt = NOW()

        results = job.Parallel(n_jobs=CPU_COUNT, verbose=LOG_VERBOSE_ALL_ITERATION_REPORT)(
            [
                job.delayed(heavy_proc)(f'value-{i}', RND.randrange(1, 3), True)
                for i in range(1, 5)
            ]
        )

        end_dt = NOW()

        pr('job-results', results)
        pr('total elapsed', (end_dt - start_dt).seconds)


def heavy_proc(value: str, sleep_seconds: int, silent: bool) -> dict:
    start_dt = NOW()
    pid = os.getpid()

    if not silent:
        pr('start', f'pid: {pid} [{value}] sleep: {sleep_seconds}')

    time.sleep(sleep_seconds)

    if not silent:
        pr('end', f'pid: {pid} [{value}]')

    end_dt = NOW()

    return {
        'pid': pid,
        'elapsed': (end_dt - start_dt).seconds
    }


def go():
    obj = Sample()
    obj.exec()
