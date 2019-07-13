"""
yaml についてのサンプルです.

YAML とは、構造化されたデータを表現するためのフォーマット。
目的は XML と似ているが、XML と比べて「読みやすい」「書きやすい」「分かりやすい」
という利点がある。

Python において、 YAML は標準モジュールには搭載されていないので
PyYaml ライブラリを利用する。PyYamlライブラリは モジュール名は yaml なのに注意。

YAML は、 YAML Ain't Markup Language の略。

YAML の正式な仕様書は以下にある。
- https://yaml.org/spec/current.html

REFERENCES:: http://bit.ly/2K1pg7N
             http://bit.ly/2HNtw86
"""
import io

import yaml

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr

YAML_TEXT = """\
# 配列にて 「半角スペース」 でインデントすると
# 配列をネストさせることが出来る。タブ文字は使えない。
- array1
- 
  - array2-1
  - array2-2
  - 
    - array3-1
    - array3-2
- array4
"""


class Sample(SampleBase):
    def exec(self):
        with io.StringIO(YAML_TEXT) as fp:
            yaml_obj = yaml.load(fp, Loader=yaml.SafeLoader)
            pr('yaml_obj', yaml_obj)
            pr('type(yaml_obj)', type(yaml_obj))

            pr('array2', yaml_obj[1])
            pr('array3', yaml_obj[1][2])


def go():
    obj = Sample()
    obj.exec()
