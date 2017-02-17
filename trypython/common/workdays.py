# coding: utf-8
from datetime import date, timedelta


def get_day(base_day, days_count = 1, optional_holidays = [], optional_business_days = []) -> date:
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

    :param date base_day: 基準日
    :param int days_count: 日数
    :param List[date] optional_holidays: 追加で休日にする日付リスト
    :param List[date] optional_business_days: 追加で営業日にする日付リスト
    :return: 対象日付
    """
    assert base_day

    forward = True if days_count > 0 else False
    count = abs(days_count)
    current = base_day
    while count > 0:
        current += timedelta(1 if forward else -1)
        weekday = current.weekday()

        if 5 <= weekday <= 6:  # 5=Saturday, 6=Sunday
            if not current in optional_business_days:
                continue
        if current in optional_holidays:
            continue

        count -= 1

    return current
