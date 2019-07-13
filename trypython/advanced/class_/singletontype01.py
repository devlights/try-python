"""
python シングルトンオブジェクトを利用するサンプルです。

REFERENCES::
https://github.com/stoic1979/PyLogger/blob/master/logger.py
"""
import typing as ty

from trypython.common.commoncls import SampleBase


class SingletonType(type):
    """シングルトンを実現するためのメタクラスです"""
    _instances: ty.Dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonObject(metaclass=SingletonType):
    """シングルトンクラス"です"""

    def __init__(self):
        print('[call] init()')


class Sample(SampleBase):
    """サンプルクラスです"""

    def exec(self):
        """シングルトンオブジェクトのサンプルを試します。"""
        obj1 = SingletonObject()
        obj2 = SingletonObject()
        obj3 = SingletonObject()

        print(f'obj1={id(obj1)}, obj2={id(obj2)}, obj3={id(obj3)}')


def go():
    """処理を実行します。"""
    obj = Sample()
    obj.exec()
