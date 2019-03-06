# coding: utf-8
"""
tkinter の messagebox を使用するサンプルです。
"""
from datetime import datetime
from functools import wraps
from time import sleep
from tkinter import Tk, messagebox

from trypython.common.commoncls import SampleBase


def show_complete_dialog(func):
    @wraps(func)
    def _wrapper(*args, **kwargs):
        results = func(*args, **kwargs)
        message = f'{func.__name__} is DONE at {datetime.now()}'

        root = Tk()
        root.withdraw()
        messagebox.showinfo('DONE', message)
        root.quit()

        return results

    return _wrapper


class Sample(SampleBase):
    def exec(self):
        #############################################################
        #
        # 内容については以下のURLを参照。
        #  http://devlights.hatenablog.com/entry/2017/12/04/134738
        #
        #############################################################
        print('start')
        sleep(5)
        print('end')


@show_complete_dialog
def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
