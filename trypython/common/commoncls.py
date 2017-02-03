# coding: utf-8

"""
共通クラスが定義されています。
"""
from abc import *


class SampleBase(metaclass=ABCMeta):
    """
    サンプルクラスの基底となるクラスです。
    """
    @abstractmethod
    def exec(self):
        raise NotImplementedError()
