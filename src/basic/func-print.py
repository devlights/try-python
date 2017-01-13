#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
print関数のサンプルです。
"""


class Sample:
    def exec(self) -> None:
        ##################################
        # print関数
        # python3からprintが関数になったため
        # カッコの付与が必須となっている。
        message = 'hello world'
        print(message)

        ##################################
        # 複数の値を指定することができる
        # デフォルトは空白でつながる
        message2 = 'hello world2'
        print(message, message2)


if __name__ == '__main__':
    obj = Sample()
    obj.exec()
