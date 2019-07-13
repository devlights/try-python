"""
contextlib モジュールについてのサンプルです。
contextlib.redirect_stdout について記載しています。
"""
import io
from contextlib import redirect_stdout

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        """
        contextlib.redirect_stdout についてのサンプルを実行します。
        :return: なし
        """
        # ----------------------------------------------------------------------
        # contextlib.redirect_stdout(new_target)
        #
        # 一時的にsys.stdoutを指定した矛先に向けてくれるコンテキストマネージャ
        # 兄弟関数として、contextlib.redirect_stderr がある。こちらは sys.stderr用
        # ----------------------------------------------------------------------

        # 以下のprint関数は結果をprint関数で出力しているので
        # 通常だと、標準出力に出力されるが redirect_stdout で矛先を変更している
        f = io.StringIO()
        with redirect_stdout(f):
            Sample.tekito()

        pr('f', f.getvalue())

        # 同様に help() は、通常 stdout に結果を出力するが
        # redirect_stdout することで結果を StringIO に格納
        f.seek(io.SEEK_SET)
        with redirect_stdout(f):
            help(sum)
        pr('f', f.getvalue())

    @staticmethod
    def tekito(begin=0, end=10):
        for i in range(begin, end):
            print(i, end=',')


def go():
    """
    サンプルを実行します。
    :return: なし
    """
    obj = Sample()
    obj.exec()
