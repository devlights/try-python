"""
aiohttp モジュールのサンプルです

基本的な使い方について

REFERENCES:: http://bit.ly/2O2lmeU
             http://bit.ly/2O08oy3
"""
import asyncio
from asyncio import Future
from typing import List, Dict

import aiohttp

from trypython.common.commoncls import SampleBase


async def fetch_async(index: int, url: str) -> Dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.read()
            return {
                'index': index,
                'resp': response,
                'length': len(html),
                'url': url
            }


def build_futures() -> List[Future]:
    urls = [
        'https://www.google.co.jp/',
        'https://stackoverflow.com/',
        'https://www.yahoo.co.jp/',
        'https://devlights.hatenablog.com/',
        'https://docs.python.org/3.7/index.html',
        'https://docs.python.org/ja/3/'
    ]

    futures = [asyncio.ensure_future(fetch_async(i, url)) for i, url in enumerate(urls, start=1)]
    return futures


class Sample(SampleBase):
    def exec(self):
        # 結果を元の順序で取得したい場合は asyncio.gather を使う
        future = asyncio.wait(build_futures(), return_when=asyncio.ALL_COMPLETED)
        done, pending = asyncio.get_event_loop().run_until_complete(future)

        for r in done:
            tr = r.result()
            print(f'{tr["index"]} {tr["url"]} {tr["length"]} bytes')


def go():
    obj = Sample()
    obj.exec()
