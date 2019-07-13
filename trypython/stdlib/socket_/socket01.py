"""
socket モジュールのサンプルです

基本的な使い方について。ブロッキング IO を利用しているサンプルです

REFERENCES:: http://bit.ly/2O07odl
             http://bit.ly/2O0ddaD
             http://bit.ly/2NZgd72
"""
import itertools
import multiprocessing
import socket

from trypython.common.commoncls import SampleBase, timetracer


# noinspection PyMethodMayBeStatic
class Sample(SampleBase):
    def exec(self):
        server_process = multiprocessing.Process(target=self.launch_server, args=())
        client_process = multiprocessing.Process(target=self.launch_client, args=())

        server_process.start()
        client_process.start()

        client_process.join()
        server_process.join()

        client_process.close()
        server_process.close()

    def launch_client(self):
        with timetracer('CLIENT'):
            sock = socket.socket()
            host = socket.gethostname()
            port = 12345

            sock.connect((host, port))

            data = b'hoge hoge' * 10 * 512
            assert sock.send(data)
            print(f'[CLIENT] {len(data)} bytes sended...')

            sock.close()
            print('[CLIENT] socket.close()')

    def launch_server(self):
        with timetracer('SERVER'):
            sock = socket.socket()
            host = socket.gethostname()
            port = 12345

            sock.bind((host, port))
            sock.listen(5)

            while True:
                conn, addr = sock.accept()

                counter = itertools.count(start=1)
                data = conn.recv(4096)
                while data:
                    print(f'[SERVER] {next(counter)} {len(data)} bytes receive')
                    data = conn.recv(4096)
                else:
                    print('[SERVER] data received...')

                conn.close()
                print('[SERVER] socket.close()')

                break


def go():
    obj = Sample()
    obj.exec()
