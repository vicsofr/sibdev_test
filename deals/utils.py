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


def datetime_tz(date_time):
    time_with_tz = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S.%f').replace(tzinfo=tz())
    return time_with_tz
