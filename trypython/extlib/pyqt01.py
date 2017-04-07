# coding: utf-8

"""
PyQt5のサンプルです。
何もないタダのWindowを表示するだけ。
"""

import sys

import PyQt5.QtWidgets as qt


def go():
    # ---------------------------
    # 最初にQGuiApplicationを生成
    # ---------------------------
    app = qt.QApplication(sys.argv)

    # ---------------------------
    # 次にメインウィンドウを生成
    # ---------------------------
    win = qt.QWidget()
    win.resize(320, 240)
    win.setWindowTitle('PyQt5 Hello World')

    # ---------------------------
    # メインウィンドウ表示
    # ---------------------------
    win.show()

    # ------------------------------------
    # イベントループ開始
    # ----------------
    # イベントループの終了と共にアプリも終了
    # ------------------------------------
    sys.exit(app.exec_())


if __name__ == '__main__':
    go()
