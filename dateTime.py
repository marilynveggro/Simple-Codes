#datetime
import datetime

week_days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
week_num=datetime.date(2020,7,24).weekday()
print(week_days[week_num])

print('-----------------------------')


import datetime

date=str(input('Enter the date(for example:09 02 2019):'))
day_name= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
day = datetime.datetime.strptime(date, '%d %m %Y').weekday()
print(day_name[day])