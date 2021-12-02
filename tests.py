from calendar import validate_input, next_date, previous_date
from dotw import get_doomsday_dotw, get_dotw
from events import read_events, get_events_binary_search, sort_events, sort_events_fast

# validate_input tests
assert validate_input("1-31-1820") == (1,31,1820)
assert validate_input("7-4-1900") == (7,4,1900)
assert validate_input("6-17-1923") == (6,17,1923)
assert validate_input("3-10-2047") == (3,10,2047)
assert validate_input("11-1-2230") == (11,1,2230)
assert validate_input("1-31-20") == None
assert validate_input("7-34-1900") == None
assert validate_input("16-17-1923") == None
assert validate_input("3-10-047") == None
assert validate_input("---") == None
assert validate_input("") == None

# next_date tests
assert next_date((1,31,1820)) == (2,1,1820)
assert next_date((7,4,1900)) == (7,5,1900)
assert next_date((6,17,1923)) == (6,18,1923)
assert next_date((3,10,2047)) == (3,11,2047)
assert next_date((12,31,2230)) == (1,1,2231)

# previous_date tests
assert previous_date((1,1,1820)) == (12,31,1819)
assert previous_date((7,4,1900)) == (7,3,1900)
assert previous_date((6,17,1923)) == (6,16,1923)
assert previous_date((3,10,2047)) == (3,9,2047)
assert previous_date((12,31,2230)) == (12,30,2230)

# get_doomsday_dotw tests
assert get_doomsday_dotw(1898) == 1
assert get_doomsday_dotw(1912) == 4
assert get_doomsday_dotw(1936) == 6
assert get_doomsday_dotw(1941) == 5
assert get_doomsday_dotw(1956) == 3
assert get_doomsday_dotw(1963) == 4
assert get_doomsday_dotw(2012) == 3
assert get_doomsday_dotw(2024) == 4
assert get_doomsday_dotw(2034) == 2
assert get_doomsday_dotw(2072) == 1
assert get_doomsday_dotw(2097) == 4

# get_dotw tests
assert get_dotw((3,27,1706)) == 6
assert get_dotw((12,13,1751)) == 1
assert get_dotw((4,5,1775)) == 3
assert get_dotw((5,13,1788)) == 2
assert get_dotw((11,14,1797)) == 2
assert get_dotw((4,27,1830)) == 2
assert get_dotw((5,30,1838)) == 3
assert get_dotw((9,14,1875)) == 2
assert get_dotw((10,6,1875)) == 3
assert get_dotw((4,17,1984)) == 2
assert get_dotw((1,8,2037)) == 4
assert get_dotw((5,5,2096)) == 6
assert get_dotw((12,5,2100)) == 0
assert get_dotw((3,2,2121)) == 0
assert get_dotw((7,29,2149)) == 2
assert get_dotw((2,1,2178)) == 0
assert get_dotw((11,26,2268)) == 4
assert get_dotw((8,7,2419)) == 3
assert get_dotw((9,17,2446)) == 1
assert get_dotw((1,18,2458)) == 5

# read_events tests
events = read_events()
assert events[0] == (1, 25, "Opposite Day")
assert events[12] == (11, 23, "Wolfenoot")
assert events[29] == (3, 8, "International Women's Day")

# sort_events tests
events = sort_events(read_events())
assert events[4] == (1, 25, "Opposite Day")
assert events[12] == (3, 8, "International Women's Day")
assert events[37] == (11, 23, "Wolfenoot")

# sort_events_fast tests
events = sort_events_fast(read_events())
assert events[4] == (1, 25, "Opposite Day")
assert events[12] == (3, 8, "International Women's Day")
assert events[37] == (11, 23, "Wolfenoot")

# get_events_search tests
assert get_events_binary_search((1, 1, 2021)) == ["New Year's Day"]
assert get_events_binary_search((2, 2, 2021)) == ["Groundhog's Day"]
assert get_events_binary_search((8, 13, 2021)) == ["Left Hander's Day"]
assert get_events_binary_search((11, 2, 2021)) == ["Dia de los Muertos", "All Soul's Day"] or get_events_binary_search((11, 2, 2021)) == ["All Soul's Day", "Dia de los Muertos"]
assert get_events_binary_search((11, 23, 2021)) == ["Wolfenoot"]
assert get_events_binary_search((1, 24, 2021)) == []
assert get_events_binary_search((8, 12, 2021)) == []
