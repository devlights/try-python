"""
dataclasses パッケージに関するサンプルです.

基本的な使い方について

REFERENCES:: http://bit.ly/2KTZynw
             http://bit.ly/2KJCnwk
             http://bit.ly/2KHeNA9
             http://bit.ly/2KFLGxc
"""
import dataclasses as dc

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


@dc.dataclass
class Data1:
    """
    dataclasses.dataclass デコレータを利用すると手軽にデータ型を定義できる。
    仕様は、PEP557 として定義されている。

    普通にクラス定義しても、もちろん同等のものは作れるが dataclass を用いたほうが
    コンストラクタやその他の dunder method も自動的にいい感じに作成してくれるので便利。
    以下のものは自動的に定義される。

    - __init__
    - __repr__
    - __eq__
    """
    name: str
    unit_price: float
    quantity: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity


class Sample(SampleBase):
    def exec(self):
        # dataclass 定義時、フィールドの初期値を設定していないものに関してはコンストラクト時に指定が必要となる
        # quantity フィールドは、初期値を設定しているので設定しなくてもコンストラクト出来る.
        obj = Data1(name='test', unit_price=300.5)
        obj.quantity = 5

        # __repr__ が自動生成されているので見やすい文字列表現が得られる
        pr('obj', obj)
        # もちろん普通のクラスと同様に自分で定義したメソッドも利用可能
        pr('obj.total_cost', obj.total_cost())


def go():
    obj = Sample()
    obj.exec()
