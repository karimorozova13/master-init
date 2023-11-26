import calendar


def get_days_in_month(month, year):
    days_31 = [1,3,5,7,8,10,12]
    days_30 = [4,6,9,11]
    if month in days_30:
        return 30
    elif month in days_31:
        return 31
    else:
        if calendar.isleap(year):
            return 29
        return 28


print(get_days_in_month(2,2020))