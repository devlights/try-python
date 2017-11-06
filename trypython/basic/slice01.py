# coding: utf-8
"""
slice 関数についてのサンプルです。
"""
import itertools

from trypython.common.commoncls import SampleBase


class Sample(SampleBase):
    def exec(self):
        #############################################################
        # slice 関数
        #   - https://docs.python.jp/3/library/functions.html#slice
        #
        # slice 関数は、インデックスの集合を表すオブジェクトを生成し返す.
        # 取得した slice オブジェクトはシーケンスの添字として利用できる.
        #############################################################
        l = list(range(10))

        # インデックス2番目から4番目までの要素を取得
        print(l[2:4])

        # slice オブジェクト取得
        # 生成した slice オブジェクトはシーケンスの添字として利用可能
        # 名前が付けられるので、sequence[x:y:z]とするよりわかりやすい
        from_two_to_four = slice(2, 4)
        print(type(from_two_to_four))
        print(l[from_two_to_four])
        print('helloworld'[from_two_to_four])

        # slice 関数に渡す引数は、前から start, stop, step となっている
        step_two = slice(None, None, 2)
        print('helloworld'[step_two])

        # イテレータに対しては、itertools.islice を使う
        it = iter(l)
        iter_from_two_to_end_step_two = itertools.islice(it, 0, None, 2)
        print([x for x in iter_from_two_to_end_step_two])


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
