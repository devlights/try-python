# coding: utf-8

from typing import Iterable, Iterator, Any


def pr(prefix: str, message: str) -> None:
    """
    指定された値を「＝」で繋いで出力します。

    :param prefix: プリフィックス
    :param message: メッセージ
    :return: 無し
    """
    print(f'{prefix}={message}')


def chunks(sequence: Iterable, chunk_size: int = 1) -> Iterator[Any]:
    """
    指定されたシーケンスを指定されたチャンクに分割します.

    :param sequence: シーケンス
    :param chunk_size: チャンクサイズ
    :return: Iterator[Any]
    """
    for i in range(0, len(sequence), chunk_size):
        yield sequence[i:i + chunk_size]
