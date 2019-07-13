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
# YAML では主に以下の3つの組み合わせでデータを表現する
#   - 配列
#   - ハッシュ (辞書)
#   - スカラー
# 以下は 配列 のサンプル

# YAML では 行頭に「-」を付けることで配列を表現する
- Python
- Ruby
- Java

"""


class Sample(SampleBase):
    def exec(self):
        with io.StringIO(YAML_TEXT) as fp:
            yaml_obj = yaml.load(fp, Loader=yaml.SafeLoader)

            pr('yaml_obj', yaml_obj)
            pr('type(yaml_obj)', type(yaml_obj))

            for item in yaml_obj:
                pr('\titem', item)


def go():
    obj = Sample()
    obj.exec()
