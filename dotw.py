dotw_index = {
    0: "Sunday",
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday"
}

def get_doomsday_dotw(year):
    """Retrieves the doomsday for that year by using the Doomsday formula."""
    # Setting variables for the Conway formula
    century = (year // 100) * 100  # Gets the century for the year entered
    century_index = century % 400  # Gets the beginning part of the century index
    target_year = year % century  # Gets the last two numbers of that year
    century_twelve = target_year // 12
    century_twelve_remainder = target_year % 12
    century_four = century_twelve_remainder // 4

    # Index for that year
    if 0 <= century_index // 100 < 1:  # I is 0 when the century index is equal to 0
        i = 2
    elif 1 <= century_index // 100 < 2:  # I is 0 when the century index is equal to 1
        i = 0
    elif 2 <= century_index // 100 < 3:  # I is 0 when the century index is equal to 2
        i = 5
    else:
        i = 3

    # Doomsday formula
    doomsday = (i + century_twelve + century_twelve_remainder + (century_four % 7)) % 7

    return doomsday

def get_dotw(date):
    """Gets the day of the week for the date inputted."""
    leap_year = False
    difference = 0
    month = date[0]
    day = date[1]
    year = date[2]

    # Determines if it is a leap year or not
    if year % 4 == 0:  # In order for it to be a leap year, the year has to be divisible by 4
        if year % 100 == 0:  # If it is divisible by 100, then it must be divisible for 400, for it to be a leap year
            if year % 400 == 0:
                leap_year = True
            elif year % 400 != 0:
                leap_year = False
        elif year % 100 != 0:  # If the year is not divisible by 100 but divisible by 4 then it is a leap year.
            leap_year = True

    # Determines the difference for the months that are effected by the leap year.
    if month == 1 and leap_year:
        difference = day - 4  # We get the difference by subtracting the inputted date with the doomsday date
    elif month == 2 and leap_year:
        difference = day - 29

    # Determines the difference for the months that are not effected by the leap year.
    if month == 1 and not leap_year:
        difference = day - 3
    elif month == 2 and not leap_year:
        difference = day - 28
    elif month == 3:
        difference = day - 14
    elif month == 4:
        difference = day - 4
    elif month == 5:
        difference = day - 9
    elif month == 6:
        difference = day - 6
    elif month == 7:
        difference = day - 11  # We get the difference by subtracting the inputted date with the doomsday date
    elif month == 8:
        difference = day - 8
    elif month == 9:
        difference = day - 5
    elif month == 10:
        difference = day - 10
    elif month == 11:
        difference = day - 7
    elif month == 12:
        difference = day - 12

    dotw = (difference + get_doomsday_dotw(year)) % 7  # Formula for dotw
    return dotw
