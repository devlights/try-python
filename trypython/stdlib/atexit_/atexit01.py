# coding: utf-8

"""
atexitモジュールについてのサンプルです。
"""
import atexit
import sys

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        #
        # atexitモジュールを利用するとシャットダウンフックを設定出来る
        # register() で登録して、 unregister() で解除する
        #
        # 引数無しの関数に限り、@atexit.register という風にデコレータで
        # 指定できる。
        #
        atexit.register(Sample.exit_hook)
        pr('script', 'end')
        sys.exit(0)

    @staticmethod
    def exit_hook():
        pr('exit_hook', 'called')

    @staticmethod
    @atexit.register
    def exit_hook2():
        pr('exit_hook2', 'called')


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
