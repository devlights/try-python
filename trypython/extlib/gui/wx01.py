"""
wxPython についてのサンプルです

お決まりの Hello world について

REFERENCES:: http://bit.ly/2OcHRh7
"""
# noinspection PyPackageRequirements
import wx

from trypython.common.commoncls import SampleBase


class Sample(SampleBase):
    def exec(self):
        app = wx.App()

        frm = wx.Frame(parent=None, title='Hello World')
        frm.Show()

        app.MainLoop()


def go():
    obj = Sample()
    obj.exec()
