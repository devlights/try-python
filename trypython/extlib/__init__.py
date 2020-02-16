import sys
from typing import Dict, Callable

from trypython.extlib.aiohttp import aiohttp01
from trypython.extlib.aiojobs import aiojobs01
from trypython.extlib.async_timeout import async_timeout01
from trypython.extlib.bitstring import bitstring01, bitstring02, bitstring03, bitstring04
from trypython.extlib.blinker import blinker01
from trypython.extlib.crayons import crayons01
from trypython.extlib.dateutil import dateutil01
from trypython.extlib.icecream import icecream01
from trypython.extlib.joblib import joblib01, joblib02
from trypython.extlib.netaddr import netaddr01
from trypython.extlib.psutil import psutil01
from trypython.extlib.pygments import pygments01, pygments02
from trypython.extlib.pyperclip import pyperclip01
from trypython.extlib.rich import rich_helloworld
from trypython.extlib.texttable import texttable01
from trypython.extlib.twisted import twisted01
from trypython.extlib.yaml import yaml01, yaml02, yaml03, yaml04, yaml05
from trypython.extlib.yarl import yarl01
from trypython.extlib.zmq import zmq01, zmq02, zmq03


def regist_modules(m: Dict[str, Callable[[], None]]):
    ########################################
    # trypython.extlib
    ########################################
    m["aiohttp_01"] = aiohttp01.go
    m["aiojobs_01"] = aiojobs01.go
    m["async_timeout_01"] = async_timeout01.go
    m["bitstring_01"] = bitstring01.go
    m["bitstring_02"] = bitstring02.go
    m["bitstring_03"] = bitstring03.go
    m["bitstring_04"] = bitstring04.go
    m["blinker_01"] = blinker01.go

    if not sys.platform.startswith('win'):
        from trypython.extlib.ciso8601 import ciso8601_01
        m["ciso8601_01"] = ciso8601_01.go

    m["crayons_01"] = crayons01.go
    m["dateutil_01"] = dateutil01.go

    if sys.platform.startswith('win'):
        from trypython.extlib.forwindows import pyautogui01, pythonnet01
        m["pyautogui_01"] = pyautogui01.go
        m["pythonnet_01"] = pythonnet01.go

    if not sys.platform.startswith('linux'):
        from trypython.extlib.gui import wx01, wx02, wx03
        m["gui_wx_01"] = wx01.go
        m["gui_wx_02"] = wx02.go
        m["gui_wx_03"] = wx03.go
    
    m["icecream_01"] = icecream01.go
    m["joblib_01"] = joblib01.go
    m["joblib_02"] = joblib02.go
    m["netaddr_01"] = netaddr01.go
    m["psutil_01"] = psutil01.go
    m["pygments_01"] = pygments01.go
    m["pyperclip_01"] = pyperclip01.go
    m["rich_helloworld"] = rich_helloworld.go
    m["texttable_01"] = texttable01.go
    m["twisted_01"] = twisted01.go
    m["yaml_01"] = yaml01.go
    m["yaml_02"] = yaml02.go
    m["yaml_03"] = yaml03.go
    m["yaml_04"] = yaml04.go
    m["yaml_05"] = yaml05.go
    m["yarl_01"] = yarl01.go
    m["zmq_01"] = zmq01.go
    m["zmq_02"] = zmq02.go
    m["zmq_03"] = zmq03.go
