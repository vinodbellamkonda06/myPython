month_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


def is_leap(year):

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):

    if not 1 <= month <= 12:
        return "In Valid month"
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]


print(is_leap(2017))
print(days_in_month(2017, 3))


