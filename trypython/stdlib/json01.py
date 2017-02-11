# coding: utf-8

"""
jsonモジュールについてのサンプルです。
"""
import json
import pathlib

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        #
        # jsonモジュールには load() と dump() がある
        # また、文字列で処理するための loads(), dumps() もある
        #
        file_path = pathlib.Path('sample01.json')

        with open(file_path) as fp:
            json_object = json.load(fp)
            pr('json', json_object)

        languages = json_object['languages']
        pr('language', [item['language']['name'] for item in languages])


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
