from typing import Dict, Callable

from trypython.basic.builtinfunc import builtinfunc01, float01, format01, len01, round01
from trypython.basic.bytes_ import bytes01
from trypython.basic.dict_ import dict01, dict02, dict_preserved_insert_order_py37
from trypython.basic.elseclause import elseclause01
from trypython.basic.enum_ import enum01
from trypython.basic.func_ import func01, func02, func03
from trypython.basic.globals_ import globals_and_locals01
from trypython.basic.int_ import int01
from trypython.basic.io import io01
from trypython.basic.list_ import list01, list02, list_copy
from trypython.basic.others import mathoperators01, pairwise01, thousands_separator01, vars01, zeropadding01
from trypython.basic.print_ import print01
from trypython.basic.set_ import set01
from trypython.basic.slice_ import slice01
from trypython.basic.str_ import str01, str02, str03, str_in_multiple01
from trypython.basic.tuple_ import tuple01
from trypython.basic.unpacking import unpack01, unpack_pep448


def regist_modules(m: Dict[str, Callable[[], None]]):
    ########################################
    # trypython.basic
    ########################################
    m["builtin_functions"] = builtinfunc01.go
    m["builtin_float"] = float01.go
    m["builtin_format"] = format01.go
    m["builtin_len"] = len01.go
    m["builtin_round"] = round01.go
    m["bytes_01"] = bytes01.go
    m["dict_01"] = dict01.go
    m["dict_02"] = dict02.go
    m["dict_insert_order"] = dict_preserved_insert_order_py37.go
    m["elseclause_01"] = elseclause01.go
    m["enum_01"] = enum01.go
    m["func_01"] = func01.go
    m["func_02"] = func02.go
    m["func_03"] = func03.go
    m["globals_and_locals"] = globals_and_locals01.go
    m["int_01"] = int01.go
    m["io_01"] = io01.go
    m["list_01"] = list01.go
    m["list_02"] = list02.go
    m["list_copy"] = list_copy.go
    m["other_math_operator"] = mathoperators01.go
    m["other_pairwise"] = pairwise01.go
    m["other_thousands_separator"] = thousands_separator01.go
    m["other_vars"] = vars01.go
    m["other_zero_padding"] = zeropadding01.go
    m["print_01"] = print01.go
    m["set_01"] = set01.go
    m["slice_01"] = slice01.go
    m["str_01"] = str01.go
    m["str_02"] = str02.go
    m["str_03"] = str03.go
    m["str_in_multiple"] = str_in_multiple01.go
    m["tuple_01"] = tuple01.go
    m["unpack_01"] = unpack01.go
    m["unpack_pep448"] = unpack_pep448.go
