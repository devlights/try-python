# coding: utf-8
"""
psutil モジュールについてのサンプルです。
"""
import psutil as ps

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        # ---------------------------------------------------------------
        # [link]
        # https://github.com/giampaolo/psutil
        # ---------------------------------------------------------------
        # psutil モジュールは
        #   - CPU時間
        #   - メモリ情報
        #   - ディスク情報
        #   - ネットワーク情報
        #   - センサー情報
        #   - ユーザ情報
        #   - プロセス情報
        # といったシステム情報が取得できる便利なモジュール。
        # ---------------------------------------------------------------
        # 空きメモリを取得するには、virtual_memory() を使用して取得できる
        # svmem オブジェクトの available プロパティから取得できる。
        # ---------------------------------------------------------------
        virtual_memory = ps.virtual_memory()
        available_memory_bytes = virtual_memory.available  # type: int

        available_memory_gb = self._to_gb(float(available_memory_bytes))
        pr('available_memory', self._adjust(available_memory_gb))

    def _to_kb(self, byte_size: float) -> float:
        return byte_size / 1024

    def _to_mb(self, byte_size: float) -> float:
        return self._to_kb(byte_size) / 1024

    def _to_gb(self, byte_size: float) -> float:
        return self._to_mb(byte_size) / 1024

    def _adjust(self, value: float) -> float:
        return round(value, 2)


def go():
    obj = Sample()
    obj.exec()
