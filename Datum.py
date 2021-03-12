# d, m = list(map(int, input().split()))
# days = ('Monday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
# days_in_months = {0: 1, 1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
# day_of_the_year = 0
# for i in range(m):
#     day_of_the_year += days_in_months[i]
#
# day_of_the_year += d
# print(days[day_of_the_year % 7])

import datetime
days = ['Monday', 'Tuesday', 'Wednesday','Thursday','Friday', 'Saturday', 'Sunday']
day,month = map(int,input().split())
d = datetime.datetime(2009, month, day).weekday()
print(days[d])