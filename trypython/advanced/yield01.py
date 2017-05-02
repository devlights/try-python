# coding: utf-8
"""yieldについてのサンプルです。
元ネタは、stackoverflowの以下のページ。

https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do-in-python/231855#231855

回答がとてもわかり易いので、自分用のメモとしても残しておく。
"""
import time
from datetime import datetime

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        # ----------------------------------------------------------
        # [元ネタ]
        # https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do-in-python/231855#231855
        #
        # 以下は、元ネタのページ内の記載を自分なりに理解した内容メモです。
        # ----------------------------------------------------------

        # ----------------------------------------------------------
        # 前書き
        # --------------
        # yield が何を行っているのかを理解するためには
        # まず generator が何なのかを理解する必要があります。
        # なので、generator の前に iterable から理解していきます。
        # ----------------------------------------------------------

        # ----------------------------------------------------------
        # Iterable
        # --------------
        # list を生成すると、１つずつ要素を読み出すことが出来ます。
        # 一つずつ、要素を読み出すことを「イテレーション」といいます。
        # ----------------------------------------------------------
        list01 = list(range(5))
        for i in list01:
            pr('list-item', i)

        # ----------------------------------------------------------
        # list01 は、iterable です。
        # リスト内包表記(list comprehension)を使ったとき
        # リストが生成され、これも iterable なものとなります。
        # ----------------------------------------------------------
        list02 = [x * 2 for x in range(5)]
        for i in list02:
            pr('list-item(list comprehension)', i)

        # ----------------------------------------------------------
        # for ... in ... は、iterableなもの全てに使えます。
        # (リストや文字列や辞書や集合やファイルなど・・・）
        #
        # このように iterable なオブジェクトはとても使いやすく便利
        # なのですが、全ての値をメモリに保持してしまうという面も持っています。
        #
        # 例えば、大量なデータを持つリストなどです。このような時
        # 実際に全てのデータが必要では無い場合もあります。
        # 利用しないデータの割合が多い場合、多くは不必要にメモリにロードされ
        # 空きメモリを圧迫します。このような場合に generator が登場します。
        # ----------------------------------------------------------

        # ----------------------------------------------------------
        # Generators
        # --------------
        # Generators は イテレータです。(iterator => iterate するもの)
        # でも、一回しかイテレートすることが出来ません。
        # (つまり、一回全要素をループさせると終わり)
        #
        # これは、generatorが一度に全ての要素をメモリに持つのではなく
        # 必要な要素をその都度 (on the fly) 生成するからです。
        #
        # なので、generator (generate するもの) となります。
        #
        # generator を生成する場合、() で生成部分を囲みます。
        # 先ほどのリスト内包表記を generator に変更する場合
        # [] を () に変えるだけで generator になります。
        # ----------------------------------------------------------
        gen01 = (x * 2 for x in range(5))
        pr('generator-object', gen01)

        for i in gen01:
            pr('generator-item(first-loop)', i)
        else:
            pr('first-loop', 'done')

        for i in gen01:
            pr('generator-item(second-loop)', i)
        else:
            pr('second-loop', 'done')

        # ----------------------------------------------------------
        # Yield
        # --------------
        # ここでやっと、yield の登場です。
        # yield は return のような感じで使います。
        # return は、値を返しますが、yield は generator を返します。
        #
        # とりあえず、以下に yield のサンプルを記載します。
        # 下記を実行すると、５回値を生成します。
        # ----------------------------------------------------------
        def create_generator():
            yield 1
            yield 2
            yield 3
            yield 4
            yield 5

        gen02 = create_generator()
        pr('generator-object', gen02)

        for x in gen02:
            pr('generator-item', x)

        # -----------------------------------------------------------------------
        # 上記の create_generator 関数では yield が5回登場しています。
        # なので、取得した generator をループすると 5回値が出力されます。
        #
        # このように書くと、なんとなく分かるけど、なんとなく分からないって
        # なってしまうのが、yield のややこしいところです。
        #
        # 大事なのが、以下の点です。
        # 「関数内に yield が存在すると、python は 関数本体を実行せずに
        # generator を生成して、呼び元に返す。」
        #
        # 内部に yield が利用されている関数は、呼ぶとすぐには実行されません。
        # generator オブジェクトが生成されて、それが返ってきます。
        #
        # なので、
        #   gen02 = create_generator()
        # と書くと、create_generator関数の中では yield があるので
        # python が内部で generator を生成して返してくれます。
        # それが 変数 gen02 にセットされます。
        #
        # generator は イテレートさせないと処理が進みません。
        # (厳密にいうと、next() が呼ばれない限り。コルーチンの場合は send() されない限り）
        # 呼び出される度（つまり一回分イテレートされるたび）に、yield一つ分進み、次の
        # yield が見つかったタイミングで一時停止します。
        #
        # なので、上のサンプルでは ループが一回進む度に yield も一つずつ進んでいって
        # 最終的に yield が5回分呼ばれたらループ終了となります。(StopIterationが発生します。)
        #
        # 一度使い切った generator は利用できないので、上記サンプルの gen02 を
        # 再度 for 文で利用しても、今度は一回もループされません。
        # (yield 5 まで進んでしまっているので、次の yield がもうないため）
        #
        # yield の動き自体はシンプルなので、以下のように無限ループの中で yield すると
        # 止めない限り、永遠に値を生成するようにも出来ます。
        # ------------------------------------------------------------------------
        def gen_forever():
            while True:
                yield datetime.now()

        gen03 = gen_forever()
        for i, d in enumerate(gen03):
            if i > 5:
                break
            pr('gen03', d.isoformat())
            time.sleep(1)


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
