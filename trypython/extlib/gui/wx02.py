"""
wxPython についてのサンプルです

wx.App の サブクラス化 について
"""
import wx

from trypython.common.commoncls import SampleBase


# noinspection PyPep8Naming
class MyApp(wx.App):

    def __init__(self, redirect=False, filename=None, use_best_visual=False, clear_sig_int=True):
        super().__init__(redirect, filename, use_best_visual, clear_sig_int)
        self._frame = None

    def OnInit(self) -> bool:
        super().OnInit()
        self._frame = wx.Frame(None)
        self._frame.SetTitle('wx02.py')
        self.SetTopWindow(self._frame)
        self._frame.Show(True)
        return True


class Sample(SampleBase):
    def exec(self):
        app = MyApp()
        app.MainLoop()


def go():
    obj = Sample()
    obj.exec()
