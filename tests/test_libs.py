import io
import os
import re
import time

import trypython.common.commonfunc as libs


def test_chdir():
    # arrange
    orig_dir = os.path.abspath('.')
    dest_dir = os.path.abspath('/tmp')

    os.chdir(orig_dir)
    assert orig_dir == os.path.abspath(os.curdir)

    # act
    with libs.chdir(dest_dir) as current_dir:
        assert dest_dir == current_dir
        assert dest_dir == os.path.abspath(os.curdir)
        print(current_dir)

    # assert
    assert orig_dir == os.path.abspath(os.curdir)


def test_timetracer():
    # arrange
    file_ = io.StringIO()

    # act
    with libs.timetracer('test', file_):
        time.sleep(0.3)

    # assert
    file_.seek(io.SEEK_SET)
    result = str(file_.read()).strip()

    assert result
    re.match(r'[test] elapsed: .* seconds', result)


def test_open_inout():
    # arrange
    in_file = '/tmp/test_open_input.txt'
    out_file = '/tmp/test_open_input2.txt'

    with open(in_file, 'w', encoding='utf-8') as fp:
        fp.writelines(str(x) for x in range(10))

    try:
        # act
        # assert
        with libs.open_inout(in_file, out_file) as (in_fp, out_fp):
            assert in_fp
            assert out_fp
            assert in_file == in_fp.name
            assert out_file == out_fp.name
            assert in_fp.mode == 'r'
            assert out_fp.mode == 'w'
    finally:
        if os.path.exists(in_file):
            os.unlink(in_file)
        if os.path.exists(out_file):
            os.unlink(out_file)
