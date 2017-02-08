# coding: utf-8

"""
ディクショナリについてのサンプルです。
"""
from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        #
        # ディクショナリ初期生成
        #   空のディクショナリを作成するには、{}とするかdict()とする
        #   空のディクショナリは、ifでFalse扱いとなる
        #
        # キーとして登録できるのは、イミュータブルなデータのみ。
        # リストやセットはミュータブルなのでキーとして利用できない
        # タプルはイミュータブルなのでキーとして利用できる
        #
        # 空リストの生成
        dict1 = {}
        pr('{}で作成', dict1)

        if not dict1:
            pr('{}のif判定', 'False')

        # 空リストの生成
        dict1 = dict()
        pr('dict()で作成', dict1)

        if not dict1:
            pr('dict()のif判定', 'False')

        # dict()に元データを渡して生成
        tuples = (('key1', 1), ('key2', 2),)
        dict2 = dict(tuples)
        pr('dict()に元データを渡して生成', dict2)

        lists = [['key1', 1], ['key2', 2]]
        dict2 = dict(lists)
        pr('dict()に元データを渡して生成', dict2)

        dict2 = dict([(x, y) for x, y in zip(['key1', 'key2'], [100, 200])])
        pr('dict()に元データを渡して生成', dict2)

        #
        # ディクショナリの統合
        # 同じキーが存在する場合は、updateに指定したディクショナリの方で上書きされる
        #
        dict3 = {'key1': 1, 'key2': 2, 'key99': 99}
        dict4 = {'key3': 3, 'key4': 4, 'key99': 100}

        dict3.update(dict4)

        pr('ディクショナリの統合', dict3)

        #
        # 要素の削除
        #
        del dict3['key99']
        pr('要素の削除', dict3)

        #
        # 要素のクリア
        #
        dict3.clear()
        pr('要素のクリア', dict3)

        #
        # キーが存在するかの確認
        #
        dict5 = {'key1': 1, 'key2': 2, 'key99': 99}
        pr('key1は存在するか', 'key1' in dict5)
        pr('key100は存在するか', 'key100' in dict5)

        #
        # 存在しないキーを指定すると例外が発生する (KeyError)
        #
        try:
            dict5['not_exists']
        except KeyError as e:
            pr('存在しないキーを指定', e)

        #
        # キーの一括取得
        # python2では keys() はリストを返す
        # python3では keys() はiterableなオブジェクトを返す
        # python3で、キーのリストを生成するには list(dict.keys()) とする
        #
        for key in dict5.keys():
            pr('key', key)

        #
        # 値の一括取得
        # python2では values() はリストを返す
        # python3では values() はiterableなオブジェクトを返す
        # python3で、値のリストを生成するには list(dict.values()) とする
        #
        for value in dict5.values():
            pr('value', value)

        #
        # キーと値ペアを一括取得
        # python2では items() はリストを返す
        # python3では items() はiterableなオブジェクトを返す
        # python3で、キーと値のペアのリストを生成するには list(dict.items()) とする
        #
        for key, value in dict5.items():
            pr('item', (key, value,))

        #
        # コピー
        #
        dict6 = dict5.copy()
        dict6['key1'] = 9999

        pr('dict5', dict5)
        pr('dict6', dict6)


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
