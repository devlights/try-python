"""
ZeroMQ (PyZMQ) の PUB-SUB パターンのサンプルです。

REFERENCES::
http://zguide.zeromq.org/page:all#Getting-the-Message-Out
"""
import datetime as dt
import multiprocessing as mp
import time

import zmq

from trypython.common.commoncls import SampleBase


class Sample(SampleBase):
    """ZeroMQ の PUB-SUB パターンのサンプルです。"""
    _SERVERURL = 'tcp://*:5555'
    _CLIENTURL = 'tcp://localhost:5555'

    def exec(self):
        """サンプル処理を実行します。"""
        # ----------------------------------------------------
        # サーバ側とクライアント側のプロセスを起動
        #
        # 今回 PUB-SUB パターンなので
        # PUBLISHするプロセスに対して複数のSUBSCRIBERが存在する。
        #
        # PUB側は毎秒の値をPUBLISHし、SUB側はそれぞれフィルターに合致した
        # データを受信して表示する。フィルターを空文字にすると全部取得となる。
        #
        #
        # 参考）
        #   http://zguide.zeromq.org/py:wuserver
        #   http://zguide.zeromq.org/py:wuclient
        #   https://stackoverflow.com/questions/13904626/zeromq-and-multiple-subscribe-filters-in-python
        #   https://stackoverflow.com/questions/6024003/why-doesnt-zeromq-work-on-localhost
        #
        # 注意）ZeroMQ のガイドにあるように、最初の発行は常に受信できない。
        #   http://zguide.zeromq.org/page:all#Getting-the-Message-Out
        #
        # 引用::
        # the subscriber will always miss the first messages that the publisher sends.
        #
        # ----------------------------------------------------
        server_proc = mp.Process(target=Sample.server, args=())
        client_procs = [
            mp.Process(target=Sample.client, args=(str(i),))
            for i in range(10, 61, 10)
        ]
        client_all_proc = mp.Process(target=Sample.client_all, args=())

        # ----------------------------------------------------
        # プロセス起動
        # ----------------------------------------------------
        for p in client_procs:
            p.start()
        else:
            client_all_proc.start()
            server_proc.start()

        # ----------------------------------------------------
        # プロセス終了待ち
        # ----------------------------------------------------
        for p in client_procs:
            p.join()
        else:
            client_all_proc.join()
            server_proc.join()

    @staticmethod
    def server():
        """PUB側の処理を行います。"""
        context = zmq.Context()
        socket = context.socket(zmq.PUB)
        socket.bind(Sample._SERVERURL)

        # ----------------------------------------------------
        # 毎秒、値を発行
        # ----------------------------------------------------
        while True:
            message = dt.datetime.now().strftime('%S')
            socket.send_string(message)
            print(f'[server] pub --> {message}', flush=True)
            time.sleep(1)

    @staticmethod
    def client(sub_filter):
        """SUB側の処理を行います。（フィルター付き）"""
        start = int(sub_filter)
        context = zmq.Context()
        socket = context.socket(zmq.SUB)
        socket.connect(Sample._CLIENTURL)

        # ----------------------------------------------------
        # フィルター設定
        # ----------------------------------------------------
        for f in (str(i) for i in range(start, start + 10)):
            socket.setsockopt_string(zmq.SUBSCRIBE, f)

        # ----------------------------------------------------
        # 受信処理
        # ----------------------------------------------------
        while True:
            message = socket.recv_string()
            print(f'\t[client-{sub_filter}]:  {message}', flush=True)

    @staticmethod
    def client_all():
        """SUB側の処理を行います。（フィルター無し（全部取得））"""
        context = zmq.Context()
        socket = context.socket(zmq.SUB)
        socket.connect(Sample._CLIENTURL)

        # ----------------------------------------------------
        # フィルター設定
        #   空文字のフィルターは全取得を意味する。
        # ----------------------------------------------------
        socket.setsockopt_string(zmq.SUBSCRIBE, '')

        # ----------------------------------------------------
        # 受信処理
        # ----------------------------------------------------
        while True:
            message = socket.recv_string()
            print(f'\t[client-all]:  {message}', flush=True)


def go():
    obj = Sample()
    obj.exec()
