"""
sys.getsizeof() と __sizeof__() で 返される値が異なる時があるのを確認するサンプル

REFERENCES:: http://bit.ly/2GTVkbs
"""
import sys

from trypython.common.commoncls import SampleBase


class Sample(SampleBase):
    def exec(self):
        # sys.getsizeof() は GC フィールドの分を加算するので
        # __sizeof__() が返す値と異なるときがある
        list_data = [10, 20]
        sys_sizeof = sys.getsizeof(list_data)
        dunder_sizeof = list_data.__sizeof__()

        self._print(type(list_data), sys_sizeof, dunder_sizeof)

        # 同じものもある
        str_data = "hello world"
        sys_sizeof = sys.getsizeof(str_data)
        dunder_sizeof = str_data.__sizeof__()

        self._print(type(str_data), sys_sizeof, dunder_sizeof)

        int_data = 1_000_000_000
        sys_sizeof = sys.getsizeof(int_data)
        dunder_sizeof = int_data.__sizeof__()

        self._print(type(int_data), sys_sizeof, dunder_sizeof)

    # noinspection PyMethodMayBeStatic
    def _print(self, t: type, sys_sizeof: int, dunder_sizeof: int):
        print(f'{t}:\tsys.getsizeof: {sys_sizeof}\tdunder_sizeof: {dunder_sizeof}')


def go():
    obj = Sample()
    obj.exec()
