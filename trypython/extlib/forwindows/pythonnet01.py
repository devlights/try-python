# coding: utf-8
"""
pythonnet (Python for .NET) のサンプルです。
.NET の List<T>, Dictionary<K,V>, Task などの利用について。
"""

# --------------------------------------------------------------
# pythonnet を利用する場合、まず最初に clr をインポートする
# --------------------------------------------------------------
# noinspection PyPackageRequirements
import clr

# --------------------------------------------------------------
# 必要なクラスが存在する 名前空間を指定しておく
# --------------------------------------------------------------
clr.AddReference('System.Collections')
clr.AddReference('System.Threading.Tasks')

# --------------------------------------------------------------
# .NET 側のインポート宣言
# --------------------------------------------------------------
# noinspection PyUnresolvedReferences
import System
# noinspection PyUnresolvedReferences
from System.Collections.Generic import List
# noinspection PyUnresolvedReferences
from System.Threading import Thread
# noinspection PyUnresolvedReferences
from System.Threading.Tasks import Task

from trypython.common.commonfunc import pr
from trypython.common.commoncls import SampleBase


class Sample(SampleBase):
    def exec(self):
        # --------------------------------------------------------------
        # List<T> の生成
        #   大抵の.NET クラスは、普通に呼び出せる。
        #   List<T> は、ジェネリックなので List[T]() という形で呼べる。
        #   Dictionary<K,V> の場合は、 Dictionary[K,V]() となる。
        # --------------------------------------------------------------
        net_list01 = List[int]()
        for x in range(10):
            net_list01.Add(x)

        pr('net_list01', net_list01)
        pr('net_list01.Count', net_list01.Count)
        pr('items', ','.join(str(x) for x in net_list01))

        # --------------------------------------------------------------
        # 引数に IEnumerable<T> を要求するメソッドの場合
        #   AddRangeを Python の list で呼ぶとエラーになる
        #      e.g. TypeError: No method matches given arguments
        #   net_list01.AddRange([10, 11, 12])
        #   つまり、Python の list のままでは駄目だということ。
        # --------------------------------------------------------------

        # --------------------------------------------------------------
        # 以下のように別のList<T>を作って, それをAddRangeはOK
        # --------------------------------------------------------------
        net_list02 = List[int]()
        net_list02.Add(11)
        net_list02.Add(12)
        net_list02.Add(13)

        net_list01.AddRange(net_list02)
        pr('items', ','.join(str(x) for x in net_list01))

        # --------------------------------------------------------------
        # 以下のやり方でもOK
        #
        # Pythonの list から .NET 側の シーケンスを 構築する場合は
        # 以下のように System.Array からつくる。
        #
        #   http://stackoverflow.com/questions/16484167/python-net-framework-reference-argument-double
        #
        # --------------------------------------------------------------
        py_list01 = [21, 22, 23]
        ary01 = System.Array[int](py_list01)
        net_list01.AddRange(ary01)
        pr('items', ','.join(str(x) for x in net_list01))

        # -------------------------------------------------------
        # System.Threading.Tasks.Task は、delegate を要求する。
        # そのまま Python の function オブジェクトを渡しても
        # エラーになる。Task.Run のシグネチャに合わせて
        # System.Action を生成して渡す。
        #
        #   http://stackoverflow.com/questions/30659933/python3-pythonnet-generic-delegates
        # -------------------------------------------------------
        def print_hello():
            for _ in range(3):
                Thread.Sleep(500)
                print('task---sleep')

            print('hello world')

        net_task01 = Task.Run(System.Action(print_hello))
        pr('task', net_task01)
        net_task01.Wait()

        # -------------------------------------------------------
        # null は Python には存在しないので None を設定するみたい。
        #   https://github.com/pythonnet/pythonnet/blob/master/src/tests/test_array.py
        # -------------------------------------------------------
        try:
            tmp_list = List[str]()
            tmp_list.Add('hello')
            tmp_list.Add('world')

            tmp_list.Clear()

            assert tmp_list is not None
            tmp_list = None
            assert tmp_list is None

            tmp_list.Add('hello world')

        except AttributeError as attr_ex:
            pr('attr-ex', attr_ex)

        # -------------------------------------------------------
        # .NET 側の例外も普通にハンドルできる
        # スローしたい場合は raise でOK
        # -------------------------------------------------------
        try:
            raise_nullex()
        except System.NullReferenceException as null_ex:
            pr('csharp-ex', null_ex)


def raise_nullex():
    raise System.NullReferenceException('nullpo')


def go():
    obj = Sample()
    obj.exec()
