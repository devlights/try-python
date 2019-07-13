# coding: utf-8
"""
pyautogui モジュールのサンプルです。
マウスの移動について
"""
import pyautogui as autogui

from trypython.common.commoncls import SampleBase


class Sample(SampleBase):
    def exec(self):
        # ---------------------------------------------------------------------
        # pyautogui モジュールは、GUIオートメーションをpythonで行うためのモジュール
        # ---------------------------------------------------------------------
        # http://pyautogui.readthedocs.io/en/latest/cheatsheet.html
        # ---------------------------------------------------------------------
        # size() で メインモニタのスクリーンサイズを、moveTo() で指定位置にマウスカーソル
        # の移動が行える。
        # ---------------------------------------------------------------------
        screen_width, screen_height = autogui.size()

        autogui.moveTo(100, 100, duration=2)
        autogui.moveTo(screen_width - 100, 100, duration=1)
        autogui.moveTo(screen_width - 100, screen_height - 100, duration=1)
        autogui.moveTo(100, screen_height - 100, duration=2)


def go():
    obj = Sample()
    obj.exec()
