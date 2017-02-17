# coding: utf-8

"""
reモジュールのサンプルです。
"""
import re

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        #
        # re.match() は、先頭からの一致を行う
        # 戻り値は、Matchオブジェクトとなる
        #
        test_string01 = 'hello world'
        m = re.match(r'^h.*d$', test_string01)
        if m:
            pr('type(m)', type(m))
            pr('m.group()', m.group())

        pr('---------END-----------', 're.match')

        #
        # re.findall() は、全体検索を行う。
        # 戻り値は文字列のリストとなる
        #
        test_string02 = 'hello hello hello world'
        matches = re.findall(r'hello', test_string02)
        if matches:
            pr('type(matches)', type(matches))
            pr('matches count', len(matches))
            pr('matches', matches)

        pr('---------END-----------', 're.findall')

        #
        # re.search() は、全体から最初の一致を探す。
        # 戻り値は、Matchオブジェクトとなる
        #
        test_string03 = 'world hello'
        matches = re.search(r'hello', test_string03)
        if matches:
            pr('type(matches)', type(matches))
            pr('m.group()', matches.group())
            pr('m.groups()', matches.groups())
            pr('matches', matches)

        pr('---------END-----------', 're.search')

        #
        # re.finditer() は、全体検索を行い見つかった部分を iterable で返す
        # 戻り値は、Matchオブジェクトのiterableとなる
        #
        matches = re.finditer(r'hello', test_string02)
        for x in matches:
            pr('type(x)', type(x))
            pr('x.group()', x.group())
            pr('x.groups()', x.groups())
            pr('x', x)

        pr('---------END-----------', 're.finditer')


def go():
    obj = Sample()
    obj.exec()


if __name__ == '__main__':
    go()
