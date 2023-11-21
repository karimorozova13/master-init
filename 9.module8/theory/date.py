from datetime import datetime

current_date = datetime.now()
print(current_date.date())
print(current_date.time())
print(current_date.weekday()) # strat from Monday, from idx 0

my_bd = datetime(year=2023, month=9, day=13,hour=14, minute=45)
# print(my_bd)

future_month = (current_date.month % 12) +1
future_year =current_date.year + int(current_date.month / 12)
future_date = datetime(future_year, future_month, 1)

print(current_date< future_date)
print(current_date)
print(future_date)

# timedelta - defference detween dates
bd_2023 = datetime(year=2023, month=9, day=13)
bd_2022 = datetime(year=2022, month=9, day=13)
diference = bd_2023 - bd_2022
print(diference)

