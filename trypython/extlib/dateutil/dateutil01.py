"""
dateutil (python-dateutil) モジュールに関するサンプルです。

relativedelta について

REFERENCES:: http://bit.ly/2KNPi0p
"""
import datetime

import dateutil.relativedelta

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        today = datetime.date.today()
        pr('today', today)

        # 10 日後
        d1 = dateutil.relativedelta.relativedelta(days=+10)
        pr('10 days after', today + d1)

        # 1 ヶ月後
        d2 = dateutil.relativedelta.relativedelta(months=+1)
        pr('1 month after', today + d2)

        # 3 週間前
        d3 = dateutil.relativedelta.relativedelta(weeks=-3)
        pr('3 weeks ago', today + d3)

        # 2 年前
        d4 = dateutil.relativedelta.relativedelta(years=-2)
        pr('2 years ago', today + d4)

        # 現在日時
        now = datetime.datetime.now()
        pr('now', now)

        # 20 時間前
        d5 = dateutil.relativedelta.relativedelta(hours=-20)
        pr('20 hours ago', now + d5)

        # 2 週間と 10 日後
        d6 = dateutil.relativedelta.relativedelta(weeks=+2, days=+10)
        pr('2 weeks and 10 days after', today + d6)


def go():
    obj = Sample()
    obj.exec()
