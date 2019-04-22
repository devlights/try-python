"""
argparse モジュールのサンプルです。
基本的な使い方について。

参考： http://bit.ly/2UXDCIG
"""
import argparse
import sys

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        #
        # argparse モジュールを使う場合の基本は以下の手順
        #
        # (1) argparse.ArgumentParser オブジェクト生成
        # (2) parser に add_argument メソッドで引数情報を追加
        # (3) parser.parse_args メソッド呼び出し
        # (4) args から 引数情報 を取得
        #
        parser = argparse.ArgumentParser(description='argparse sample01')

        parser.add_argument('indir', type=str, help='input directory')
        parser.add_argument('outdir', type=str, help='output directory')

        args = parser.parse_args()

        pr('type(parser)', type(parser))
        pr('type(args)', type(args))
        pr('args.indir', args.indir)
        pr('args.outdir', args.outdir)


def go():
    sys.argv.append('~/indir')
    sys.argv.append('~/outdir')

    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
