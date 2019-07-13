# coding: utf-8
"""
functools モジュールのサンプルです。
functools.lru_cache() について。
"""
import functools

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        # --------------------------------------------------
        # lru_cache()
        # ---------------------------
        # デコレータとして指定した関数をラップして
        # 指定された回数分のメモ化を行う。
        #
        # キャッシュヒットした場合は、本来の処理に入らず
        # キャッシュから値を返すため、速い。
        #
        # 元の関数オブジェクトには __wrapped__ でアクセス可能
        # 現在のキャッシュ状態は、cache_info() で確認できる
        # キャッシュをクリアする場合は、cache_clear() を呼び出す
        # --------------------------------------------------
        pr('functools.lru_cache()', type(self.my_sum))
        pr('functools.lru_cache()', self.my_sum.__wrapped__)
        pr('functools.lru_cache()', self.my_sum.cache_info())

        self.my_sum(1, 1)  # no hit
        self.my_sum(1, 2)  # no hit
        self.my_sum(1, 3)  # no hit
        self.my_sum(1, 1)  # hit

        pr('functools.lru_cache()', self.my_sum.cache_info())

        self.my_sum(1, 2)  # hit
        self.my_sum(1, 3)  # hit
        self.my_sum(1, 4)  # no hit

        pr('functools.lru_cache()', self.my_sum.cache_info())

        self.my_sum(1, 2)  # hit
        self.my_sum(1, 3)  # hit
        self.my_sum(1, 4)  # hit

        pr('functools.lru_cache()', self.my_sum.cache_info())

        self.my_sum.cache_clear()
        pr('functools.lru_cache()', self.my_sum.cache_info())

    @functools.lru_cache(maxsize=32)
    def my_sum(self, x, y):
        return x + y


def go():
    obj = Sample()
    obj.exec()
