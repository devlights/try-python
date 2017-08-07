# coding: utf-8

"""
各処理の後に付与できる オプション else節 についてのサンプルです。
"""
from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        # ------------------------------------------------------------
        # Pythonの for, while, try には else をつけることが出来る
        # どれも、正常に処理が通った場合に else に入るようになっている。
        #
        # for: ループが break されずに終了した場合
        # while: ループが break されずに終了した場合
        # try: 例外が発生しなかった場合
        #
        # 何かをサーチするような処理の場合、見つけた時点で break することが
        # 多いため、このようなときに else を入れておくと見つからなかった場合の
        # 処理を簡単に書くことが出来る。
        #
        # tryの場合は、例外が発生せずに正常に処理が通ったときを判定できる
        # ------------------------------------------------------------
        for x in range(5):
            pr('for-loop', x)
        else:
            pr('for-else', 'passed')

        pr('-----------------------------------', '')

        for x in range(5):
            if x == 3:
                break
            pr('for-loop', x)
        else:
            pr('for-else', 'passed')

        pr('-----------------------------------', '')

        count = 5
        while count >= 0:
            pr('while-loop', count)
            count -= 1
        else:
            pr('while-else', 'passed')

        pr('-----------------------------------', '')

        count = 5
        while count >= 0:
            if count == 2:
                break
            pr('while-loop', count)
            count -= 1
        else:
            pr('while-else', 'passed')

        pr('-----------------------------------', '')

        try:
            pr('try', sum((10, 20,)))
        except MyException as e:
            pr('except', e)
        else:
            pr('try-else', 'passed')

        pr('-----------------------------------', '')

        # noinspection PyUnreachableCode
        try:
            pr('try', sum((10, 20,)))
            raise MyException('this is test exception.')
        except MyException as e:
            pr('except', e)
        else:
            pr('try-else', 'passed')


class MyException(Exception):
    def __init__(self, message: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._message = message

    def __str__(self, *args, **kwargs):
        return f'{self._message}'

    def __repr__(self, *args, **kwargs):
        return self.__str__(*args, **kwargs)


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
