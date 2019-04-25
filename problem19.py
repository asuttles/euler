#    1 Jan 1900 was a Monday.
#
#    A leap year occurs on any year evenly divisible by 4,
#    but not on a century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century
# (1 Jan 1901 to 31 Dec 2000)?


dayOfWeek = 1
dayOfMonth = 0
year = 1900
month = 0

daysInMonthNormal = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
daysInMonthLeap = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


def nextWeekDay(day):
    day += 1
    return day % 7


def nextMonth(mon):
    mon += 1
    return mon % 12


def leapYearP(year):

    # Every 4th Year
    if year % 4 != 0:
        return False

    # But Not a Century Year
    if year % 100 == 0:

        # Unless it is a 4th century year
        if year % 400 == 0:
            return True
        else:
            return False

    else:
        return True
