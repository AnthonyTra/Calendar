from dotw import get_dotw, dotw_index
from events import get_events_binary_search

# This index is used in the main function to print the months according to the month's number.
month_index = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

def validate_input(date_string):
    """Validates the user input and returns the date in a form of a tuple."""
    # This is to check if the characters are not special characters or letters.
    i = 0
    chars_to_check = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for char in chars_to_check:
        i += 1
        if char in date_string:
            break
        elif i == 9:  # If it reaches the end of the list and there are no numbers, then return none
            print("Not a valid input")
            return None

    # Can declare variables after we have tested for special characters or letters
    month, day, year = date_string.split('-')  # Sets the values into 3 different variables
    month = int(month)
    day = int(day)
    year = int(year)
    dates = [0, 0, 0]
    leap_year = False

    # Validates if it is a valid month
    if 1 <= month <= 12:  # If the number of the months is in between 1 and 12, it is a valid month
        dates[0] = month  # We assign it to the array if it is a valid month
    else:
        print("Not a valid month")
        return None

    # Validates if it is a leap year
    if year % 4 == 0:  # In order for it to be a leap year, the year has to be divisible by 4
        if year % 100 == 0:  # If it is divisible by 100, then it must be divisible for 400, for it to be a leap year
            if year % 400 == 0:
                leap_year = True
            elif year % 400 != 0:
                leap_year = False
        elif year % 100 != 0:  # If the year is not divisible by 100 but divisible by 4 then it is a leap year.
            leap_year = True

    # Validates if it is a 31 day month.
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if 1 <= day <= 31:
            dates[1] = day  # If that day is in range of that months values then we assign the day to the list
        else:
            print("Not a valid date for the 31 day month date input.")
            return None

    # Validates if it is a 30 day month.
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if 1 <= day <= 30:
            dates[1] = day  # If that day is in range of that months values then we assign the day to the list
        else:
            print("Not a valid date for the 30 day month date input.")
            return None

    # Validates the days of the month for February if it is a leap year or not.
    elif month == 2 and leap_year:
        if 1 <= day <= 29:
            dates[1] = day  # If that day is in range of February's leap year values then we assign the day to the list
        else:
            print("Not a valid February date range.")
            return None
    elif month == 2 and not leap_year:
        if 1 <= day <= 28:
            dates[1] = day  # If that day is in range of February's year values then we assign the day to the list
        else:
            print("Not a valid February date range.")
            return None

    # Validates if it is a year above 1000 AD.
    if year >= 1000:
        dates[2] = year
    else:
        print("Year is not in the range of the calender.")
        return None

    # Turns the list to a tuple
    dates_tuple = tuple(dates)
    return dates_tuple

def next_date(date):
    """Returns the next day in a form of a tuple."""
    date_list = list(date)
    month = date_list[0]
    day = date_list[1]
    year = date_list[2]
    leap_year = False

    # Validates if it is a leap year
    if year % 4 == 0:  # In order for it to be a leap year, the year has to be divisible by 4
        if year % 100 == 0:  # If it is divisible by 100, then it must be divisible for 400, for it to be a leap year
            if year % 400 == 0:
                leap_year = True
            elif year % 400 != 0:
                leap_year = False
        elif year % 100 != 0:  # If the year is not divisible by 100 but divisible by 4 then it is a leap year.
            leap_year = True

    # Calculates the next day for a 31 day month.
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if 1 <= day <= 30:  # If day is in between 1-30 add 1 to the day
            date_list[1] += 1
        elif day == 31:  # If it is the 31st day set the day back equal to one.
            date_list[1] = 1
            if 1 <= month <= 11:  # Then we determine if the month is in between January and November
                date_list[0] += 1  # We add one to the month if it is
            elif month == 12:  # If it is December on the 31 day, then set the month = 1 and add a year to the date.
                date_list[0] = 1  # If it is the 31st of December then we set the month back to January
                date_list[2] += 1  # If it is the 31st of December then we add one to the year.

    # Calculates the next day for a 30 day month
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if 1 <= day <= 29:
            date_list[1] += 1  # If that value is in between 1 and 29, then we add one to the day
        elif day == 30:  # If that day is the 30th, then we set the day = 1 and we add one to the month
            date_list[0] += 1
            date_list[1] = 1

    # Calculates the next day for February
    elif month == 2:
        if leap_year:
            if 1 <= day <= 28:
                date_list[1] += 1  # If it is a leap year on a February and in between 1-28 days then we add one to day
            elif day == 29:
                date_list[0] += 1  # If it is on the 29th day then we set the day equal to one and add one to the month
                date_list[1] = 1
        elif not leap_year:
            if 1 <= day <= 27:  # If it is not a leap year and in between 1-27 days then we add one to day
                date_list[1] += 1
            elif day == 28:  # If it is on the 28th day then we set the day equal to one and add one to the month
                date_list[0] += 1
                date_list[1] = 1

    dates = tuple(date_list)  # Turns the list into a tuple
    return dates

