# coding: utf-8
"""
weakref モジュールについてのサンプルです。
weakref.finalize() についてのサンプルコードが記載されています。
"""
import time
import weakref

from trypython.common.commoncls import SampleBase


class Sample(SampleBase):
    def exec(self):
        print(f'処理開始')
        time.sleep(3)
        print(f'処理終了')


def finalize_sample(*args, **kwargs):
    print(f'object [sample] is dead. \n\targs   = {tuple(args)}\n\tkwargs = {kwargs}')


def go():
    obj = Sample()

    #################################################################
    # ファイナライザを設定して実行
    #
    # finalize() の書式は (obj, func, *args, **kwargs) となっており
    # 設定時に指定した *args, **kwargs が、ファイナライザに引き渡される
    #################################################################
    weakref.finalize(obj, finalize_sample, 999, keyword1='helloworld')
    obj.exec()


if __name__ == '__main__':
    go()

    ###################################################################################
    # go() が終了した段階で Sample オブジェクトの参照数が0となるので、オブジェクトが gc される
    # (python の gc は、メインルーチンに参照カウンタ方式なので、即削除される (*1))
    # ので、設定していたファイナライザが発動する
    #
    # (*1) 循環参照を検出するために 世代間GC もやっている
    ###################################################################################
    print(f'メインルーチン終了')
