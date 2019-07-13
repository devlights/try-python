# coding: utf-8
"""
Python で ディレクトリの削除を行うサンプルです。
"""
import os
import pathlib
import shutil
import tempfile

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


# noinspection PyTypeChecker
class Sample(SampleBase):
    def exec(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            base_dir = pathlib.Path(tmpdir)
            pr('base_dir', base_dir)

            os.mkdir(base_dir / 'test01')
            try:
                # os.remove ではディレクトリは削除できない
                # 中身が空でもダメ
                os.remove(base_dir / 'test01')
            except OSError as e:
                pr('os.remove', e)

            # 中身が空の場合は、rmdir() で削除できる
            os.rmdir(base_dir / 'test01')

            # サブディレクトリも含めて一気に作成
            os.makedirs(base_dir / 'a/b/c/d')

            # サブディレクトリも含めて一気に削除
            # ただし、中身が空の場合のみ
            os.removedirs(base_dir / 'a/b/c/d')

            # ディレクトリ内にコンテンツがあると removedirs() は失敗する
            os.makedirs(base_dir / 'a/b/c')
            print('hello world', file=open(base_dir / 'a/b/c/test.txt', mode='wt'))
            try:
                os.removedirs(base_dir / 'a/b/c')
            except OSError as e:
                pr('os.removedirs', e)

            # shutil.rmtree() はコンテンツがあっても再帰削除してくれる
            shutil.rmtree(base_dir / 'a')


def go():
    obj = Sample()
    obj.exec()
