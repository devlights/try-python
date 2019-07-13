# coding: utf-8

"""
collections.Counterについてのサンプルです。
"""
import collections

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        #
        # Counterクラスは辞書ライクに利用できるクラス
        # 便利な点として、クラス名が示す通り
        # 内部でカウントを管理してくれて、トップN位などを
        # 簡単に抽出出来る
        #
        # iterableなものから作成できる
        str01 = 'helloworld'
        counter01 = collections.Counter(str01)
        pr('counter01', counter01)

        list01 = ['hello', 'world', 'hello', 'wold']
        counter02 = collections.Counter(list01)
        pr('counter02', counter02)

        map01 = {'hello': 100, 'world': 200}
        counter03 = collections.Counter(map01)
        pr('counter03', counter03)

        # kwargsを用いた生成
        counter04 = collections.Counter(apple=100, pineapple=200)
        pr('counter04', counter04)

        # 存在しないキーを指定しても例外は発生せず 0 となる
        # collections.defaultdict(int) と同じようなもの
        counter05 = collections.Counter()
        pr('counter05["notexists"]', counter05['notexists'])

        #
        # 最も多い n要素 を返す
        #
        pr('most_common()', counter01.most_common())
        pr('most_common(1)', counter01.most_common(n=1))

        # カウンター同士を + - 出来る
        counter06 = counter01 + counter02
        pr('counter06', counter06)

        #
        # それぞれの要素を、そのカウント分だけ繰り返すイテレータを返す
        #
        pr('elements()', tuple(counter01.elements()))


def go():
    obj = Sample()
    obj.exec()
