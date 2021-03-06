# coding: utf-8

"""
セットについてのサンプルです。
"""
from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        #
        # セット（集合）
        # セットは文字通り「集合」を表す
        # 特徴は
        #   ・値の順序は不定
        #   ・値は一意（リストと異なり同じ値を複数持てない）
        #   ・集合演算可能
        # イメージ的にはディクショナリのキーだけの順序不定リストなイメージ
        # 集合は「何かがあるかどうか」ということが分かれば良いという場合に利用できる
        #
        # 集合を作成するには、set() か {値1, 値2,...値N} を利用する
        # set() とすると空集合が作成できるが、{} とすると空のディクショナリが作成されてしまう。
        #
        set01 = set()
        pr('空集合', set01)

        set01 = {1, 2, 3, 4, 5}
        pr('集合', set01)  # ここでの表示にて 数値の順番 異なるかもしれないが集合は順序を持たない

        #
        # 他のデータ型から集合への変換
        #
        lists = list(range(10))
        set02 = set(lists)

        pr('他のデータ型から集合の生成', set02)

        lists.extend(list(range(20)))
        set02 = set(lists)

        pr('集合生成元リスト', lists)
        pr('重複する値は一つになる', set02)

        #
        # 値が存在するか
        #
        pr('11が存在するか', 11 in set02)

        ################################
        # 集合演算
        ################################
        #
        # 積集合
        # 積集合は、両方の集合に含まれているものがヒットする
        # 積集合を求めるには、 & か intersection() を利用する
        #
        set03 = {17, 18, 99}
        pr('積集合', set02 & set03)

        #
        # 和集合
        # 和集合は、どちらかの集合に含まれているものがヒットする
        # 和集合を求めるには、 | か union() を利用する
        #
        set04 = {1, 2, 98, 99}
        pr('和集合', set03 | set04)

        #
        # 差集合
        # 差集合は、左側には存在するが、右側には存在しないものがヒットする
        # 差集合を求めるには、 - か difference() を利用する
        #
        pr('差集合', set03 - set04)

        #
        # 排他的論理和 (排他的OR)
        # 排他的論理和は、どちらか片方に含まれているが、両方には含まれていないものがヒットする
        # 排他的論理和を求めるには、 ^ か symmetric_difference() を利用する
        #
        pr('排他的論理和', set03 ^ set04)

        #
        # サブセット（部分集合）
        # サブセットは、片方の集合がもう片方の集合をすっぽり含む場合のことをいう
        # サブセットかどうかを求めるには、 <= か issubset() を利用する
        # <= の部分を < にすると「真部分集合」となる。
        # 第一の集合が第二の集合の真部分集合になるためには、第二の集合は第一の集合の
        # 全要素に加えて別の要素を持っていなければならない.
        #
        set05 = {1, 2, 99}
        pr('set05はset04の部分集合', set05 <= set04)
        pr('set05はset04の真部分集合', set05 < set04)

        #
        # スーパーセット (上位集合)
        # スーパーセットは、サブセットの逆。
        # スーパーセットかどうかを求めるには、 >= か issuperset() を利用する
        # >= の部分を > にすると「真上位集合」となる
        #
        pr('set04はset05の上位集合', set04 >= set05)
        pr('set04はset05の真上位集合', set04 > set05)


def go():
    obj = Sample()
    obj.exec()
