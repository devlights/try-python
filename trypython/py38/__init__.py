import sys
from typing import Dict, Callable


def regist_modules(m: Dict[str, Callable[[], None]]):
    ########################################
    # trypython.py38
    ########################################
    if sys.version.startswith('3.8'):
        from trypython.py38 import assignment_expression, fstring_debug

        m["py38_assignment_expression"] = assignment_expression.go
        m["py38_fstring_debug"] = fstring_debug.go
