def read_events():
    """Reads the events in the csv file and returns the events in a list."""
    events = []
    f = open('events.csv', 'r')  # Opens the file so we can read it
    for event in f.read().split('\n'):  # Loops through the loop for every line in the csv file
        event = event.split(",")  # Takes the event and sets it equal to the 3 values in the line of that csv file
        if len(event) == 3:  # If the event has 3 values then we append it onto the events list
            events.append((int(event[0]), int(event[1]), event[2]))
    f.close()  # When done we close the file
    return events

def sort_events(event_list):
    """Sorts the event list using selection sort."""
    for i in range(len(event_list)):
        small = i
        for j in range(i + 1, len(event_list)):  # Compares i to the next element j.
            if event_list[j] < event_list[small]:
                small = j  # If the word at j is less then the smallest word, then set small = j
        event_list[i], event_list[small] = event_list[small], event_list[i]  # Swap elements if j is less then small
    return event_list

def partition(event_list, low, high):
    """This function partitions the set for quick sort."""
    i = low
    pivot = high
    for j in range(low, high):
        if event_list[j] < event_list[pivot]:
            event_list[i], event_list[j] = event_list[j], event_list[i]  # Swap elements if j is greater then the pivot
            i += 1  # Increments position of i if j is bigger then pivot
    event_list[i], event_list[pivot] = event_list[pivot], event_list[i]  # When done swap i and pivot in the list
    return i

def quick_sort(event_list, low, high):
    """Sorts the event list using quick sort."""
    if low < high:
        # Calls partition function to find the pivot
        pivot = partition(event_list, low, high)
        quick_sort(event_list, low, pivot - 1)
        # Recursively calls the function with the high position assigned one position to the left of the pivot
        quick_sort(event_list, pivot + 1, high)
        # Recursively calls the function with the low position one position to the right of the pivot
    return event_list

def sort_events_fast(event_list):
    """Calls the quick sort method and returns the sorted event list."""
    event_list = quick_sort(event_list, 0, len(event_list) - 1)  # Calls the quick sort method.
    return event_list

def greater_than(date, target_date):
    """Compares if the date is greater than the target date. (Helper function for binary search)"""
    if date[0] > target_date[0]:  # If date month is bigger than target date month then it returns true
        return True
    elif date[0] < target_date[0]:  # If the date month is smaller than the target date month then it returns false
        return False
    else:                           # else if it is equal then it compares the days
        if date[1] > target_date[1]:
            return True  # If the date for that day is bigger than the target date for that day then it returns true
        elif date[1] <= target_date[1]:
            return False  # If the date for that day is smaller than the target date for that day then it returns false

def less_than(date, target_date):
    if date[0] < target_date[0]:  # If date month is smaller than target date month then it returns true
        return True
    elif date[0] > target_date[0]:  # If date month is bigger than target date month then it returns false
        return False
    else:        # else if it is equal then it compares the days
        if date[1] < target_date[1]:
            return True  # If the date for that day is smaller than the target date for that day then it returns true
        elif date[1] >= target_date[1]:
            return False  # If the date for that day is bigger than the target date for that day then it returns false

def get_events_binary_search(date):
    """Searches and returns the events for that day using binary search."""
    event_list = sort_events_fast(read_events())
    matches = []
    looking = True

    while looking:
        low = 0
        high = len(event_list) - 1
        while low <= high:
            mid = (low + high) // 2
            if greater_than(event_list[mid], date):
                high = mid - 1  # Calls the function to test if the list date is bigger than the target date
            elif less_than(event_list[mid], date):
                low = mid + 1  # Calls the function to test if the list date is smaller than the target date
            else:
                counter = event_list.pop(mid)  # If they are the same date then pop the element off of the event list
                matches.append(counter[2])  # Append the popped list onto the matched list
                if high == len(event_list):
                    high -= 1  # Re-adjusts the high variable if high equals the same as the event list.
                    mid = (low + high) // 2  # Re-adjusts the mid variable if high equals the same as the event list.

        if event_list[mid][0] == date[0] and event_list[mid][1] == date[1]:
            # If the last mid variable is an event on the same day then pop it from original list.
            counter = event_list.pop(mid)
            matches.append(counter[2])  # Then append the event to our matches list

        looking = False  # Set to false so we don't enter an infinite loop
    return matches
