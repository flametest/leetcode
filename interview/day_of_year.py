#!/usr/bin/env python3

common_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# Determine if a given year is a leap year.
def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


# function to calculate the day of the year for that date
def day_of_year(year: int, month: int, day: int) -> int:
    # if this year is leap year
    year_day_list = leap_year if is_leap_year(year) else common_year
    # validate input
    if year < 1:
        return -1
    if month < 1 or month > 12:
        return -1
    if day < 1 or day > year_day_list[month - 1]:
        return -1
    # calculate
    res = 0
    for i in range(month - 1):
        res += year_day_list[i]
    res += day
    return res


if __name__ == '__main__':
    # invalid input
    assert day_of_year(2015, 2, 29) == -1
    assert day_of_year(2015, 4, 31) == -1
    assert day_of_year(2015, 13, 29) == -1
    assert day_of_year(2015, 13, 29) == -1
    assert day_of_year(2015, 12, 32) == -1
    assert day_of_year(2015, 1, -1) == -1
    assert day_of_year(2015, -1, 31) == -1
    assert day_of_year(-1, 1, 31) == -1
    assert day_of_year(-1, 1, 0) == -1
    assert day_of_year(2023, 2, 29) == -1
    # leap year
    assert day_of_year(2016, 1, 3) == 3
    assert day_of_year(2016, 2, 1) == 32
    assert day_of_year(2016, 2, 29) == 60
    assert day_of_year(2016, 3, 1) == 61
    assert day_of_year(2016, 12, 31) == 366
    # common year
    assert day_of_year(2015, 2, 28) == 59
    assert day_of_year(2015, 3, 1) == 60
    assert day_of_year(2015, 12, 31) == 365
