# coding: utf-8

from pprint import pformat
from typing import Iterator, Any, Sequence, Tuple
from unicodedata import east_asian_width


def hr(message: Any = None) -> None:
    """
    水平線を出力します。
    中にメッセージを入れたい場合は引数 message を指定します。
    
    :param message: メッセージ 
    :return: 無し
    """
    print(f'----------------{message or ""}----------------')


def pr(prefix: str, message: Any, *args: Tuple) -> None:
    """
    指定された値を「＝」で繋いで出力します。
    argsに指定したオプション引数は ( ) で後ろに付与されます。

    :param prefix: プリフィックス
    :param message: メッセージ
    :param args: オプションで追加する情報
    :return: 無し
    """
    optional = args and f'({",".join(str(s) for s in args)})' or ''
    print(f'{prefix}={pformat(message)}{optional}')


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
    return sum([east_asian_width(c) in 'WF' and 2 or 1 for c in s])
