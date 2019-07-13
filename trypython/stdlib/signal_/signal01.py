"""
signal モジュールのサンプル

signal.signal(SIGINT) の使い方について。
CTRL-C をハンドルする。

注意点:: 本サンプルはPyCharmから実行してもうまく動きません。
        ターミナルから python -m trypython.stdlib.signal_.signal01 で
        実行してください。

REFERENCES:: http://bit.ly/2Y4dxt2
             http://bit.ly/2XYnqso
"""
import signal
import time

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        # コンソール上での CTRL-C をハンドルする
        signal.signal(signal.SIGINT, self.handler)
        pr("signal handling start....", signal.SIGINT)
        time.sleep(10)
        pr("signal handling end", signal.SIGINT)

    @staticmethod
    def handler(signal_number, stack_frame):
        pr("signal_number", signal_number)
        pr("stack_frame", stack_frame)
        pr("dir(stack_frame)", [x for x in dir(stack_frame) if x.startswith("f")])


def go():
    obj = Sample()
    obj.exec()
