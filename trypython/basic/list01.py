#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
リストの基本サンプルです。
"""


class Sample:
    def exec(self):
        list1 = [1, 2, 3, 4, 5]
        print(list1)

        list1.append(10)
        print(list1)

        list1.remove(10)
        print(list1)

        print(2 in list1)
        print(100 in list1)


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
