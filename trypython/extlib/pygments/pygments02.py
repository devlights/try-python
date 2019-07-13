"""
pygments に関するサンプルです。
pygments に備わっている ファイル名からの予想機能 をつかって 色付きcatコマンド みたいなのを実装しています。

usage:
  $ python -m trypython.extlib.pygments02 ファイルパス

  ファイルのエンコーディングを指定したい場合は以下のようにします。デフォルトは utf-8 です。

  $ python -m trypython.extlib.pygments02 ファイルパス --encoding euc-jp
"""
import argparse
import os

from pygments import highlight
from pygments.formatters.terminal import TerminalFormatter
from pygments.lexers import get_lexer_for_filename

from trypython.common.commoncls import SampleBase


class Sample(SampleBase):
    """
    pygments に関するサンプルです。
    pygments に備わっている ファイル名からの予想機能 をつかって 色付きcatコマンド みたいなのを実装しています。
    """

    def __init__(self, file_path: str, encoding: str) -> None:
        """
        オブジェクトを初期化します。

        :param file_path: ファイルパス
        :param encoding: エンコーディング
        """
        super().__init__()
        self.file_path = file_path
        self.encoding = encoding

    def exec(self) -> None:
        """
        処理を実行します。

        :return: なし
        """
        with open(self.file_path, mode='r', encoding=self.encoding) as in_fp:
            code = in_fp.read()

        lexer = get_lexer_for_filename(self.file_path)
        formatter = TerminalFormatter(bg='dark')
        result = highlight(code, lexer, formatter)

        print(result)


def _go(file_path: str, encoding: str) -> None:
    """
    サンプルを実行します。

    :param file_path: ファイルパス
    :param encoding: エンコーディング
    :return: なし
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f'target file is not found [{file_path}]')
    if os.path.isdir(file_path):
        raise ValueError(f'file_path should be file, NOT directory [{file_path}]')

    try:
        'helloworld'.encode(encoding)
    except LookupError:
        raise ValueError(f'invalid encoding [{encoding}]')

    obj = Sample(file_path, encoding)
    obj.exec()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path', type=str, help='target file path')
    parser.add_argument('--encoding', type=str, default='utf-8', help='file encoding (default: utf-8)')

    args = parser.parse_args()
    _go(args.file_path, args.encoding)
