# coding: utf-8
from datetime import date, timedelta


def get_day(base_day, days_count=1, optional_holidays=(), optional_business_days=()):
    """
    基準日からN営業日[前or後]の日付を求めます。

    >>> from datetime import date

    >>> today = date(2017, 2, 6)
    >>> get_day(today, 5)
    datetime.date(2017, 2, 13)

    >>> get_day(today, -2)
    datetime.date(2017, 2, 2)

    >>> opt_holidays = [date(2017, 2, 13)]
    >>> get_day(today, 5, opt_holidays)
    datetime.date(2017, 2, 14)

    >>> opt_business_days = [date(2017, 2, 12)]
    >>> get_day(today, 5, optional_business_days=opt_business_days)
    datetime.date(2017, 2, 12)

    >>> get_day(today, 6, opt_holidays, opt_business_days)
    datetime.date(2017, 2, 14)
    
    >>> from datetime import datetime
    >>> d1 = datetime(2017, 2, 6)
    >>> get_day(d1)
    Traceback (most recent call last):
    AssertionError: base_day is not type(date)
    
    >>> d1 = date(2017, 2, 6)
    >>> opt_busi_days = (datetime(2017, 2, 13), datetime(2017, 2, 14))
    >>> get_day(d1, optional_business_days=opt_busi_days)
    Traceback (most recent call last):
    AssertionError: optional_business_days is not type(date)

    >>> d1 = date(2017, 2, 13)
    >>> opt_busi_days = (date(2017, 2, 13), date(2017, 2, 14))
    >>> opt_holi_days = (datetime(2017, 2, 11), datetime(2017, 2, 12))
    >>> get_day(d1, optional_business_days=opt_busi_days, optional_holidays=opt_holi_days)
    Traceback (most recent call last):
    AssertionError: optional_holidays is not type(date)

    :param date base_day: 基準日
    :param int days_count: 日数
    :param Tuple[date] optional_holidays: 追加で休日にする日付リスト
    :param Tuple[date] optional_business_days: 追加で営業日にする日付リスト
    :return: 対象日付
    """
    assert base_day, 'base_day is not specified'
    assert isinstance(base_day, date), 'base_day is not type(date)'
    assert all(isinstance(x, date) for x in optional_business_days), 'optional_business_days is not type(date)'
    assert all(isinstance(x, date) for x in optional_holidays), 'optional_holidays is not type(date)'

    forward = True if days_count > 0 else False
    count = abs(days_count)
    current = base_day
    while count > 0:
        current += timedelta(1 if forward else -1)
        weekday = current.weekday()

        if 5 <= weekday <= 6:  # 5=Saturday, 6=Sunday
            if current not in optional_business_days:
                continue
        if current in optional_holidays:
            continue

        count -= 1

    return current


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
