# coding: utf-8

from typing import Iterator, Any, Sequence
from unicodedata import east_asian_width


def pr(prefix: str, message: Any) -> None:
    """
    指定された値を「＝」で繋いで出力します。

    :param prefix: プリフィックス
    :param message: メッセージ
    :return: 無し
    """
    print(f'{prefix}={message}')


def chunks(sequence: Sequence, chunk_size: int = 1) -> Iterator[Any]:
    """
    指定されたシーケンスを指定されたチャンクに分割します.

    :param sequence: シーケンス
    :param chunk_size: チャンクサイズ
    :return: Iterator[Any]
    """
    for i in range(0, len(sequence), chunk_size):
        yield sequence[i:i + chunk_size]


def unicode_width(s: str) -> int:
    """
    マルチバイトを考慮した文字幅を返します。

    :param s: 対象文字列
    :return: 文字幅
    """
    return sum(east_asian_width(c) in 'WF' and 2 or 1 for c in s)
