# coding: utf-8

"""
csvモジュールについてのサンプルです。
"""
import csv
import io
import tempfile

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


# noinspection PyMethodMayBeStatic
class Sample(SampleBase):
    def exec(self):
        rows = [
            ['hello', 'world'],
            ['こんにちわ', '世界'],
            ['he,llo', 'w,orld']
        ]

        rows2 = [
            {'field1': 'hello', 'field2': 'world'},
            {'field1': 'こんにちわ', 'field2': '世界'},
        ]

        #
        # カンマ区切りファイル (CSV)
        #
        with self.get_file_obj() as fp:
            csvout = csv.writer(fp)
            csvout.writerows(rows)

            fp.seek(io.SEEK_SET)
            pr('fp', fp.read())
            fp.seek(io.SEEK_SET)

            csvin = csv.reader(fp)
            pr('csv', [row for row in csvin])

        #
        # タブ区切りファイル (TSV)
        #
        with self.get_file_obj() as fp:
            csvout = csv.writer(fp, delimiter='\t')
            csvout.writerows(rows)

            fp.seek(io.SEEK_SET)
            pr('fp', fp.read())
            fp.seek(io.SEEK_SET)

            csvin = csv.reader(fp, delimiter='\t')
            pr('tsv', [row for row in csvin])

        #
        # データを dict で扱う
        #   csv.DictReader, csv.DictWriter を利用
        #
        with self.get_file_obj() as fp:
            fieldnames = ['field1', 'field2']

            csvout = csv.DictWriter(fp, fieldnames=fieldnames)
            csvout.writeheader()
            csvout.writerows(rows2)

            fp.seek(io.SEEK_SET)
            pr('fp', fp.read())
            fp.seek(io.SEEK_SET)

            csvin = csv.DictReader(fp)
            pr('dictreader', [row for row in csvin])

    def get_file_obj(self):
        return tempfile.TemporaryFile(mode='w+t', encoding='utf-8')


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
