"""
ZeroMQ (PyZMQ) の PUSH-PULL パターンのサンプルです。

REFERENCES::
http://zguide.zeromq.org/page:all#Divide-and-Conquer
"""
import multiprocessing as mp
import time

import zmq

from trypython.common.commoncls import SampleBase


class Sample(SampleBase):
    """ZeroMQ の PUSH-PULL パターンのサンプルです。"""
    VENTILATOR_BIND_URL = 'tcp://*:5555'
    VENTILATOR_CONNECT_URL = 'tcp://localhost:5555'
    SINK_CONNECT_URL = 'tcp://localhost:5556'
    SINK_BIND_URL = 'tcp://*:5556'
    TASK_COUNT = 10
    WORKER_COUNT = 2

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
        # ** worker: 1 の場合 **
        # [worker-0] --> READY
        # [ventilator] --> START: SEND 0 to sink
        # [ventilator] Total Expected Time: 9sec
        # [sink] --> START: RECV 0 from ventilator
        # [worker-0] --> recv 0
        # [sink] recv --> 0
        # [worker-0] --> recv 1
        # [sink] recv --> 1
        # [worker-0] --> recv 2
        # [sink] recv --> 2
        # [worker-0] --> recv 3
        # [sink] recv --> 3
        # [worker-0] --> recv 4
        # [sink] recv --> 4
        # [worker-0] --> recv 5
        # [sink] recv --> 5
        # [worker-0] --> recv 6
        # [sink] recv --> 6
        # [worker-0] --> recv 7
        # [sink] recv --> 7
        # [worker-0] --> recv 8
        # [sink] recv --> 8
        # [worker-0] --> recv 9
        # [sink] recv --> 9
        # [sink] Total elapsed time: 9.0sec
        # ----------------------------------------------------------------------
        # ** worker: 2 の場合 **
        # [worker-0] --> READY
        # [worker-1] --> READY
        # [ventilator] --> START: SEND 0 to sink
        # [sink] --> START: RECV 0 from ventilator
        # [ventilator] Total Expected Time: 9sec
        # [worker-0] --> recv 0
        # [worker-1] --> recv 1
        # [sink] recv --> 0
        # [sink] recv --> 1
        # [worker-0] --> recv 2
        # [worker-1] --> recv 3
        # [sink] recv --> 2
        # [sink] recv --> 3
        # [worker-1] --> recv 5
        # [sink] recv --> 5
        # [worker-0] --> recv 4
        # [sink] recv --> 4
        # [worker-1] --> recv 7
        # [worker-0] --> recv 6
        # [sink] recv --> 7
        # [sink] recv --> 6
        # [worker-1] --> recv 9
        # [worker-0] --> recv 8
        # [sink] recv --> 8
        # [sink] recv --> 9
        # [sink] Total elapsed time: 4.0sec
        # ----------------------------------------------------------------------
        # ** worker: 4 の場合 **
        # [worker-1] --> READY
        # [worker-0] --> READY
        # [worker-2] --> READY
        # [worker-3] --> READY
        # [ventilator] --> START: SEND 0 to sink
        # [ventilator] Total Expected Time: 9sec
        # [sink] --> START: RECV 0 from ventilator
        # [worker-3] --> recv 0
        # [worker-0] --> recv 2
        # [worker-1] --> recv 1
        # [worker-2] --> recv 3
        # [sink] recv --> 2
        # [sink] recv --> 1
        # [sink] recv --> 0
        # [sink] recv --> 3
        # [worker-2] --> recv 7
        # [worker-1] --> recv 5
        # [worker-3] --> recv 4
        # [sink] recv --> 5
        # [sink] recv --> 7
        # [sink] recv --> 4
        # [worker-0] --> recv 6
        # [sink] recv --> 6
        # [worker-3] --> recv 8
        # [worker-1] --> recv 9
        # [sink] recv --> 8
        # [sink] recv --> 9
        # [sink] Total elapsed time: 2.0sec
        # ----------------------------------------------------------------------
        # ** worker: 10 の場合 **
        # [worker-1] --> READY
        # [worker-2] --> READY
        # [worker-0] --> READY
        # [worker-6] --> READY
        # [worker-5] --> READY
        # [worker-9] --> READY
        # [worker-4] --> READY
        # [worker-3] --> READY
        # [worker-8] --> READY
        # [worker-7] --> READY
        # [ventilator] --> START: SEND 0 to sink
        # [sink] --> START: RECV 0 from ventilator
        # [worker-2] --> recv 1
        # [worker-6] --> recv 2
        # [worker-0] --> recv 0
        # [worker-5] --> recv 3
        # [ventilator] Total Expected Time: 9sec
        # [worker-9] --> recv 4
        # [worker-4] --> recv 5
        # [sink] recv --> 0
        # [sink] recv --> 1
        # [sink] recv --> 2
        # [sink] recv --> 3
        # [worker-3] --> recv 6
        # [worker-8] --> recv 7
        # [worker-7] --> recv 8
        # [worker-1] --> recv 9
        # [sink] recv --> 4
        # [sink] recv --> 5
        # [sink] recv --> 6
        # [sink] recv --> 7
        # [sink] recv --> 8
        # [sink] recv --> 9
        # [sink] Total elapsed time: 0.0sec
        # ----------------------------------------------------------------------
        ventilator_proc = mp.Process(target=Sample.ventilator, args=())
        workers_proc = [
            mp.Process(target=Sample.worker, args=(i,))
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
    def ventilator():
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

        # worker が 接続完了するまで待機
        # これを行わないと、複数の worker が動いてくれない
        # 一つの worker のみが動作してしまう。
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

        time.sleep(0.5)
        print('[ventilator] --> shutdown...')

    @staticmethod
    def worker(number: int):
        """データを処理する"""
        context = zmq.Context()

        receiver = context.socket(zmq.PULL)
        receiver.connect(Sample.VENTILATOR_CONNECT_URL)

        sender = context.socket(zmq.PUSH)
        sender.connect(Sample.SINK_CONNECT_URL)

        print(f'[worker-{number}] --> READY', flush=True)
        while True:
            message = receiver.recv_string()
            print(f'[worker-{number}] --> recv {message}', flush=True)

            if message == 'quit':
                print(f'[worker-{number}] --> shutdown...')
                break

            sender.send_string(message)
            time.sleep(1)

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
