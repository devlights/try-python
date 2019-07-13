"""
time モジュールに関するサンプルです。
"""
import time

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        # -------------------------------------------------------
        # time モジュール
        # -------------
        # timeモジュールは、時刻に関する関数を提供する。
        # UNIX時間（epoch) を扱う際に利用することになる。
        # epochからの経過秒は、 time.time() で取得できる。
        # また、他の言語では Thread.Sleep のようにスレッド関連の処理として
        # 属している sleep 関数が、pythonではtimeモジュールにある。
        #
        # よく利用する関数は以下のもの。
        #
        #   - time.time()
        #   - time.localtime()
        #   - time.perf_counter()
        #   - time.sleep()
        #   - time.strftime()
        #
        # time.perf_counter() は、time.time()が返すものよりも高精度なので
        # 処理時間を計測したい場合は、こちらを利用するほうが良い。
        # -------------------------------------------------------
        t1 = time.time()
        pr('t1', t1)

        time.sleep(3)

        t2 = time.time()
        pr('t2', t2)
        pr('diff', t2 - t1)

        lt1 = time.localtime(t1)
        lt2 = time.localtime(t2)
        pr('localtime', lt1)
        pr('localtime', lt2)

        # strftimeには、struct_timeか時刻を表す９要素のタプルが必要
        pr('strftime', time.strftime('%Y/%m/%d %H:%M:%S', lt1))
        pr('strftime', time.strftime('%Y/%m/%d %H:%M:%S', lt2))


def go():
    obj = Sample()
    obj.exec()
