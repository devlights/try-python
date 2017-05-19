# coding: utf-8
"""
itertools モジュールについてのサンプル

以下の処理についてのサンプルです。

- count()
- accumulate()
- compress()
- dropwhile()
- filterfalse()
"""
import itertools as it
import operator as op

from common.commoncls import SampleBase
from common.commonfunc import pr, hr


class Sample(SampleBase):
    def exec(self):
        # -----------------------------------------------
        # itertools.count()
        # ----------------------
        # 無限イテレータ。
        # 指定した start 値から step 分加算した値を
        # 生成し続ける。
        # -----------------------------------------------
        hr('itertools.count()')

        iter01 = it.count(start=10, step=2)
        for i in iter01:
            if i > 20:
                break
            pr('it.count', i)

        # -----------------------------------------------
        # itertools.accumulate()
        # ----------------------
        # 指定した関数の結果を累積した結果を返す。
        # 汎用性が高い関数。seed は指定できない。
        # 最終的な累積結果のみが欲しい場合はfunctools.reduce() を使う。
        # -----------------------------------------------
        hr('itertools.accumulate()')

        data01 = [1, 2, 3, 4, 5]

        # 加算
        pr('it.accumulate', list(it.accumulate(data01, op.add)))
        # 乗算
        pr('it.accumulate', list(it.accumulate(data01, op.mul)))

        # 自前関数
        def _accum(accum: int, curr: int) -> int:
            return accum * curr if accum < 20 else 20

        pr('it.accumulate', list(it.accumulate(data01, func=_accum)))

        # -----------------------------------------------
        # itertools.compress()
        # ----------------------
        # 引数に指定されたシーケンスを第二引数で指定したリスト
        # 内でTrueとなっているもののみにフィルタリングする。
        # 注意点として、zip関数と同様に短い方が終了した
        # 段階で処理が打ち切られる。
        # -----------------------------------------------
        hr('itertools.compress()')

        selector01 = [True if x >= 3 else False for x in data01]
        pr('it.compress', list(it.compress(data01, selectors=selector01)))

        # -----------------------------------------------
        # itertools.dropwhile()
        # ----------------------
        # 条件が成り立つ間、要素を捨てる。
        # 条件が成り立たなくなってからの要素が返る。
        # 他の言語では、SkipWhile() という名前になったりする。
        # 第一引数が predicate つまり、条件。
        # 第二引数が データ であることに注意。
        # -----------------------------------------------
        hr('itertools.dropwhile()')
        pr('it.dropwhile', list(it.dropwhile(lambda x: x < 3, data01)))

        # -----------------------------------------------
        # itertools.filterfalse()
        # ----------------------
        # ちょっと特殊な子で、条件がfalseとなるものが返る。
        # predicate に None が指定できる。Noneを指定した
        # 場合は、データの要素が false 判定されたものが返る。
        # 第一引数が predicate つまり、条件。
        # 第二引数が データ であることに注意。
        # -----------------------------------------------
        hr('itertools.filterfalse()')
        pr('it.filterfalse', list(it.filterfalse(lambda x: x < 3, data01)))

        # ----------------------------------------------------------------------------
        # 上の dropwhile と filterfalse では同じ条件を指定している。
        # dropwhile は predicate が True の要素は飛ばして、falseになってから要素を返す。
        # filterfalse は predicate が false の要素を返す。
        # つまり、上の2つは対象データが[1, 2, 3, 4, 5]の場合は、同じ結果となる。
        #
        # 違いが出るのは、一旦 True なデータが出現した後に 再度 false データが出現した場合
        #
        # dropwhile() は、一度 True になった後は、以降のデータは無条件で全部返る。
        # filterfalse() は、false の判定になったものしか返さない。
        # ----------------------------------------------------------------------------
        hr('difference between dropwhile() and filterfalse()')
        data02 = [*data01, 2, 1, 3, 4, 5]
        pr('it.dropwhile', list(it.dropwhile(lambda x: x < 3, data02)))
        pr('it.filterfalse', list(it.filterfalse(lambda x: x < 3, data02)))


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
