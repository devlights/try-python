from typing import Match

from trypython.common.commonfunc import pr


def print_match_object(m: Match[str]):
    """指定された Match オブジェクトの情報を出力します."""
    pr('r.match', m)
    if m:
        pr('\tgroups', m.groups())
        pr('\tmatch', m.group(0))
        pr('\tstart', m.start(0))
        pr('\tend', m.end(0))
        pr('\tspan', m.span(0))
