"""
icecream ライブラリのサンプル

REFERENCES::
https://github.com/gruns/icecream
"""
import collections
import contextlib as ctx
import datetime

from icecream import ic

from trypython.common.commoncls import SampleBase


class Sample(SampleBase):

    def exec(self):
        """サンプル用の処理を実行します"""
        ###############################################
        # icecream
        # ---------------------------------------------
        # icecream はデバッグ時によく利用する print 出力を
        # もっと便利にしてくれるライブラリ。
        # 使い方については、github の README.md に記載されて
        # いるので、だいたい分かる。
        # 以下、基本的な使い方をメモしたもの。
        ###############################################
        #
        # (1) print(f'hoge={hoge}') の代わり
        # ---------------------------------------------
        # よくデバッグ時に上記のように出力入れたりするが
        # icecream だと以下のように書ける
        #   ic(hoge)
        # これだけで、"ic| hoge: hoge"と出力してくれる
        #
        hello = 'world'
        ic(hello)  # ic| hello: 'world'

        # リストの場合
        l01 = list(range(10))
        ic(l01[-1])  # ic| l01[-1]: 9

        # 辞書の場合
        d01 = dict(zip(['apple', 'banana'], [100, 200]))
        ic(d01['apple'])  # ic| d01['apple']: 100

        # 集合の場合
        s01 = set(range(10))
        ic(s01.pop())  # ic| s01.pop(): 0

        # 独自オブジェクトの場合
        Data1 = collections.namedtuple('Data1', ['x', 'y'])
        dat1 = Data1(100, 200)
        ic(dat1)  # ic| dat1: Data1(x=100, y=200)

        #
        # (2) print(1) のような通過確認用ログの代わり
        # ---------------------------------------------
        # よくデバッグ時に上記のように「この場所を通ったか？」の
        # 確認用出力を入れたりするが
        # icecream だと以下のように書ける
        #   ic()
        # これだけで、"ic| icecream_sample.py:10"と出力してくれる
        #
        def debug_print():
            print(0)
            # 何か処理....
            print(1)
            # 何か処理....
            print(2)

        def debug_ic():
            ic()
            # 何か処理....
            ic()
            # 何か処理....
            ic()

        debug_print()
        debug_ic()

        # ただし、この状態ではソースファイルと行番号しか出せない
        # 「コネクション確保」とかみたいな補助情報も出力したい場合は
        # 以下のように includeContext を True に設定する
        def debug_ic2():
            ic.includeContext = True
            conn = None
            ic(conn)
            # 何か処理
            conn = dat1
            ic(conn)
            ic.includeContext = False

        debug_ic2()

        # 以下のように with で一時的なスイッチできるようにした方が使いやすいかも
        @ctx.contextmanager
        def context_on():
            old = ic.includeContext
            ic.includeContext = True
            yield
            ic.includeContext = old

        def debug_ic3():
            with context_on():
                conn = None
                ic(conn)
                # 何か処理
                conn = dat1
                ic(conn)
            ic()

        debug_ic3()

        #
        # (3) ic() は引数の値をそのまま返してくれる
        # ---------------------------------------------
        # なので、関数の引数に渡すついでにログ出力なども出来る
        #
        def tekito(x, y):
            return x + y

        x = 10
        y = 20
        tekito(ic(x), ic(y))

        #
        # (4) ic.disable()/enable()で有効無効を切り替え可能
        # ---------------------------------------------
        #
        @ctx.contextmanager
        def ic_off():
            ic.disable()
            try:
                yield
            finally:
                ic.enable()

        with ic_off():
            ic('これは出力されない')

        #
        # (5) prefix(ic|って出てる部分)を変更可能
        # ---------------------------------------------
        # ic.configureOutput(prefix=xx) で変更できる
        # prefix=xxの部分には関数も指定可能。
        # 現在のprefixは、ic.prefixで取得できる
        #
        def yyyymmddhhmiss():
            d = datetime.datetime.now()
            s = d.strftime('%Y/%m/%d %H:%M:%S')
            return f'{s} |> '

        @ctx.contextmanager
        def datetime_prefix_on():
            old = ic.prefix
            try:
                ic.configureOutput(prefix=yyyymmddhhmiss)
                yield
            finally:
                ic.prefix = old

        with datetime_prefix_on():
            ic()
            ic(dat1)
            ic()

        #
        # ic.configureOutput()には、他にも
        # 出力処理を指定できる outputFunction や
        # 引数の値を文字列にする際に呼ばれる argToStringFunction が
        # 指定できる
        #

        # 割愛
        # https://github.com/gruns/icecream 参照


def go():
    """処理を実行します"""
    obj = Sample()
    obj.exec()
