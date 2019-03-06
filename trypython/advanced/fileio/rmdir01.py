# coding: utf-8
"""
Python で ディレクトリの削除を行うサンプルです。
"""
import os
import shutil

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


# noinspection PyTypeChecker
class Sample(SampleBase):
    def exec(self):
        os.mkdir('/tmp/test01')
        try:
            # os.remove ではディレクトリは削除できない
            # 中身が空でもダメ
            os.remove('/tmp/test01')
        except OSError as e:
            pr('os.remove', e)

        # 中身が空の場合は、rmdir() で削除できる
        os.rmdir('/tmp/test01')

        # サブディレクトリも含めて一気に作成
        os.makedirs('/tmp/a/b/c/d')

        # サブディレクトリも含めて一気に削除
        # ただし、中身が空の場合のみ
        os.removedirs('/tmp/a/b/c/d')

        # ディレクトリ内にコンテンツがあると removedirs() は失敗する
        os.makedirs('/tmp/a/b/c')
        print('hello world', file=open('/tmp/a/b/c/test.txt', mode='wt'))
        try:
            os.removedirs('/tmp/a/b/c')
        except OSError as e:
            pr('os.removedirs', e)

        # shutil.rmtree() はコンテンツがあっても再帰削除してくれる
        shutil.rmtree('/tmp/a')


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
