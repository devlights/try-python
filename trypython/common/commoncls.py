# coding: utf-8

"""
共通クラスが定義されています。
"""
from abc import *


class SampleBase(metaclass=ABCMeta):
    @abstractmethod
    def exec(self):
        raise NotImplementedError()
