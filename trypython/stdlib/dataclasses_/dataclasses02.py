"""
dataclasses モジュールのサンプルです.

fronzen プロパティの指定について

REFERENCESS:: http://bit.ly/2KTZynw
              http://bit.ly/2KJCnwk
              http://bit.ly/2KHeNA9
              http://bit.ly/2KFLGxc
"""
import dataclasses as dc

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


@dc.dataclass(frozen=True)
class Data1:
    name: str
    unit_price: float
    quantity: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity


class Sample(SampleBase):
    def exec(self):
        obj = Data1(name='test', unit_price=300.5)

        try:
            # --------------------------------------------------------
            # frozen 指定している dataclass は値の設定が出来ないようになる.
            # dataclasses.FrozenInstanceError が発生する.
            # --------------------------------------------------------
            # noinspection PyDataclass
            obj.quantity = 5
        except dc.FrozenInstanceError as e:
            pr('frozen な dataclass に値を設定', e)


def go():
    obj = Sample()
    obj.exec()
