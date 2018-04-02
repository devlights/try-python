# coding: utf-8

"""
pathlib モジュールについてのサンプルです。
"""
import pathlib

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        """
        pathlibモジュールについてのサンプル

        pathlibは、3.4から追加されたモジュール。
        システムのパスをオブジェクト指向な形で扱えるようになっている。

        基本パターンは、Path オブジェクトを生成して
        そのメソッドを呼び出すことで操作出来るようになっている

        :return: None
        """

        #
        # Pathオブジェクト生成 (ホームディレクトリ)
        #
        home_dir = pathlib.Path.home()

        #
        # 存在確認
        #
        pr('HOME', home_dir)
        pr('存在するか (HOME)', home_dir.exists())

        #
        # パスを追加
        #   / を使ってパスを追加していける
        #
        anaconda_dir = home_dir / 'anaconda3'
        pr('存在するか (anaconda)', anaconda_dir.exists())
        miniconda_dir = home_dir / 'miniconda3'
        pr('存在するか（miniconda)', miniconda_dir.exists())

        conda_dir = anaconda_dir if anaconda_dir.exists() else miniconda_dir

        #
        # globモジュールのように指定したパターンにマッチするファイルを探す
        #
        pattern = '**/*.pyc'
        file_list = [x for x in conda_dir.glob(pattern)]
        pr('glob結果', len(file_list))

        #
        # rglob メソッドは、recursive glob の意味
        # なので、globを利用する際の **/ の部分はなくても良い。
        #
        pattern = '*.pyc'
        file_list = [x for x in conda_dir.rglob(pattern)]
        pr('rglob結果', len(file_list))


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
