def is_leap(year):
    """
    Docstring: The function that takes year as an input and checks whether or not it is a leap year or not and returns
    a boolean value as an answer
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]


y = int(input("Enter the year = "))  # Enter a year
m = int(input("Enter the month = "))  # Enter a month
days = days_in_month(y, m)
print(f"The days in the month {m} of year {y} are {days}")
