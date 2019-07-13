"""
pygments に関するサンプルです。
最も基本的な使い方を記載しています。

- pythonからpygmentsの操作方法
- pygmentize コマンドの使い方（コメントで）
"""
import os
import pathlib
import shlex
import subprocess
import sys

from pygments import highlight
from pygments.formatters import get_formatter_by_name
from pygments.lexers import get_lexer_by_name

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    """
    pygmentsのサンプルです。
    pythonのコードをハイライト付きでhtmlに出力します。
    """

    def exec(self):
        """処理を実行します。"""
        # --------------------------------------------------------------------------------
        # pygments の基本的な使い方
        #   - http://pygments.org/
        #
        # pygments を利用する場合、必要なオブジェクトは以下の3つ
        #   - コード： ハイライト表示対象のコード
        #   - 解析器(lexer)： コードを解析するためのオブジェクト
        #   - フォーマッタ： 最終的な出力を担当するオブジェクト
        #
        # lexer と formatter は、各実装クラスを直接つかってもいいが
        # 以下のヘルパー関数を使用しても取得できる
        #   - pygments.lexers.get_lexer_by_name()
        #     - 例えば、言語が python の場合は、"python" or "python3" となる
        #     - http://pygments.org/docs/lexers/
        #   - pygments.formatters.get_formatter_by_name()
        #     - 例えば、HTMLで出力したい場合は "html" となる
        #     - http://pygments.org/docs/formatters/
        #     - HtmlFormatterは便利だが、残念な事にHTML4形式で現状出力されてしまう。
        #
        # 必要なオブジェクトが揃ったら、後は pygments.highlight() に渡すと
        # 整形データが取得できる
        # --------------------------------------------------------------------------------
        code = """\
def hello():
    print('world')
    results = []
    for x in range(10):
        ressults.append(i for i in x)
        """
        lexer = get_lexer_by_name('python3')
        formatter = get_formatter_by_name('html', linenos=True, full=True, encoding='utf-8')

        # formatter に対して, 共通パラメータ [encoding] を指定した場合
        # 結果として受け取るデータの型は、bytes になる。指定していない場合、str となる。
        # HtmlFormatter にて encoding を指定しない場合、 charset の値が None となることに注意。
        html = highlight(code, lexer, formatter)
        if hasattr(html, 'decode'):
            html = html.decode('utf-8')
        pr('pygments.html', html)

        file_path = (pathlib.Path.home() / 'pygments_test.html').as_posix()
        with open(file_path, 'w') as out_fp:
            out_fp.write(html)

        preserve_file = True
        try:
            if sys.platform == 'win32':
                cmd = shlex.split(f'cmd /C start {file_path}')
            else:
                cmd = shlex.split(f'open {file_path}')
            subprocess.check_call(cmd, shell=False)
        finally:
            if not preserve_file:
                os.unlink(file_path)

        # --------------------------------------------------------------------------------
        # pygmentize コマンドの利用
        # pygments をインストールすると pygmentize という専用コマンドもインストールされる。
        # このコマンドを利用すると、pythonスクリプトを書かなくてもハイライト付きのデータが取得できる。
        #
        # 上のコードと同じような出力を得る場合は以下のようにする
        # $ pygmentize -f html -O linenos,full -o /tmp/pygments_test.html hello.py
        # --------------------------------------------------------------------------------


def go():
    """サンプルを実行します。"""
    obj = Sample()
    obj.exec()
