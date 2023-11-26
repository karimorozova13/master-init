from datetime import datetime


def get_days_from_today(date):
    today= datetime.now()
    new = date.split('-')
    full_date =datetime(year=int(new[0]), month=int(new[1]), day=int(new[2]))
    diference = today - full_date
    return diference.days
print(get_days_from_today("2021-10-09"))