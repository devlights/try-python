# coding: utf-8
"""
mmap モジュールについてのサンプルです。

通常の file-like オブジェクトを使ってのファイル処理より
mmapオブジェクトの方が効率がいい場合があることを確認するサンプルです。
"""
import itertools
import mmap
import re
from timeit import timeit
from typing import Union, Match

from trypython.common.commoncls import SampleBase


# noinspection SpellCheckingInspection
class Sample(SampleBase):
    LINUX_WORDS = 'linux.words'
    KEN_ALL = 'KEN_ALL_UTF8.csv'
    LINUX_WORDS_PATTERN = 'zymurgies'
    KEN_ALL_PATTERN = '鳩間'

    def __init__(self):
        self._files = [
            self.LINUX_WORDS,
            self.KEN_ALL
        ]

        self._methods = [
            self.grep1,
            self.grep2,
            self.grep3
        ]

        self._pattern_factory = {
            self.LINUX_WORDS: {
                self.grep1: lambda: self.LINUX_WORDS_PATTERN,
                self.grep2: lambda: self.LINUX_WORDS_PATTERN,
                self.grep3: lambda: self.LINUX_WORDS_PATTERN.encode('utf-8')
            },
            self.KEN_ALL: {
                self.grep1: lambda: self.KEN_ALL_PATTERN,
                self.grep2: lambda: self.KEN_ALL_PATTERN,
                self.grep3: lambda: self.KEN_ALL_PATTERN.encode('utf-8')
            }
        }

    def exec(self):
        for f, m in itertools.product(self._files, self._methods):
            p = self._pattern_factory[f][m]
            r = timeit('m(p(), f)', number=1, globals=locals())
            print(f'[file={f:20}|{m.__name__}]\t{r:0.3f}')

    @staticmethod
    def grep1(pattern: str, file_path: str) -> Union[Match, None]:
        with open(file_path, mode='r', encoding='utf-8') as f:
            for l in f:
                m = re.search(pattern, l)
                if m:
                    return m
        return None

    @staticmethod
    def grep2(pattern: str, file_path: str) -> Union[Match, None]:
        with open(file_path, mode='r', encoding='utf-8') as f:
            return re.search(pattern, f.read())

    # noinspection PyTypeChecker
    @staticmethod
    def grep3(pattern: bytes, file_path: str) -> Union[Match, None]:
        with open(file_path, mode='r', encoding='utf-8') as f:
            mm = mmap.mmap(f.fileno(), length=0, access=mmap.ACCESS_READ)
            return re.search(pattern, mm)


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
