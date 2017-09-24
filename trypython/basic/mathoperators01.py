# coding: utf-8
"""
Pythonの数学演算子についてのサンプルです。
"""
from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        # ---------------------------------------
        # 加算
        # ---------------------------------------
        pr('add', 2 + 3)

        # ---------------------------------------
        # 減算
        # ---------------------------------------
        pr('sub', 5 - 3)

        # ---------------------------------------
        # 乗算
        # ---------------------------------------
        pr('mul', 2 * 3)

        # ---------------------------------------
        # 除算
        # pythonには除算に２つのやり方がある
        # 「/」は、結果をfloatで返す
        # 「//」は、結果をintで返す
        # ---------------------------------------
        pr('div1', 4 / 2)
        pr('div2', 4 // 2)

        # ---------------------------------------
        # 累乗
        # ---------------------------------------
        pr('pow', 2 ** 3)

        # ---------------------------------------
        # 剰余
        # ---------------------------------------
        pr('surplus', 5 % 2)


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()