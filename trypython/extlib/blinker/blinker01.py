"""
イベントディスパッチライブラリ blinker のサンプルです。
基本的な signal の使い方について。

REFERENCES::
https://github.com/jek/blinker
https://pythonhosted.org/blinker/
"""
import blinker as bl

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import hr


class Sample(SampleBase):
    """Blinker の基本的な使い方について"""

    def exec(self):
        """サンプル処理を実行します。"""
        # --------------------------------------------------------------
        # blinker は、イベント通知を行ってくれるライブラリ。
        # 使い方がシンプルで速いのが特徴。
        # Observerパターンを利用したい場合に有効。
        #
        # blinker では、まず最初に signal() でシグナルを作成する。
        # signal は、好きに命名することが可能
        # 通知を受けるためには、 connect メソッドでアタッチする。
        # あとは、 send メソッドで値を送信するたびにアタッチされたハンドラに通知が発行される。
        # --------------------------------------------------------------
        my_signal = bl.signal('my-signal')

        # sender を指定しない場合は ブロードキャスト 扱いとなる。
        # つまり、この signal で発行されたすべての値を受け取ることが出来る。
        my_signal.connect(self.print_message)

        hr('broadcast')

        for i in range(5):
            my_signal.send(i)

        hr('broadcast + filtering')

        # sender を指定している場合、値に合致したイベントのみが通知される。
        my_signal.connect(self.print_message2, sender=3)

        for i in range(5):
            my_signal.send(i)

    @staticmethod
    def print_message(message):
        print(f'notify signal [{message}]')

    @staticmethod
    def print_message2(message):
        print(f'notify signal 2 [{message}]')


def go():
    obj = Sample()
    obj.exec()
