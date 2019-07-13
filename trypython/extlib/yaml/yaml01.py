# coding: utf-8

"""
pyyamlモジュールについてのサンプルです。
"""
import io

import yaml

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr

YAML_TEXT = """\
# コメント

# 辞書の中にリスト
mydata1:
  - hello
  - world

mydata2:
  # リストの中に辞書
  - key1: hello
    key2: world
  - key3: hehe
    key4: hoge
"""


class Sample(SampleBase):
    def exec(self):
        #
        # python で yaml を扱う場合、標準モジュールには
        # 存在しないので、PyYAMLモジュールを利用する
        #
        with io.StringIO(YAML_TEXT) as fp:
            obj = yaml.load(fp, Loader=yaml.SafeLoader)
            pr('yaml.load()', obj)


def go():
    obj = Sample()
    obj.exec()
