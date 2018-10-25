"""
datetime.fromtimestamp() についてのサンプルです。
"""
import time
from datetime import datetime

from common.commoncls import SampleBase
from common.commonfunc import hr


class Sample(SampleBase):
    def exec(self):
        #############################################
        # datetime.fromtimestamp メソッドについて
        #
        # datetimeには、POSIX タイムスタンプを手軽に日時に変換できる
        #     fromtimestamp
        # メソッドが存在する。このメソッドにタイムスタンプを渡すと
        # datetimeに変換してくれる.
        #############################################
        hr('fromtimestamp(0)')

        try:
            print(datetime.fromtimestamp(0))
        except OSError as e:
            # 呼び出し失敗は OSError が送出される
            print(e)

        hr('fromtimestamp(time.time())')
        now = time.time()
        print(datetime.fromtimestamp(now))


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
