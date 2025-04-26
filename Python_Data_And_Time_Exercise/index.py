# Exercise 1: Print current date and time in Python
# from time import asctime, gmtime, strftime
# import datetime
# print(asctime())
# print(datetime.datetime.now())
# print("%Y-%m-%d %H:%M:%S",gmtime())

# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 2: Convert string into a datetime object
# from datetime import datetime
# date_string = "Feb 25 2020 4:20PM"
# datetime_object = datetime.strptime(date_string,'%b %d %Y %I:%M%p')
# print(datetime_object)

# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 3: Subtract a week (7 days)  from a given date in Python
# from datetime import datetime, timedelta
# given_date = datetime(2020, 2, 25)
# print("Diven Date","\n",given_date)

# days_to_subtract = 7
# res_date = given_date - timedelta(days=days_to_subtract)
# print("New Date","\n",res_date)


# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 4: Print a date in a the following format
# from datetime import datetime
# given_date = datetime(2020, 2, 25)
# print("Given Date is ","\n",given_date.strftime("%A %d %B %Y"))

# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 5: Find the day of the week of a given date
# from datetime import datetime
# given_date = datetime(2020, 7, 26)
# print(given_date.today().weekday())

# print(given_date.strftime("%A"))

# USING CALENDAR
# import calendar
# from datetime import datetime

# given_date = datetime(2020,7,26)
# weekday = calendar.day_name[given_date.weekday()]
# print(weekday)

# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 6: Add a week (7 days) and 12 hours to a given date
# from datetime import datetime,timedelta
# given_date = datetime(2020, 3, 22, 10, 0, 0)

# days_to_add = 7
# red_date = given_date+timedelta(days=days_to_add,hours=12)
# print(red_date)


# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 7: Print current time in milliseconds
# import time
# milliseconds  = int(round(time.time()*1000))
# print(milliseconds)

# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 8: Convert the following datetime into a string
# from datetime import datetime
# given_date = datetime(2020, 2, 25)
# strind_date = given_date.strftime("%Y-%m-%d %H:%M:%S")
# print(strind_date)

# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 9: Calculate the date 4 months from the current date
# from datetime import datetime
# from dateutil.relativedelta import relativedelta
# given_date = datetime(2020, 2, 25).date()

# months_to_add = 4
# new_date = given_date + relativedelta(month=+ months_to_add)
# print(new_date)


# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 10: Calculate number of days between two given dates
# from datetime import datetime
# date_1 = datetime(2020, 2, 25).date()
# date_2 = datetime(2020, 9, 17).date()

# delta = None
# if date_1 > date_2:
#     print("Date 1 is greater")
#     delta = date_1 - date_2
# else:
#     print("date 2 is greater")
#     delta = date_2 - date_1
# print("Difference is ",delta.days, " days")