"""
組み込み関数 iter(callable, sentinel) についてのサンプルです。

iter(callable, sentinel) と functools.partial を組合せて
ソケット通信時の受信処理をループせずに行っています。

REMARKS::
本サンプルを実行する前に予め以下をコマンドラインで実行しておく必要があります。

$ python -m trypython.advanced.socket_server01
"""
import functools
import socket

from trypython.common.commoncls import SampleBase


class Sample(SampleBase):
    """本サンプルの処理を実装しているクラスです"""
    def __init__(self):
        self._host = '127.0.0.1'
        self._port = 8888

    def exec(self):
        """処理を実行します"""
        with socket.socket() as sock:
            sock.connect((self._host, self._port))
            recv = functools.partial(sock.recv, 1)  # partialで callable を作る。（わざと1バイトずつ受信するようにしている）
            recv_bytes = b''.join(iter(recv, b''))  # 1バイトずつ受信したものを一気に結合
            print(f'From server [{recv_bytes.decode("utf-8")}]')  # bytes なので復号する


def go():
    """サンプルを実行します"""
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
