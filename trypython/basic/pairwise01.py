"""
特定のリストのデータを 対 (Pairwise) で処理したい場合のサンプルです。

参考：
https://twitter.com/raymondh/status/967927989752098816?s=12
"""
from trypython.common.commoncls import SampleBase


class Sample(SampleBase):
    def exec(self):
        data = list(range(10))

        for first, second in zip(data, data[1:]):
            print(first, second)


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
