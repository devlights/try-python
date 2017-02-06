# coding: utf-8

"""
ディクショナリについてのサンプルです。
"""
from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        #
        # ディクショナリ初期生成
        #   空のディクショナリを作成するには、{}とするかdict()とする
        #   空のディクショナリは、ifでFalse扱いとなる
        #
        dict1 = {}
        pr('{}で作成', dict1)

        if not dict1:
            pr('{}のif判定', 'False')

        dict1 = dict()
        pr('dict()で作成', dict1)

        if not dict1:
            pr('dict()のif判定', 'False')


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
