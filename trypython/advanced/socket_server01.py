"""
最もシンプルな形の Socket サーバ のサンプル

8888 番ポートで待ち受けて、クライアントから接続されたら 'hello' とだけ返し
CTRL+C で終了します。
"""

import contextlib
import socket

HOST = '127.0.0.1'
PORT = 8888
BACKLOG = 1


def start():
    """サーバを起動します"""
    with socket.socket() as sock:
        _configure(sock)
        try:
            _accept_endless(sock)
        except KeyboardInterrupt:
            # 終わり
            print('CTRL+C Pressed....shutting down')


def _configure(sock: socket.socket):
    sock.settimeout(1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
    sock.listen(BACKLOG)


def _accept_endless(sock: socket.socket):
    while True:
        with contextlib.suppress(socket.timeout):
            client, address = sock.accept()
            with client:
                print(f'Connect From {address}')
                client.sendall('hello'.encode('utf-8'))


if __name__ == '__main__':
    print('Start Server....')
    start()
    print('Shutdown Server....')
