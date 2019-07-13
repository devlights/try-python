"""
async-timeout モジュールについてのサンプルです

基本的な使い方について

REFERENCES:: http://bit.ly/2O0kYNP
"""
import asyncio
import contextlib

from async_timeout import timeout

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


# noinspection PyMethodMayBeStatic
class Sample(SampleBase):
    def exec(self):
        asyncio.run(self.async_run())

    async def async_run(self):
        # ---------------------------------------------------------------------------
        # async-timeout モジュール
        # -----------------------------------------
        # asyncio 処理を書く際のタイムアウト処理をスムーズに記述できるようにしてくれるライブラリ
        # timeoutクラスがコンテキストマネージャとして利用できるので async with で利用する
        #
        # オブジェクトには、
        #   - expired
        #   - remaining
        # というプロパティが存在しており、それぞれ
        #   - タイムアウトしたかどうか
        #   - 残り時間
        # を取得できる
        # ---------------------------------------------------------------------------

        # タイムアウト時間内に処理を終えた場合は何も起こらない
        async with timeout(1.5) as tm1:
            await asyncio.sleep(1)
        pr('timeout(1.5) vs sleep(1) expired', tm1.expired)
        pr('timeout(1.5) vs sleep(1) remaining', tm1.remaining)

        # タイムアウトが発生した場合、 asyncio.TimeoutError が raise される
        try:
            async with timeout(1) as tm2:
                await asyncio.sleep(2)
        except asyncio.TimeoutError as e:
            pr('TimeoutError', e)
        else:
            pr('timeout(1) vs sleep(2) expired', tm2.expired)
            pr('timeout(1) vs sleep(2) remaining', tm2.remaining)

        # コンテキストマネージャでタイムアウトしたかわかるので、以下でもいいかも
        with contextlib.suppress(asyncio.TimeoutError):
            async with timeout(1) as tm3:
                await asyncio.sleep(2)

        pr('timeout(1) vs sleep(2) with suppress expired', tm3.expired)
        pr('timeout(1) vs sleep(2) with suppress remaining', tm3.remaining)


def go():
    obj = Sample()
    obj.exec()
