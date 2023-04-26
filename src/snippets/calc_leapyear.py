import datetime

def is_leap_year(year=None):
    """Determine if current year, or argument, is a leapyear"""
    if year is None:
        year = datetime.date.today().year
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
