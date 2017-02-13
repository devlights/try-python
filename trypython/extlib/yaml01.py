# coding: utf-8

"""
pyyamlモジュールについてのサンプルです。
"""
import yaml

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        #
        # python で yaml を扱う場合、標準モジュールには
        # 存在しないので、PyYAMLモジュールを利用する
        #
        with open('sample01.yaml', encoding='utf-8') as fp:
            obj = yaml.load(fp)
            pr('yaml.load()', obj)


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
