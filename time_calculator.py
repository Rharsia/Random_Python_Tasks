# Write a function named add_time that takes in two required parameters and one optional parameter:

# a start time in the 12-hour clock format (ending in AM or PM)
# a duration time that indicates the number of hours and minutes
# (optional) a starting day of the week, case insensitive
# The function should add the duration time to the start time and return the result.

# If the result will be the next day, it should show (next day) after the time. If the result will be more than one day later, 
# it should show (n days later) after the time, where "n" is the number of days later.

# If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. 
# The day of the week in the output should appear after the time and before the number of days later.

# Below are some examples of different cases the function should handle. Pay close attention to the spacing and punctuation of the results.

### Examples
# add_time("3:00 PM", "3:10")
# # Returns: 6:10 PM

# add_time("11:30 AM", "2:32", "Monday")
# # Returns: 2:02 PM, Monday

# add_time("11:43 AM", "00:20")
# # Returns: 12:03 PM

# add_time("10:10 PM", "3:30")
# # Returns: 1:40 AM (next day)

# add_time("11:43 PM", "24:20", "tueSday")
# # Returns: 12:03 AM, Thursday (2 days later)

# add_time("6:30 PM", "205:12")
# # Returns: 7:42 AM (9 days later)

# Do not import any Python libraries. Assume that the start times are valid times. 
# The minutes in the duration time will be a whole number less than 60, but the hour can be any whole number.


weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# first example input
# start_time = "11:43 PM"
# add_this_time = "24:20"
# day = "tueSday"

def add_time(start_time, add_this_time, day = None):
    
    day_index = 0
    if day != None:
        # if user messed up the day string
        day = day.capitalize()  
        day_index = weekdays.index(day)


    # split the start time
    splitted_start = start_time.split()
    day_part = splitted_start[1]

    # find the start time
    start_time = splitted_start[0]

    # get the hours of the start time
    start_hours = int(start_time[:start_time.index(":")])

    # convert to 24h time
    if day_part == "PM":
        start_hours += 12

    # get the minutes
    start_minutes = int(start_time[start_time.index(":")+1:])

    # convert to minutes
    minutes1 = start_hours * 60 + start_minutes

    # get the hours to be added
    add_this_time = add_this_time

    # hours
    add_hours = int(add_this_time[:add_this_time.index(":")])

    # minutes
    add_minutes = int(add_this_time[add_this_time.index(":")+1:])

    # convert to minutes
    minutes2 = add_hours * 60 + add_minutes

    # add times together
    result_minutes = minutes1 + minutes2

    # convert back to time
    end_hours = result_minutes // 60
    end_minutes = result_minutes % 60


    # calculate the days
    days_later = 0
    if end_hours >= 24:
        days_later = end_hours // 24 
        end_hours -= 24 * days_later

    # calculate the day of the week
    day_index += days_later

    # day_index must be bewteen 0-6
    if day_index > 6:
        day_index = day_index % 7
    

    # calculate the part of the day
    if end_hours > 12:
        day_part = "PM"
        end_hours -= 12
    elif end_hours == 12 and end_minutes > 0:
        day_part = "PM"
    elif end_hours == 0:
        end_hours += 12
        day_part = "AM"
    else:
        day_part = "AM"


    # if minutes are single digits
    end_minutes = str(end_minutes)
    if len(end_minutes) == 1:
        end_minutes = "0" + end_minutes

    # print the result
    if day == None:
        if days_later == 0:
            print(f"{end_hours}:{end_minutes} {day_part}")
        elif days_later > 0:
            if days_later == 1:
                print(f"{end_hours}:{end_minutes} {day_part} (next day).")
            else:
                print(f"{end_hours}:{end_minutes} {day_part} ({days_later} days later).")
    else:
        if days_later == 0:
            print(f"{end_hours}:{end_minutes} {day_part}, {day}")
        elif days_later > 0:
            if days_later == 1:
                print(f"{end_hours}:{end_minutes} {day_part}, {weekdays[day_index]} (next day).")
            else:
                print(f"{end_hours}:{end_minutes} {day_part}, {weekdays[day_index]} ({days_later} days later).")



add_time("3:00 PM", "3:10")
add_time("11:30 AM", "2:32", "Monday")
add_time("11:43 AM", "00:20")
add_time("10:10 PM", "3:30")
add_time("11:43 PM", "24:20", "tueSday")
add_time("6:30 PM", "205:12")
add_time("3:30 PM", "2:12")
add_time("11:55 AM", "3:12")
add_time("9:15 PM", "5:30")
add_time("11:40 AM", "0:25")
add_time("2:59 AM", "24:00")
add_time("11:59 PM", "24:05")
add_time("8:16 PM", "466:02")
add_time("5:01 AM", "0:00")
add_time("3:30 PM", "2:12", "Monday")
add_time("2:59 AM", "24:00", "saturDay")
add_time("11:59 PM", "24:05", "Wednesday")
add_time("8:16 PM", "466:02", "tuesday")