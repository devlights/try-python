"""
初期処理を実施します.
"""
from typing import Dict, Callable

from trypython import advanced, basic, stdlib, py38


def make_mappings() -> Dict[str, Callable[[], None]]:
    """サンプル名と実行する関数のマッピングを生成します"""
    # noinspection PyDictCreation
    m = {}

    advanced.regist_modules(m)
    basic.regist_modules(m)
    stdlib.regist_modules(m)
    py38.regist_modules(m)

    return m


mappings = make_mappings()
