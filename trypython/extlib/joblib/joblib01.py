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
        # ----------------------------------------------------------
        # joblib モジュールは、以下の機能を持つライブラリ。
        #   ・透過的で速いキャッシュ (joblib.Memory)
        #   ・並列処理ヘルパー (joblib.Parallel)
        #   ・pickleの代わりに利用できる永続化 (joblib.dump/load)
        # ----------------------------------------------------------
        start_dt = NOW()

        # ----------------------------------------------------------
        # joblib.Parallelの最も基本的な利用方法
        # --------------------------------------
        # Parallel関数の引数「n_jobs」には並列稼働させる数を指定する。
        # ここで指定された値分のプロセスが起動して並列処理を実施する。
        # 値に -1 を指定すると、マシンのCPU数を指定したことと同じになる。
        #
        # Parallelの中で、並列処理したい処理に対して joblib.delayed を
        # 指定して処理する。delayed関数の引数に実際の処理を実施する関数を
        # 指定し、返ってくるオブジェクトに対して元々の関数の引数を指定する。
        # ----------------------------------------------------------
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
