# В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
# Во второй строке дано одно число days -- число дней.
#
# Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента исходной
# даты date пройдет число дней, равное days.
#
# Примечание:
# Для решения этой задачи используйте стандартный модуль datetime.
# Вам будут полезны класс datetime.date для хранения даты и класс datetime.timedelta﻿ для прибавления дней к дате.
import datetime
# input
# 2016 4 20
# 14

date = datetime.datetime.strptime(input(), "%Y %m %d")
delta = int(input())
new_date = datetime.timedelta(days=delta)
new_date = date + new_date
print(new_date.year, new_date.month, new_date.day)

# //// linux ////
# import datetime
#
# date = input().split()
# days = datetime.timedelta(days=int(input()))
#
# now = datetime.date(int(date[0]), int(date[1]), int(date[2]))
#
# will_be = now + days
#
# print(will_be.strftime('%Y %-m %-d'))