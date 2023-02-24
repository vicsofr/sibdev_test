from datetime import datetime

from django.utils.timezone import get_default_timezone as tz

from deals.models import Deal


def deals_to_model(csv_list: list) -> list:
    """
    Transforms list with csv-data to comfort for Django bulk-create representation
    """
    deals_list = [
        Deal(
            customer=row[0],
            item=row[1],
            total=row[2],
            quantity=row[3],
            date=datetime_tz(row[4]),
        ) for row in csv_list[1:]
    ]
    return deals_list


def gems_by_two_more_clients(top_5_gems_list: list) -> list:
    """
    Takes list of aggregated gems from top 5 clients queryset and returns new list without gems that bought by less
    than 2 different clients
    """
    for row_num, gems in enumerate(top_5_gems_list):
        for_delete = []
        list_copy = top_5_gems_list.copy()
        list_copy.pop(row_num)
        beside = set([y for x in list_copy for y in x])
        for gem in gems:
            if gem not in beside:
                for_delete.append(gem)
        for item in for_delete:
            top_5_gems_list[row_num].remove(item)
    return top_5_gems_list


def datetime_tz(date_time):
    time_with_tz = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S.%f').replace(tzinfo=tz())
    return time_with_tz
