# coding: utf-8
"""
dis モジュールについてのサンプルです。
"""
import dis

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import hr


# noinspection SpellCheckingInspection
class Sample(SampleBase):
    def exec(self):
        ##############################################
        # dis モジュールは、pythonのバイトコードの
        # 解析をサポートしてくれるモジュール。
        #
        # 大きく分けて２つの使い方がある
        #   1) dis.dis()
        #   2) dis.Bytecode()
        #
        # 1) は、指定された内容を逆アセンブルして出力してくれる。
        # 引数の file に何も指定しない場合は標準出力に指定してくれる。
        #
        # 2) は、python 3.4 で追加されたAPI。
        # 指定の仕方は 1) とほぼ変わらないが、いきなり結果を
        # 出力ではなくて、一旦 Bytecode オブジェクトにラップして
        # 返してくれる。
        #
        ##############################################
        listcomp_str = 'r = [x for x in range(1000000) if x % 2 == 0]'
        forloop_str = '''
        
r = []
for x in range(1000000):
    if x % 2 == 0:
        r.append(x)
        
        '''

        ###############################################
        # dis.dis()
        ###############################################
        hr('dis.dis(listcomp_str)')
        dis.dis(listcomp_str)

        hr('dis.dis(forloop_str)')
        dis.dis(forloop_str)

        ###############################################
        # dis.Bytecode()
        #
        # python 3.4 から dis モジュールに追加されたAPI。
        # 内部で code オブジェクトや dis.code_info() の
        # 結果を保持してくれたりするので、こちらの方が便利。
        ###############################################
        hr('dis.Bytecode(listcomp_str)')
        listcomp_bytecode = dis.Bytecode(listcomp_str)

        print(listcomp_bytecode.codeobj)
        print(listcomp_bytecode.dis())
        print(listcomp_bytecode.info())

        hr('dis.Bytecode(forloop_str)')
        forloop_bytecode = dis.Bytecode(forloop_str)

        print(forloop_bytecode.codeobj)
        print(forloop_bytecode.dis())
        print(forloop_bytecode.info())


def go():
    obj = Sample()
    obj.exec()
