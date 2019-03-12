# coding: utf-8
import contextlib as ctx
import functools
import os
import sys
import time
from datetime import datetime
from pprint import pformat
from typing import Iterator, Any, Sequence, Tuple, Callable, Generator, IO, Optional
from unicodedata import east_asian_width


@ctx.contextmanager
def open_inout(in_file: str,
               out_file: str,
               in_enc: str = 'utf-8',
               out_enc: str = 'utf-8') -> Generator[Tuple[IO[str], IO[str]], None, None]:
    """
    指定した２つのファイルを片方は読み込み用、もう片方は書込み用で開きます。

    :param in_file: 入力用ファイルパス
    :param out_file: 出力用ファイルパス
    :param in_enc: 入力用ファイルのエンコーディング
    :param out_enc: 出力用ファイルのエンコーディング
    :return: 入力用ファイル、出力用ファイルのタプル
    """
    if not in_file or not out_file:
        raise ValueError('parameters must be set. [in_file, out_file]')
    if not in_enc or not out_enc:
        raise ValueError('parameters must be set. [in_enc, out_enc]')

    in_fp = open(in_file, mode='r', encoding=in_enc)
    out_fp = open(out_file, mode='w', encoding=out_enc)
    try:
        yield (in_fp, out_fp)
    finally:
        if in_fp:
            in_fp.close()
        if out_fp:
            out_fp.close()


@ctx.contextmanager
def chdir(directory: str = None) -> Generator[str, None, None]:
    """
    指定したディレクトリを一時的にカレントディレクトリに変更するコンテキストマネージャです。

    :param directory: 一時的にカレントディレクトリにするディレクトリ
    :return: 現在のカレントディレクトリ (yield の結果)
    """
    if directory is None or not os.path.exists(directory):
        raise ValueError('parameter: directory must be directory-path.')

    _orig_dir = os.path.abspath(os.path.curdir)
    try:
        os.chdir(directory)
        yield os.path.abspath(directory)
    finally:
        os.chdir(_orig_dir)


@ctx.contextmanager
def timetracer(message: Optional[str] = None, file: Optional[IO[str]] = None) -> Generator[None, None, None]:
    """
    処理の経過時間を出力するコンテキストマネージャです。

    :param message: メッセージ (デフォルトは [timetracer])
    :param file: 出力先 (デフォルトは sys.stdout)
    :return: なし
    """
    _start = datetime.now()
    try:
        yield
    finally:
        _diff = datetime.now() - _start
        _io = sys.stdout if file is None else file
        _message = 'timetracer' if message is None else message
        _log = f'[{_message}] elapsed: {_diff.seconds}.{_diff.microseconds} seconds'

        print(_log, file=_io)


def stopwatch(func: Callable) -> Callable:
    """
    デコレータ。
    関数呼び出しにかかった時間を出力します。

    :param func: 関数
    :return: 関数
    """

    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        start = time.perf_counter()
        results = func(*args, **kwargs)
        end = time.perf_counter()

        hr(f'ELAPSED TIME: {(end - start):0.3f}')

        return results

    return _wrapper


def hr(message: Any = None) -> None:
    """
    水平線を出力します。
    中にメッセージを入れたい場合は引数 message を指定します。
    
    :param message: メッセージ 
    :return: 無し
    """
    print(f'----------------{message or ""}----------------')


def pr(prefix: str, message: Any, *args: Any) -> None:
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


def is_py3() -> bool:
    """
    python 3.x 系かどうかを返します。

    :return: 3.x 系の場合はTrue, それ以外は False.
    """
    if sys.version_info >= (3, 0,):
        return True
    return False
