# coding: utf-8

"""
共通クラスが定義されています。
"""
import contextlib
from datetime import datetime
from abc import ABCMeta, abstractmethod


class SampleBase(metaclass=ABCMeta):
    """
    サンプルクラスの基底となるクラスです。
    """

    @abstractmethod
    def exec(self):
        raise NotImplementedError()


class timetracer(contextlib.AbstractContextManager):
    def __init__(self, message: str):
        self._message = message
        self._start = None

    def __enter__(self):
        self._start = datetime.now()

    def __exit__(self, exc_type, exc_value, traceback):
        diff = (datetime.now() - self._start)
        print(f'[{self._message}] elapsed: {diff.seconds}.{diff.microseconds} seconds')
