# coding: utf-8

"""
ZeroMQ (PyZMQ) の REP-REQ パターンのサンプルです。
"""
import itertools as it
import multiprocessing as mp
import time

import zmq

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    _SERVERURL = 'tcp://*:5555'
    _CLIENTURL = 'tcp://localhost:5555'

    def exec(self):
        server_proc = mp.Process(target=Sample.server, args=())
        client_proc = mp.Process(target=Sample.client, args=())

        server_proc.start()
        client_proc.start()

        client_proc.join()
        server_proc.join()

    @staticmethod
    def client():
        """クライアント側の処理です。"""
        #
        # ZeroMQでの REP-REQ パターン
        # クライアントは REQ 側となる。
        # 手順としては以下の通り
        #   (1) zmq.Context 生成
        #   (2) コンテキストから zmq.Socket 生成
        #   (3) connect メソッドで接続
        #   (4) send/recv メソッドでやり取り
        #
        # 注意点として、REP-REQ パターンの場合
        # 必ず、片方が send したら 片方が recv する必要がある。
        # 一方的に送り続けることは出来ない。(要求-応答パターンなので)
        #
        # 大きなデータを送った際の分割結合などの細かい部分は ZeroMQ が
        # 面倒見てくれるので気にしなくて良い。
        #
        ctx = zmq.Context()
        socket = ctx.socket(zmq.REQ)  # type: zmq.Socket
        socket.connect(Sample._CLIENTURL)

        for i in range(5):
            send_message = f'hello from client {i}'
            socket.send(send_message.encode('utf-8'))
            pr('send(client)', send_message)

            recv_result = socket.recv()
            pr('recv(client)', recv_result)

            time.sleep(0.5)

        socket.send(b'quit')
        pr('recv(client)', socket.recv())

        pr('done', 'client')

    @staticmethod
    def server():
        """サーバー側の処理です。"""
        #
        # ZeroMQでの REP-REQ パターン
        # サーバーは REP 側となる。
        # 手順としては以下の通り
        #   (1) zmq.Context 生成
        #   (2) コンテキストから zmq.Socket 生成
        #   (3) bind メソッドでポート空ける
        #   (4) send/recv メソッドでやり取り
        #
        # 注意点として、REP-REQ パターンの場合
        # 必ず、片方が send したら 片方が recv する必要がある。
        # 一方的に送り続けることは出来ない。(要求-応答パターンなので)
        #
        # 大きなデータを送った際の分割結合などの細かい部分は ZeroMQ が
        # 面倒見てくれるので気にしなくて良い。
        #
        ctx = zmq.Context()
        socket = ctx.socket(zmq.REP)
        socket.bind(Sample._SERVERURL)

        for i in it.count():
            recv_result = socket.recv()
            pr('recv(server)', recv_result)

            if recv_result == b'quit':
                socket.send(b'ok')
                break

            send_message = f'return from server {i}'
            socket.send(send_message.encode('utf-8'))
            pr('send(server)', send_message)

        pr('done', 'server')


def go():
    obj = Sample()
    obj.exec()
