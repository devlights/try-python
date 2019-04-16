# coding: utf-8

"""
csvモジュールについてのサンプルです。

ファイルに書き込む先に改行が勝手に入ってしまう場合の制御について
"""
import csv
import pathlib

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    # noinspection PyTypeChecker
    def exec(self):
        #
        # csvモジュールを利用してファイルに書き込みを行う場合に
        # open() に newline='' を付与していないと
        # 書込み後のファイルには、自動で改行が一つ多く含まれてしまう。
        #
        csv_path = pathlib.Path.home() / r'csv02.csv'
        if csv_path.exists():
            csv_path.unlink()

        with open(csv_path, mode='wt', encoding='utf-8', newline='') as fp:
            writer = csv.DictWriter(fp, fieldnames=['field1', 'field2'])

            writer.writeheader()
            writer.writerow(dict(field1=100, field2=200))
            writer.writerow(dict(field1=300, field2=400))

        assert csv_path.exists()

        with open(csv_path, mode='rt', encoding='utf-8', newline='') as fp:
            reader = csv.DictReader(fp)

            for row in reader:
                pr('row', row)

        if csv_path.exists():
            csv_path.unlink()


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
