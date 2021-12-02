
### Calculating the other dates for the week
```next_date``` will take a date tuple as its sole input and return a date tuple that represents the next date. For example, if it received ```(1, 23, 2023)``` as the argument value, it would return ```(1, 24, 2023)```.

```previous_date``` will take a date tuple as its sole input and return a date tuple that represents the previous date. For example, if it received ```(1, 23, 2023)``` as the argument value, it would return ```(1, 22, 2023)```.

Be careful to include edge cases, such as wrapping from one month to another, or even one year to another. Also make sure to account for February 29 if it is a leap year.

```read_events``` will read and parse the ```events.csv``` file. This is a Comma Separated Values (CSV) file. Each line of the CSV file represents one group of data points (in this case an event). The line will have values that are separated by commas. This file will contain (in order) the event's integer month, its integer day, and its name. For example, the New Year's Eve event will have a line in ```events.csv``` that looks like ```12,31,New Year's Eve```.

```sort_events``` will take a list of event tuples as its sole argument and return a sorted list of event tuples (in ascending order). 

```sort_events_fast``` will take a list of event tuples as its sole argument and return a sorted list of event tuples (in ascending order). 

```get_events_binary_search``` will take a date tuple as its sole argument. It will get a list of event tuples by calling ```read_events``` and sort them using either the ```sort_events``` function or the ```sort_events_fast``` function. It will then search the sorted list of event tuples to find all events that are on the same day as the input date tuple. If one or more events are found, it will return a list of the name(s) of the found event(s). If there is no matching event it will return an empty list. Binary search will only find one matching event, so you will need to repeat searching the list (removing any found events after each iteration) until there are no more matching events in the list.