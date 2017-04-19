# coding: utf-8

"""
共通クラスが定義されています。
"""
import contextlib
from abc import ABCMeta, abstractmethod
from datetime import datetime


class SampleBase(metaclass=ABCMeta):
    """
    サンプルクラスの基底となるクラスです。
    """

    @abstractmethod
    def exec(self):
        """処理を実行します。"""
        raise NotImplementedError()


class timetracer(contextlib.AbstractContextManager):
    """処理時間を計測します。"""

    def __init__(self, message: str):
        self._message = message
        self._start = None

    def __enter__(self):
        self._start = datetime.now()

    def __exit__(self, exc_type, exc_value, traceback):
        diff = (datetime.now() - self._start)
        print(f'[{self._message}] elapsed: {diff.seconds}.{diff.microseconds} seconds')
