"""
wxPython についてのサンプルです.

wx.BoxSizer について
"""
import typing

import wx

from trypython.common.commoncls import SampleBase


class MyApp(wx.App):

    def __init__(self, redirect=False, filename=None, use_best_visual=False, clear_sig_int=True):
        super().__init__(redirect=redirect, filename=filename, useBestVisual=use_best_visual, clearSigInt=clear_sig_int)
        self._frame: typing.Optional[wx.Frame] = None

    def OnInit(self) -> bool:
        super().OnInit()
        self._frame = wx.Frame(None, title='wx03', size=(200, 200))
        self._build_ui()
        self.SetTopWindow(self._frame)
        self._frame.Show(True)
        return True

    def _build_ui(self):
        v_box = wx.BoxSizer(wx.VERTICAL)
        v_box.Add(wx.Button(self._frame, label='hello'))
        v_box.Add(wx.Button(self._frame, label='world'))

        h_box = wx.BoxSizer(wx.HORIZONTAL)
        h_box.Add(wx.Button(self._frame, label='hello'))
        h_box.Add(wx.Button(self._frame, label='world'))
        v_box.Add(h_box)

        self._frame.SetSizer(v_box)


class Sample(SampleBase):
    def exec(self):
        app = MyApp()
        app.MainLoop()


def go():
    obj = Sample()
    obj.exec()
