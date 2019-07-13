"""
netaddr モジュールについてのサンプルです

基本的な使い方について

REFERENCES:: http://bit.ly/2Oepd8H
             http://bit.ly/2Oc12Yo
             http://bit.ly/2OehqYv
             http://bit.ly/2Oc5W7M
             http://bit.ly/2ObWb9C

"""
import netaddr

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        # --------------------------------------------------------------------------
        # netaddr モジュール
        # ------------------------
        # ネットワークアドレスを表現したり操作したり出来るライブラリ.
        # 例えばIPアドレスの取扱などがとても楽に出来る
        # --------------------------------------------------------------------------
        ip = netaddr.IPAddress('192.168.0.111')
        pr('netaddr.IPAddress', ip)
        pr('ip.version', ip.version)
        pr('ip.ipv4()', ip.ipv4())
        pr('ip.ipv6()', ip.ipv6())
        pr('ip.netmask_bits()', ip.netmask_bits())
        pr('ip.words', ip.words)


def go():
    obj = Sample()
    obj.exec()
