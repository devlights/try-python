# coding: utf-8

"""
pickleモジュールについてのサンプルです。
"""
import collections
import functools
import os
import pickle

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr

Test02 = collections.namedtuple('Test02', ['val1', 'val2'])


class Sample(SampleBase):
    def exec(self):
        #
        # 何度も呼び出すので使いやすいように保持
        #
        dumps = functools.partial(pickle.dumps, protocol=pickle.HIGHEST_PROTOCOL)
        loads = pickle.loads

        #
        # 数値
        #
        num01 = 123456
        pic01 = dumps(num01)
        pr('dumps-int', pic01, f'{len(pic01)}bytes')
        pr('loads-int', loads(pic01))

        #
        # 文字列 (ascii)
        #
        str01 = "test strings"
        pic02 = dumps(str01)
        pr('dumps-str', pic02, f'{len(pic02)}bytes')
        pr('loads-str', loads(pic02))

        #
        # 文字列 (utf-8)
        #
        str02 = "テスト文字列"
        pic03 = dumps(str02)
        pr('dumps-str', pic03, f'{len(pic03)}bytes')
        pr('loads-str', loads(pic03))

        #
        # リスト
        #
        lst01 = list(range(10))
        pic04 = dumps(lst01)
        pr('dumps-list', pic04, f'{len(pic04)}bytes')
        pr('loads-list', loads(pic04))

        #
        # 辞書
        #
        dict01 = dict(apple=100, pineapple=200)
        pic05 = dumps(dict01)
        pr('dumps-dict', pic05, f'{len(pic05)}bytes')
        pr('loads-dict', loads(pic05))

        #
        # 名前付きタプル
        #
        try:
            #
            # 名前付きタプルを関数内で定義して直列化しようとすると
            # エラーとなる。原因は以下に記載されている
            #   http://stackoverflow.com/questions/16377215/how-to-pickle-a-namedtuple-instance-correctly
            #
            Test01 = collections.namedtuple('Test01', ['val1', 'val2'])
            namedtuple01 = Test01(val1=100, val2=200)
            pic06 = dumps(namedtuple01)
            pr('dumps-namedtuple', pic06, f'{len(pic06)}bytes')
            pr('loads-namedtuple', loads(pic06))
        except pickle.PickleError as pickleEx:
            pr('error-at-namedtuple01', pickleEx)

        #
        # グローバルなエリアで定義しておいた名前付きタプル
        #
        namedtuple02 = Test02(val1=100, val2=200)
        pic07 = dumps(namedtuple02)
        pr('dumps-namedtuple', pic07, f'{len(pic07)}bytes')
        pr('loads-namedtuple', loads(pic07))

        #
        # 集合
        #
        set01 = set(range(10))
        pic08 = dumps(set01)
        pr('dumps-set', pic08, f'{len(pic08)}bytes')
        pr('loads-set', loads(pic08))

        #
        # クラス
        #
        cls01 = ForPickle()
        pic09 = dumps(cls01)
        pr('dumps-cls', pic09, f'{len(pic09)}bytes')
        pr('loads-cls', loads(pic09))


class ForPickle:
    def __init__(self):
        super().__init__()
        self._num = 100
        self._str = 'hello world'
        self._lst = list(range(5))
        self._dict = dict(A=1, B=2)
        self._set = set(range(5, 5))
        self._namedtuple = Test02(val1=100, val2=10)

    def __str__(self, *args, **kwargs):
        return f',{os.linesep}'.join([f'({k}={v})' for k, v in self.__dict__.items()])

    def __repr__(self, *args, **kwargs):
        return self.__str__(self, args, kwargs)


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
