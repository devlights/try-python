"""
datetime モジュールについてのサンプルです。

datetime.datetime オブジェクトについての基本的な情報について
"""
from datetime import datetime

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import hr, pr


class Sample(SampleBase):
    def exec(self):
        #############################################
        # datetime.datetime オブジェクトについて
        #
        # datetime.datetime オブジェクトは 日付を表す。
        # このオブジェクトは日付処理を行う上で最低限必要な情報を
        # 各種備えている。
        #
        # 現在日時を取得するには
        #     datetime.now()
        # とする。
        # (from datetime import datetime としているとする)
        #############################################
        hr('datetime.now()')
        now = datetime.now()

        pr('now', now)
        pr('type', type(now))

        # --------------------------------------------
        # datetime.ctime()
        # --------------------------------------------
        # 日付文字列を ctime スタイルで表示
        #    https://bit.ly/2PGoEYB
        # --------------------------------------------
        hr('datetime.ctime()')
        ctime_value = now.ctime()
        pr('ctime', ctime_value)
        pr('type', type(ctime_value))


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
