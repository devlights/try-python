# coding: utf-8

"""
collections.dequeについてのサンプルです。
"""
import collections

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        #
        # collections.deque() は 両端キューの事。
        # deque は 「Double-Ended-Queue」の略。
        # 左にも右にも要素が追加できて、取り出しも出来る
        # 計算量として、どちらの方向からも O(1) で処理可能
        # ただし、これは両端のアクセスが O(1) なので
        # 中央部分は O(n) となる。ランダムアクセスが必要であれば
        # リストを利用するべきとのこと。
        #
        # https://docs.python.jp/3/library/collections.html#collections.deque
        #
        deque01 = collections.deque(iterable=range(10, 15))

        #
        # 左右にappend
        #
        deque01.append(1)
        deque01.appendleft(2)

        #
        # 左右からpop
        #
        pr('deque01', deque01)
        pr('pop()', deque01.pop())
        pr('popleft()', deque01.popleft())
        pr('deque01', deque01)

        #
        # rotate() は指定された数分、右に循環させる
        # 負の値を指定すると左に循環する
        #
        deque01.rotate()
        pr('rotate()', deque01)

        deque01.rotate(-1)
        pr('rotate(-1)', deque01)

        deque01.rotate(3)
        pr('rotate(3)', deque01)

        #
        # dequeの特徴として、生成時に maxlen を指定すると
        # 最大長が決まった deque となり、要素がフルの場合に
        # 新しく要素を追加すると、追加した側の反対側から要素
        # が捨てられる。
        #
        # つまり、右に要素を追加すると左側から要素が捨てられ
        # 左に要素を追加すると右側から要素が捨てられる。
        #
        deque02 = collections.deque(maxlen=3)

        pr('deque02', deque02)
        deque02.extend(range(1, 4))
        pr('deque02', deque02)
        deque02.append(100)
        pr('deque02', deque02)
        deque02.append(200)
        pr('deque02', deque02)
        deque02.appendleft(300)
        pr('deque02', deque02)


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
