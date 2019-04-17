# coding: utf-8
"""
Pythonでのループ最適化のサンプルです。
以下のURLの情報にインスパイアされてサンプルつくりました。

http://stackoverflow.com/questions/43827281/python-loop-optimization
"""
import collections
import csv
import pathlib
import tempfile
import zipfile
from timeit import timeit
from typing import List, Dict

import requests


class PrepareProc:
    def __init__(self, base_dir: str) -> None:
        super().__init__()

        self.zip_file_name = r'ken_all.zip'
        self.csv_file_name = r'ken_all.csv'

        self.work_dir = pathlib.Path(base_dir)
        self.zip_file_path = self.work_dir / self.zip_file_name
        self.csv_file_path = self.work_dir / self.csv_file_name

        # 郵便番号データダウンロードURL
        self.data_url = r'http://www.post.japanpost.jp/zipcode/dl/kogaki/zip/ken_all.zip'
        # 郵便番号データファイルのエンコーディング
        self.csv_encoding = 'sjis'

    def download(self) -> None:
        if self.zip_file_path.exists():
            return

        with open(self.zip_file_path, mode='wb') as writer:
            writer.write(requests.get(self.data_url).content)

    def extract(self) -> None:
        if self.csv_file_path.exists():
            return

        with zipfile.ZipFile(str(self.zip_file_path.absolute()), mode='r') as z:
            z.extractall(self.work_dir)

    def read(self) -> List[List[str]]:
        with open(self.csv_file_path, mode='rt', encoding=self.csv_encoding, newline='') as f:
            reader = csv.reader(f)
            return [line for line in reader]


# noinspection PyUnresolvedReferences
class _ProcValidateMixin:
    def pre_validate(self) -> None:
        assert self._lines[0][0] != '北海道'

    def post_validate(self) -> None:
        assert self._lines[0][0] == '北海道'


class SlowProc(_ProcValidateMixin):
    def __init__(self, lines: List[List[str]]) -> None:
        super().__init__()
        self._lines = lines
        self._mapping = self._make_mapping()

    def __call__(self, *args, **kwargs) -> None:
        for line in self._lines:
            for key in self._mapping:
                if line[0] in self._mapping[key]:
                    line[0] = key

    def _make_mapping(self) -> Dict[str, list]:
        mapping = collections.defaultdict(list)
        for line in self._lines:
            mapping[line[6]].append(line[0])

        return mapping


class NormalProc(_ProcValidateMixin):
    def __init__(self, lines: List[List[str]]) -> None:
        super().__init__()
        self._lines = lines
        self._mapping = self._make_mapping()

    def __call__(self, *args, **kwargs) -> None:
        for line in self._lines:
            for key in self._mapping:
                if line[0] in self._mapping[key]:
                    line[0] = key

    def _make_mapping(self) -> Dict[str, set]:
        mapping = collections.defaultdict(set)
        for line in self._lines:
            mapping[line[6]].add(line[0])

        return mapping


class FastProc(_ProcValidateMixin):
    def __init__(self, lines: List[List[str]]) -> None:
        super().__init__()
        self._lines = lines
        self._mapping = self._make_mapping()

    def __call__(self, *args, **kwargs) -> None:
        for line in self._lines:
            item = self._mapping[line[0]]
            if item:
                line[0] = item

    def _make_mapping(self) -> Dict[str, str]:
        mapping = collections.defaultdict(str)
        for line in self._lines:
            mapping[line[0]] = line[6]

        return mapping


if __name__ == '__main__':
    with tempfile.TemporaryDirectory() as tmpdir:
        print(f'base_dir={tmpdir}')

        prepare = PrepareProc(tmpdir)
        prepare.download()
        prepare.extract()

        # 全件処理させると、とても時間がかかるので20000行に絞って実施。
        # 実際の行数は、2017/05/10時点で124115行ある。
        slow = SlowProc(prepare.read()[:20000])
        slow.pre_validate()
        print(f'slow={round(timeit(slow, number=1), 3)}')
        slow.post_validate()

        normal = NormalProc(prepare.read())
        normal.pre_validate()
        print(f'normal={round(timeit(normal, number=1), 3)}')
        normal.post_validate()

        fast = FastProc(prepare.read())
        fast.pre_validate()
        print(f'fast={round(timeit(fast, number=1), 3)}')
        fast.post_validate()
