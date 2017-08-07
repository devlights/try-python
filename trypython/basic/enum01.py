# coding: utf-8

"""
enumについてのサンプルです。
"""
from enum import Enum, unique

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


@unique
class Fruit(Enum):
    """
    PythonにてEnumを定義する場合以下のようにする。

    ・Enumクラスをベースクラスにしたクラスを作成
    ・クラスフィールドとして各列挙値を定義
    ・各Enumメンバーが持つ値を一意に制限するにはuniqueデコレータを付与
    """
    Apple = 1
    Strawberry = 2
    Banana = 3
    Cherry = 4


class Sample(SampleBase):
    def exec(self):
        val = Fruit.Apple
        self.show_enum_value(val)

    def show_enum_value(self, val: Fruit) -> None:
        pr('val', val)
        pr('Apple?', val == Fruit.Apple)
        pr('Strawberry?', val == Fruit.Strawberry)
        pr('Banana?', val == Fruit.Banana)
        pr('Cherry?', val == Fruit.Cherry)


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
