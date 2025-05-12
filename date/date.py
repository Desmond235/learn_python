import datetime

date = datetime.date(2025,1, 8)
today = datetime.date.today()

time = datetime.time(12,50,0)
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S %m-%d-%Y")

target_dateTime = datetime.datetime(2020, 4, 5, 9, 45, 8)
current_dateTime = datetime.datetime.now()

if target_dateTime < current_dateTime:
    print("Target date has passed")
else:
    print("Target date has not passed")