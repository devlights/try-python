"""[markdown の表を tsv に変換]

[事前準備]
$ python -m pip install --upgrade pip
$ python -m pip install pytablereader
$ python -m pip install pytablereader[md]
"""
import functools
import pathlib

import pytablereader as ptr


def main():
    in_files = [str(p) for p in pathlib.Path('.').glob('**/*.md') if not str(p).startswith('venv')]
    out_files = [in_file.replace('md', 'tsv') for in_file in in_files]

    for in_file, out_file in zip(in_files, out_files):
        with open(out_file, mode='w', encoding='utf-8') as fp_out:
            _write = functools.partial(print, file=fp_out)
            for t in ptr.MarkdownTableFileLoader(in_file).load():
                _write('\t'.join(t.header_list))
                for r in t.row_list:
                    _write('\t'.join(r))
                _write('\n')
