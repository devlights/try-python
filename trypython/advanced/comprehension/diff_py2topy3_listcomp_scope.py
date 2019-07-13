# coding: utf-8
"""
python 2.x 系と 3.x 系にて
内包表記内で使用した一次変数のスコープが異なることを
試すサンプルです。
"""
from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import is_py3, pr


class Sample(SampleBase):
    def exec(self):

        _ = [x for x in range(10)]

        if is_py3():
            # -------------------------------------------
            # python 3.x 系
            #
            # 3.x 系では想定通りの動きをする。
            # 外のスコープから見えない。
            # -------------------------------------------
            try:
                # noinspection PyUnresolvedReferences,PyUnboundLocalVariable
                print(x)
            except NameError as e:
                pr('py3', e)
        else:
            # -------------------------------------------
            # python 2.x 系
            #
            # 2.x 系では内包表記で使用した一次変数が
            # 外のスコープから見える。
            # -------------------------------------------
            # python 2.x 系で試す場合は以下のコメントを外す
            # noinspection PyUnresolvedReferences,PyUnboundLocalVariable
            pr('py2', x)


def go():
    obj = Sample()
    obj.exec()
