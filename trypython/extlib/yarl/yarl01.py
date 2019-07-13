"""
yarl モジュールについてのサンプルです

基本的な使い方について

REFERENCES:: http://bit.ly/2O2aD3R
             http://bit.ly/2O1BwoR
"""
from yarl import URL

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        # --------------------------------------------------------------
        # yarl (Yet another URL library)
        # ----------------------------------------
        # URL を 扱うためのライブラリ
        #
        # 標準モジュール urllib.parse.urlparse() を使っても同じようなことは
        # 可能だが、こちらの方が直感的に使いやすいように出来ている。
        #
        # pathlib.Path のように、 url / 'hoge' とやるとパスを結合してくれたりする
        #
        # 詳細な使い方は http://bit.ly/2O1BwoR に記載されている
        # --------------------------------------------------------------
        url = URL(r'https://devlights.hatenablog.com/entry/2019/03/13/192719')
        pr('yarl.URL', url)

        # 代表的なデータにはプロパティからアクセスできる
        pr('url.scheme', url.scheme)
        pr('url.host', url.host)
        pr('url.port', url.port)
        pr('url.query', url.query)
        pr('url.query_string', url.query_string)
        pr('url.path', url.path)

        # pathlib.Path のように / で結合できる
        new_url = url / 'hoge'
        pr('new_url', new_url)

        # with_xxx メソッドを使って新たなURLを構築できる
        new_url = new_url.with_query('val=111')
        pr('new_url2', new_url)
        pr('new_url2.query_string', new_url.query_string)

        # ヒューマンフレンドリーな形で取得する場合は human_repr() を使う
        pr('human_repr', new_url.human_repr())


def go():
    obj = Sample()
    obj.exec()
