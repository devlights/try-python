# coding: utf-8

"""
multiprocessingモジュールについてのサンプルです。
"""
import multiprocessing
import os
import time

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        #
        # multiprocessingモジュール
        # threadingと似た構成を持つモジュール。threadingがスレッドを扱うのに
        # 対して、こちらはプロセスを扱う。Pythonでは、GILの絡みがあって
        # マルチコアな処理をthreadingで記述することが難しいため
        # そのような処理を記述する場合は multiprocessing モジュールを利用する
        #
        # つまり、CPUバウンドな処理の場合は multiprocessing, IOバウンドな処理は
        # threadingのような利用用途となる。
        #

        #
        # multiprocessingモジュールで最も基本的なものが Process.
        # その名の通り、プロセスを表す。
        #
        c01 = multiprocessing.current_process()
        p01 = multiprocessing.Process(target=Sample.fn01, args=['hello from another process'])

        pr('current process', c01.pid)

        p01.start()  # 開始
        p01.join()  # 終了待機

        #
        # 便利なものとして、Pool がある。
        # 指定した数のプロセスを起動してコネクションプールのように扱える
        #
        with multiprocessing.Pool(os.cpu_count()) as pl:
            pr('Pool.map()', pl.map(Sample.fn02, list(range(10))))

    @staticmethod
    def fn01(message):
        pr('fn01', f'{os.getpid()}-{message}')

    @staticmethod
    def fn02(x):
        pr('pid()', os.getpid())
        time.sleep(1)
        return x * x


def go():
    obj = Sample()
    obj.exec()
