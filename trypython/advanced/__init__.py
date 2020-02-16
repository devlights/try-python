"""
初期処理を実施します.
"""
from typing import Dict, Callable

from trypython.advanced.class_ import cls01, cls02, cls03, dynamicclass01, singletontype01, slots01
from trypython.advanced.closure import closure01
from trypython.advanced.comprehension import comprehension01, diff_py2topy3_listcomp_scope
from trypython.advanced.contextmanager import contextmanager01
from trypython.advanced.coroutine import coroutine01
from trypython.advanced.decorator import decorator01
from trypython.advanced.fileio import rmdir01
from trypython.advanced.generator import generator01, yield01
from trypython.advanced.iter_ import iter01, iter02, iterableunpacking01
from trypython.advanced.networking import socket_server01


def regist_modules(m: Dict[str, Callable[[], None]]):
    ########################################
    # trypython.advenced
    ########################################
    m["class_cls01"] = cls01.go
    m["class_cls02"] = cls02.go
    m["class_cls03"] = cls03.go
    m["class_dynamic_class01"] = dynamicclass01.go
    m["class_singleton_type01"] = singletontype01.go
    m["class_slots01"] = slots01.go
    m["closure01"] = closure01.go
    m["comprehension01"] = comprehension01.go
    m["diff_list_comprehension"] = diff_py2topy3_listcomp_scope.go
    m["contextmanager01"] = contextmanager01.go
    m["coroutine01"] = coroutine01.go
    m["decorator01"] = decorator01.go
    m["fileio_rmdir01"] = rmdir01.go
    m["generator_01"] = generator01.go
    m["generator_yield01"] = yield01.go
    m["iter_01"] = iter01.go
    m["iter_02"] = iter02.go
    m["iter_iterable_unpacking"] = iterableunpacking01.go
    m["networking_socket_server01"] = socket_server01.start