def previous_date(date):
    """Returns the previous date in the form of a tuple."""
    date_list = list(date)
    month = date_list[0]
    day = date_list[1]
    year = date_list[2]
    previous_month = month - 1
    leap_year = False

    # Validates if it is a leap year
    if year % 4 == 0:  # In order for it to be a leap year, the year has to be divisible by 4
        if year % 100 == 0:  # If it is divisible by 100, then it must be divisible for 400, for it to be a leap year
            if year % 400 == 0:
                leap_year = True
            elif year % 400 != 0:
                leap_year = False
        elif year % 100 != 0:  # If the year is not divisible by 100 but divisible by 4 then it is a leap year.
            leap_year = True

    # Does the previous day for january
    if month == 1:
        if day == 1:  # If it is new years then we set the day to 31st of December and subtract one from the year
            date_list[0] = 12
            date_list[1] = 31
            date_list[2] -= 1
        elif 2 <= day <= 31:  # If the day is in between 2 and 31 then subtract one from the day
            date_list[1] -= 1

    # Does previous day for February
    if month == 2:
        if day == 1:  # If the day is the 1st then we set it back to the 31st and subtract the month
            date_list[0] -= 1
            date_list[1] = 31
        elif 2 <= day <= 29:  # If the day is in between 2 and 29 then subtract one from the day
            date_list[1] -= 1

    # Calculates the previous day for a 31 day month excluding January.
    if month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if day == 1:
            if previous_month == 2:  # If it is March, then we set the month back one
                date_list[0] -= 1
                if leap_year:  # If it is a leap year then we set the day equal to 29
                    date_list[1] = 29
                elif not leap_year:  # If it isn't a leap year then set the equal to 28
                    date_list[1] = 28
            elif previous_month == 4 or previous_month == 6 or previous_month == 9 or previous_month == 11:
                date_list[0] = previous_month  # If the previous month was a 30 day month then we set the day to 30
                date_list[1] = 30
            else:
                date_list[0] = previous_month
                date_list[1] = 31  # If the previous month was a 31 day month then we set the day to 31
        elif 2 <= day <= 31:
            date_list[1] -= 1

    # Does previous day for the 30 day months
    if month == 4 or month == 6 or month == 9 or month == 11:
        if day == 1:
            if previous_month == 3 or previous_month == 5 or previous_month == 8 or previous_month == 10:
                date_list[0] = previous_month  # If the previous month was a 31 day month then we set the day to 31
                date_list[1] = 31
        elif 2 <= day <= 30:  # If the day is in between 2-30 then subtract one from the day
            date_list[1] -= 1

    dates = tuple(date_list)  # Turns the list into a tuple
    return dates


if __name__ == "__main__":
    """Takes the user inputted date and prints out the week of that date."""
    date = input("Enter a date (mm-dd-yyyy):")  # Asks the user for the date
    date = validate_input(date)  # Validates the date the user entered
    dotw = get_dotw(date)  # Gets day of the week for that date

    for i in range(dotw, 0, -1):  # Sets the date back to Sunday of that week
        date = previous_date(date)
    for i in range(7):  # Loops through the week starting with Sunday
        print(dotw_index[get_dotw(date)] + ",", month_index[date[0]], date[1])  # Prints the day that the for loop is on
        events = get_events_binary_search(date)  # Gets the events for that day using the binary search function
        if len(events) == 0:  # If there are no events print out that there is no events
            print("- No events")
        else:
            for event in events:  # If there are events then we loop through the events and print them out
                print("-", event)
        date = next_date(date)  # We then go to the next day after an iteration of this loop
