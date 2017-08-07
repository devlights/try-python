# coding: utf-8

"""
globals() と locals() のサンプルです。
"""
from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr

# グローバル名前空間で定義した変数は「グローバル変数」となる
global_variable01 = 'hello world from global'


class Sample(SampleBase):
    def exec(self):
        self.access_globalvariable_without_globalcall()
        self.access_globalvariable_with_globalcall()

        #
        # 組み込み関数の locals() と globals() でそれぞれの内容を見ることが出来る
        #
        local_variable = 'local val'
        pr('locals()', locals())
        pr('globals()', globals())

    @staticmethod
    def access_globalvariable_without_globalcall():
        try:
            # ------------------------------------------------------------
            # グローバル変数を見るだけなら可能。
            # 以下の２行のうち、２行目をコメントアウトすると
            # エラーにはならない。
            # ------------------------------------------------------------
            # noinspection PyUnresolvedReferences
            pr('global 無しでグローバル変数にアクセス', global_variable01)
            global_variable01 = 'hello world from func-inside'
        except UnboundLocalError as e:
            pr('global無しでグローバル変数を書き換えようとするとエラーとなる', e)

    @staticmethod
    def access_globalvariable_with_globalcall():
        # ------------------------------------------------------------
        # グローバル変数を利用すると宣言
        # ------------------------------------------------------------
        global global_variable01

        pr('global 呼び出し後にグローバル変数にアクセス', global_variable01)
        global_variable01 = 'hello world from func-inside'
        pr('値変更後', global_variable01)


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
