# coding: utf-8
"""gcモジュールについてのサンプルです。"""
import gc
import secrets
import string

from trypython.common.commoncls import SampleBase, timetracer
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def __init__(self) -> None:
        super().__init__()
        self._data_list = None
        self._characters = string.ascii_letters + string.digits

    def exec(self):
        # ------------------------------------------------
        # gcモジュール
        # ------------------------------------------------
        # gcモジュールには、その名前の通りガベージコレクション
        # 関連の操作が行えるモジュールとなっている。
        #
        # gc.get_objects() は、現在Pythonが追跡対象と
        # マークしているオブジェクトのリストを返す。
        # -----------------------------------------------
        alive_objects = gc.get_objects()
        pr('gc.get_objects()', len(alive_objects))

        with timetracer('heavy proc'):
            self._heavy_proc()

        alive_objects = gc.get_objects()
        pr('gc.get_objects()', len(alive_objects))

    def _heavy_proc(self, count=100000) -> None:
        self._data_list = [self._generate_password() for _ in range(count)]

    def _generate_password(self, nbytes=32) -> str:
        return ''.join(secrets.choice(self._characters) for _ in range(nbytes))


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
