# write your code here

# 1. Check if month is valid
def is_valid_month(month):
    return 1 <= month <= 12

# 2. Check if year is a leap year
def is_leap_year(year):
    return (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))

# 3. Check if month has 30 days
def has_30_days(month):
    return month in [4, 6, 9, 11]

# 4. Check if month has 31 days
def has_31_days(month):
    return month in [1, 3, 5, 7, 8, 10, 12]

# 5. Check if month has 28 days (February, not leap year)
def has_28_days(month, year):
    return month == 2 and not is_leap_year(year)

# 6. Check if month has 29 days (February, leap year)
def has_29_days(month, year):
    return month == 2 and is_leap_year(year)

# 7. Check if a date is valid
def is_valid_date(day, month, year):
    return (
        is_valid_month(month) and (
            (has_31_days(month) and 1 <= day <= 31) or
            (has_30_days(month) and 1 <= day <= 30) or
            (has_29_days(month, year) and 1 <= day <= 29) or
            (has_28_days(month, year) and 1 <= day <= 28)
        )
    )

