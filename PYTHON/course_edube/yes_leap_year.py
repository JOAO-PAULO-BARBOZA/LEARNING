def is_year_leap(year):
    return ((year % 4 == 0) and (year % 100 != 0)) or \
           ((year % 100 == 0) and (year % 400 == 0))


def days_in_month(year, month):

    year = is_year_leap(year)
    months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    days_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month not in months:
        return None
    if year and months.index(month) == 1:
        return 29
    else:
        return days_months[month - 1]


def day_of_year(year, month, day):
    yr = is_year_leap(year)

    day_month = days_in_month(year, month)

    if day_month != day:
        return None
    return day_month


print(day_of_year(2000, 12, 30))


test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
days_in_month(2000, 2)