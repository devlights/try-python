# coding: utf-8

"""
ElementTreeモジュールについてのサンプルです。
"""
import xml.etree.ElementTree as et

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        #
        # 標準モジュールで用意されているXML関連モジュールで
        # 最も楽に扱えるものが ElementTree モジュール
        #
        # 他には、xml.dom, xml.sax がある
        #

        #
        # XMLツリーオブジェクトを生成
        # この他にも、文字列からパースするやり方もある
        #
        tree = et.ElementTree(file='sample01.xml')

        #
        # ルートオブジェクトを取得
        #
        languages = tree.getroot()
        pr('root-tag', languages)
        pr('len(root)', len(languages))

        #
        # DOMライクなループ
        #
        for language in languages:
            for child in language:
                if child.tag != 'name':
                    continue
                pr('dom', child.text)

        #
        # 指定した要素を iterate
        #
        for word in languages.iter('name'):
            pr('element-iter()', word.text)


def go():
    obj = Sample()
    obj.exec()
