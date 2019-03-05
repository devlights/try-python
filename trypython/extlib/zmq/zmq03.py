"""
ZeroMQ (PyZMQ) の PUSH-PULL パターンのサンプルです。

REFERENCES::
http://zguide.zeromq.org/page:all#Divide-and-Conquer
"""
import multiprocessing as mp
import time

import zmq

from trypython.advanced.multiprocesslatch import CountDownLatch
from trypython.common.commoncls import SampleBase


class Sample(SampleBase):
    """ZeroMQ の PUSH-PULL パターンのサンプルです。"""
    VENTILATOR_BIND_URL = 'tcp://*:5555'
    VENTILATOR_CONNECT_URL = 'tcp://localhost:5555'
    SINK_CONNECT_URL = 'tcp://localhost:5556'
    SINK_BIND_URL = 'tcp://*:5556'
    TASK_COUNT = 10
    WORKER_COUNT = 2

    def __init__(self):
        self.worker_connect_latch = CountDownLatch(Sample.WORKER_COUNT)
        """workerの接続完了を待ち合わせるためのラッチ"""

        self.worker_quit_latch = CountDownLatch(Sample.WORKER_COUNT)
        """workerの終了を待ち合わせるためのラッチ"""

    def exec(self):
        """サンプルの処理を実施します。"""
        # ----------------------------------------------------------------------
        # PUSH-PULL パターン
        # ----------------------------------------------------------------------
        # PUSH-PULL パターンは、「分割統治法」。パイプラインのようにデータをフェーズで処理して
        # 最終的に目的地へと通知する。
        #
        # 登場人物は以下の３つ。
        #   - ventilator -- 送風機を意味する。データを発信するもの
        #   - worker     -- 処理するものを意味する。 ventilatorからのデータを受信して
        #                   処理し、次に送り出す。
        #   - sink       -- くぼみ。データの目的地。 ventilator -> worker で処理した
        #                   データが行き着く先。
        #
        # PUSH-PULL パターンでは、 ventilator からのデータを複数の worker が処理し
        # sink に送るように処理する。
        #
        # 参考::
        #   [ventilator] http://zguide.zeromq.org/py:taskvent
        #   [worker    ] http://zguide.zeromq.org/py:taskwork
        #   [sink      ] http://zguide.zeromq.org/py:tasksink
        # ----------------------------------------------------------------------
        ventilator_proc = mp.Process(
            target=Sample.ventilator,
            args=(self.worker_connect_latch, self.worker_quit_latch))

        workers_proc = [
            mp.Process(target=Sample.worker, args=(i, self.worker_connect_latch, self.worker_quit_latch))
            for i in range(Sample.WORKER_COUNT)
        ]

        sink_proc = mp.Process(target=Sample.sink, args=())

        # 起動
        sink_proc.start()
        ventilator_proc.start()
        for w in workers_proc:
            w.start()

        # 終了
        sink_proc.join()
        ventilator_proc.join()
        for w in workers_proc:
            w.join()

    @staticmethod
    def ventilator(worker_connect_latch: CountDownLatch, worker_quit_latch: CountDownLatch):
        """データの送り出しを行う"""
        #
        # データの送り元を構築
        #
        context = zmq.Context()
        sender = context.socket(zmq.PUSH)
        sender.bind(Sample.VENTILATOR_BIND_URL)

        #
        # sink側に今からデータの同期が始まることを
        # 通知するために 値「0」 を送る
        # (sink 側は 待ち合わせのためにこのデータを最初に待っている)
        #
        sink = context.socket(zmq.PUSH)
        sink.connect(Sample.SINK_CONNECT_URL)

        # worker が 接続完了して、最初のrecvを実行するまで待機
        # これを行わないと、複数の worker が動いてくれない
        # 一つの worker のみが動作してしまう。
        # (タスクデータを送り出してから最初にrecvしたworkerが全データを処理してしまうため)
        #
        # worker_latch にて待機が解除された段階で、 worker が接続まで完了しているが
        # 実際に最初の recv　を呼び出すまでに、少しの待ちが必要となるため、sleep している。
        worker_connect_latch.await()
        time.sleep(1)

        # バッチ処理の開始を通知
        print('[ventilator] --> START: SEND 0 to sink', flush=True)
        sink.send(b'0')

        # 10個のタスクを送る
        for i in range(Sample.TASK_COUNT):
            sender.send_string(str(i))
        else:
            print(f'[ventilator] Total Expected Time: {Sample.TASK_COUNT - 1}sec', flush=True)

        # ZeroMQ が　メッセージを配信する時間を確保
        time.sleep(10)

        # worker に終了通知を送る
        for _ in range(Sample.WORKER_COUNT):
            sender.send_string('quit')

        worker_quit_latch.await()
        print('[ventilator] --> shutdown...')

    @staticmethod
    def worker(number: int, worker_connect_latch: CountDownLatch, worker_quit_latch: CountDownLatch):
        """データを処理する"""
        context = zmq.Context()

        receiver = context.socket(zmq.PULL)
        receiver.connect(Sample.VENTILATOR_CONNECT_URL)

        sender = context.socket(zmq.PUSH)
        sender.connect(Sample.SINK_CONNECT_URL)

        print(f'[worker-{number}] --> READY', flush=True)
        worker_connect_latch.count_down()

        while True:
            message = receiver.recv_string()
            print(f'[worker-{number}] --> recv {message}', flush=True)

            if message == 'quit':
                print(f'[worker-{number}] --> shutdown...')
                break

            sender.send_string(message)
            time.sleep(1)

        worker_quit_latch.count_down()

    @staticmethod
    def sink():
        """処理したデータを受信する"""
        context = zmq.Context()
        receiver = context.socket(zmq.PULL)
        receiver.bind(Sample.SINK_BIND_URL)

        # SENDER (ventilator) からの開始通知を待つ
        m = receiver.recv_string()
        print(f'[sink] --> START: RECV {m} from ventilator', flush=True)

        start_time = time.time()
        for i in range(Sample.TASK_COUNT):
            message = receiver.recv_string()
            print(f'[sink] recv --> {message}', flush=True)
        else:
            print(f'[sink] Total elapsed time: {round(time.time() - start_time, 1)}sec', flush=True)

        print('[sink] --> shutdown...')


def go():
    """サンプルを実行します。"""
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
