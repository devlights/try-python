"""
pathlib モジュールについてのサンプルです。

REFERENCES::
  * https://docs.python.jp/3/library/pathlib.html
"""
import itertools as it
import pathlib
import tempfile

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr, hr


class Sample(SampleBase):

    def exec(self):
        """サンプル処理を実行します"""
        ###########################################################
        # pathlib の基本的な使い方
        # ---------------------------------------------------------
        # pathlib は、 3.4 から追加されたモジュール。
        # これまで、 os.path などを利用して処理していたパス操作を専門に担当する
        # モジュールである。
        #
        # pathlib モジュールで根幹となるアイテムは pathlib.Path となる。
        #
        # pathlib は、純粋パスと具象パスの２種類の概念を扱う。
        # クラス階層については、以下の公式ドキュメントを見るとわかりやすい。
        #   - https://docs.python.jp/3/library/pathlib.html
        #
        # 純粋パスは実際にOSに存在しているかどうかは関係なく処理できる。
        # なので、OSにアクセスすることなく処理を確認したい場合などに利用できるらしい。
        # （使ったことがありません。）
        #
        ###########################################################

        with tempfile.TemporaryDirectory() as tmpdir:
            #
            # (1) Path インスタンスの作成
            #
            hr('Path.ctor()')
            tmp_dir = pathlib.Path(tmpdir)
            pr('tmp_dir', tmp_dir)

            #
            # (2) 存在確認は、exists メソッドで行う
            #
            hr('Path.exists()')
            pr('パス (tmp_dir)', str(tmp_dir))
            pr('存在するか (/tmp)', tmp_dir.exists())

        #
        # (3) パスの結合は、 / で行える
        # (4) HOME ディレクトリの取得は クラスメソッド home を呼び出す
        #
        hr('Path::home() and path concat by "/"')
        home_dir = pathlib.Path.home()
        work_dir = pathlib.Path('PyCharmProjects')
        py_dir = pathlib.Path('try-python')

        src_dir = home_dir / work_dir / py_dir

        pr('パス (src_dir)', str(src_dir))
        pr(f'存在するか (src_dir)', src_dir.exists())

        #
        # (5) Path 内のファイル一覧を取得するには iterdir メソッドを呼び出す
        #     このメソッドは名前の通り イテレータ を返す
        # (6) ファイル名のみ（親ディレクトリを除く）を取得する場合は name プロパティを呼び出す
        # (7) ディレクトリかどうかは is_dir() を使う。ファイルかどうかは is_file() を使う。
        #
        hr('Path.iterdir() and Path.is_dir() and Path.is_file()')
        pr('ファイル一覧 (iterdir)', src_dir.iterdir())
        pr('ファイル一覧 (iterdir)', [x.name for x in src_dir.iterdir()])
        pr('ファイル一覧 (is_dir)', [x.name for x in src_dir.iterdir() if x.is_dir()])
        pr('ファイル一覧 (is_file)', [x.name for x in src_dir.iterdir() if x.is_file()])

        #
        # (8) 現在のカレントディレクトリは、 Path.cwd() クラスメソッドで取得できる。 (os.getcwd() と同じ)
        #
        hr('Path::cwd()')
        pr('カレントディレクトリ (cwd)', pathlib.Path.cwd())

        #
        # (9) シェルのように ~ を展開するには、 expanduser() メソッドを利用する。
        #
        hr('Path.expanduser()')
        pr('~ の展開 (expanduser)', pathlib.Path('~/work').expanduser())

        #
        # (10) ディレクトリの作成は mkdir(), 削除は rmdir() メソッドを利用する。
        #      対象がファイルの場合、削除は unlink() メソッドを利用する。
        #
        hr('Path.mkdir() and rmdir()')
        dir1 = src_dir / 'dir1'
        dir1.mkdir()
        pr('存在する (dir1)', dir1.exists())
        dir1.rmdir()
        pr('存在する (dir1)', dir1.exists())

        #
        # (11) Path は、ファイル操作用の API も備えている。 open メソッドでファイルをそのまま開ける。
        #
        hr('Path.open()')
        readme = src_dir / 'README.md'
        with readme.open(encoding='utf-8') as fp:
            lines = list(fp)
            pr('README', f'{len(lines)} 行')

        #
        # (12) 単純にファイルの中身を全取得したい場合だったら, open メソッドを呼ぶ必要はなく
        #      read_bytes() もしくは read_text() メソッドを呼び出せば取得できる。
        #
        # (*) 書き込む場合は、 write_bytes(), write_text() を利用できる
        #
        hr('Path.read_text()')
        all_text = readme.read_text(encoding='utf-8')
        lines = all_text.split('\n')[:-1]
        pr('README (read_text)', f'{len(lines)} 行')

        #
        # (13) glob モジュールのように条件にマッチするファイルを抽出したい場合は　glob() メソッドを利用する。
        #      glob() は、リストではなくジェネレータを返す。再帰的に抽出する場合は ** を利用する。
        #
        # (*) Path には、 rglob() というメソッドもあるが、これは glob() に ** を指定した場合と同じ動作。
        #
        hr('Path.glob()')
        all_py_files = src_dir.glob('**/*.py')
        top_10_files = it.islice(all_py_files, 10)
        top_10_names = [x.name for x in top_10_files]
        pr('glob (**/*.py)', top_10_names)

        hr('Path.rglob()')
        all_py_files = src_dir.rglob('*.py')
        top_10_files = it.islice(all_py_files, 10)
        top_10_names = [x.name for x in top_10_files]
        pr('rglob (*.py)', top_10_names)


def go():
    """処理を実行します"""
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
