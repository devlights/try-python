"""
aiojobs ライブラリのサンプルです。

基本的な使い方について。

REFERENCES:: https://git.io/fjn1o
             http://bit.ly/2GYmZqU
"""
import asyncio

import aiojobs

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


# noinspection PyMethodMayBeStatic
class Sample(SampleBase):
    def exec(self):
        asyncio.run(self.async_main())

    async def async_main(self):
        # ---------------------------------------
        # aiojobs
        #   基本的な使い方については
        #   http://bit.ly/2GYmZqU
        #   を参照のこと。
        # ---------------------------------------
        # スケジューラ作成
        scheduler = await aiojobs.create_scheduler()

        # ジョブを生成
        jobs = []
        for i in range(5):
            jobs.append(await scheduler.spawn(self.coro(float(i), i)))

        # 現在の状況表示
        self.print_status('ジョブ生成直後', jobs)

        # 1 秒待機
        await asyncio.sleep(1.0)

        # 現在の状況表示
        self.print_status('1秒待機後', jobs)

        # 1 秒待機
        await asyncio.sleep(1.0)

        # 現在の状況表示
        self.print_status('2秒待機後', jobs)

        # スケジューラを落とす
        await scheduler.close()

        # 現在の状況表示
        self.print_status('スケジューラをclose後', jobs)

    async def coro(self, timeout: float, task_id: int):
        try:
            await asyncio.sleep(timeout)
            pr('done', task_id)
        except asyncio.CancelledError:
            pr('cancelled', task_id)

    def print_status(self, name: str, jobs: list):
        pr(name, [
            f'active={job.active} closed={job.closed} pending={job.pending}'
            for job in jobs
        ])


def go():
    obj = Sample()
    obj.exec()
