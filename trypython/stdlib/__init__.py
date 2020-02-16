"""
初期処理を実施します.
"""
from typing import Dict, Callable

from trypython.stdlib.argparse_ import argparse01
from trypython.stdlib.atexit_ import atexit01
from trypython.stdlib.binascii_ import binascii01
from trypython.stdlib.collections_ import collections01, collections02, collections03, collections04, collections05, \
    collections06, collections07
from trypython.stdlib.contextlib_ import contextlib01, contextlib02
from trypython.stdlib.csv_ import csv01, csv02
from trypython.stdlib.dataclasses_ import dataclasses01, dataclasses02
from trypython.stdlib.datetime_ import datetime01, datetime02
from trypython.stdlib.dis_ import dis01
from trypython.stdlib.functools_ import functools01, functools02, functools03
from trypython.stdlib.gc_ import gc01
from trypython.stdlib.itertools_ import itertools01, itertools02, itertools03, itertools04, itertools05, itertools06, \
    itertools07, itertools08
from trypython.stdlib.json_ import json01
from trypython.stdlib.keyword_ import keyword01
from trypython.stdlib.logging_ import logging01, logging02, logging03, logging04, logging05, logging06, logging07, \
    logging08, logging09, logging10
from trypython.stdlib.mmap_ import mmap01
from trypython.stdlib.multiprocessing_ import multiprocessing01
from trypython.stdlib.operator_ import operator01
from trypython.stdlib.pathlib_ import pathlib01, pathlib02
from trypython.stdlib.pickle_ import pickle01
from trypython.stdlib.re_ import re01, re02, re03, re04, re05, re06, re07
from trypython.stdlib.reprlib_ import reprlib01
from trypython.stdlib.secrets_ import secrets01
from trypython.stdlib.signal_ import signal01
from trypython.stdlib.socket_ import socket01
from trypython.stdlib.struct_ import struct01
from trypython.stdlib.sys_ import sys01, sys02, sys03, sys_getsizeof_vs_dunder_sizeof_diff
from trypython.stdlib.tempfile_ import tempfile01, tempfile02, tempfile03
from trypython.stdlib.textwrap_ import textwrap01
from trypython.stdlib.time_ import time01
from trypython.stdlib.tkinter_ import messagebox01
from trypython.stdlib.tracemalloc_ import tracemalloc01
from trypython.stdlib.typing_ import typing01
from trypython.stdlib.weakref_ import weakref01, weakref02
from trypython.stdlib.xml_ import xml01


def regist_modules(m: Dict[str, Callable[[], None]]):
    ########################################
    # trypython.stdlib
    ########################################
    m["argparse_01"] = argparse01.go
    m["atexit_01"] = atexit01.go
    m["binascii_01"] = binascii01.go
    m["collections_01"] = collections01.go
    m["collections_02"] = collections02.go
    m["collections_03"] = collections03.go
    m["collections_04"] = collections04.go
    m["collections_05"] = collections05.go
    m["collections_06"] = collections06.go
    m["collections_07"] = collections07.go
    m["contextlib_01"] = contextlib01.go
    m["contextlib_02"] = contextlib02.go
    m["csv_01"] = csv01.go
    m["csv_02"] = csv02.go
    m["dataclasses_01"] = dataclasses01.go
    m["dataclasses_02"] = dataclasses02.go
    m["datetime_01"] = datetime01.go
    m["datetime_02"] = datetime02.go
    m["dis_01"] = dis01.go
    m["functools_01"] = functools01.go
    m["functools_02"] = functools02.go
    m["functools_03"] = functools03.go
    m["gc_01"] = gc01.go
    m["itertools_01"] = itertools01.go
    m["itertools_02"] = itertools02.go
    m["itertools_03"] = itertools03.go
    m["itertools_04"] = itertools04.go
    m["itertools_05"] = itertools05.go
    m["itertools_06"] = itertools06.go
    m["itertools_07"] = itertools07.go
    m["itertools_08"] = itertools08.go
    m["json_01"] = json01.go
    m["keyword_01"] = keyword01.go
    m["logging_01"] = logging01.go
    m["logging_02"] = logging02.go
    m["logging_03"] = logging03.go
    m["logging_04"] = logging04.go
    m["logging_05"] = logging05.go
    # m["logging_06"] = logging06.go
    # m["logging_07"] = logging07.go
    # m["logging_08"] = logging08.go
    m["logging_09"] = logging09.go
    m["logging_10"] = logging10.go
    m["mmap_01"] = mmap01.go
    m["multiprocessing_01"] = multiprocessing01.go
    m["operator_01"] = operator01.go
    m["pathlib_01"] = pathlib01.go
    m["pathlib_02"] = pathlib02.go
    m["pickle_01"] = pickle01.go
    m["re_01"] = re01.go
    m["re_02"] = re02.go
    m["re_03"] = re03.go
    m["re_04"] = re04.go
    m["re_05"] = re05.go
    m["re_06"] = re06.go
    m["re_07"] = re07.go
    m["reprlib_01"] = reprlib01.go
    m["secrets_01"] = secrets01.go
    m["signal_01"] = signal01.go
    m["socket_01"] = socket01.go
    m["struct_01"] = struct01.go
    m["sys_01"] = sys01.go
    m["sys_02"] = sys02.go
    m["sys_03"] = sys03.go
    m["sys_getsizeof_vs_dunder_sizeof_diff"] = sys_getsizeof_vs_dunder_sizeof_diff.go
    m["tempfile_01"] = tempfile01.go
    m["tempfile_02"] = tempfile02.go
    m["tempfile_03"] = tempfile03.go
    m["textwrap_01"] = textwrap01.go
    m["time_01"] = time01.go
    m["tkinter_01"] = messagebox01.go
    m["tracemalloc_01"] = tracemalloc01.go
    m["typing_01"] = typing01.go
    m["weakref_01"] = weakref01.go
    m["weakref_02"] = weakref02.go
    m["xml_01"] = xml01.go
