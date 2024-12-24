def add_time(start: str, duration: str, day: str = "") -> str:
    """
    Add a duration to a start time and return the new time.

    Args:
    -----
        start (str): Start time in 12-hour format (e.g., '3:00 PM').
        duration (str): Duration in 'hours:minutes' format (e.g., '2:30').
        day (str, optional): Starting day of the week (e.g., 'Monday').

    Returns:
    --------
        str: New time in 12-hour format, with optional day and day count.
    """
    # Parse start time
    start_time, meridiem = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Convert start time to 24-hour format
    if meridiem == 'PM':
        start_hour += 12 if start_hour != 12 else 0
    elif meridiem == 'AM' and start_hour == 12:
        start_hour = 0

    # Add duration
    total_minutes = start_minute + duration_minute
    total_hours = start_hour + duration_hour + (total_minutes // 60)
    final_minutes = total_minutes % 60
    final_hours = total_hours % 24
    days_later = total_hours // 24

    # Determine AM/PM and adjust final_hours to 12-hour format
    meridiem = 'AM' if final_hours < 12 else 'PM'
    final_hours = final_hours if final_hours % 12 != 0 else 12
    final_hours = final_hours % 12 if final_hours % 12 != 0 else 12

    # Day of the week calculation (if provided)
    if day:
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        start_day_index = days_of_week.index(day.capitalize())
        final_day = days_of_week[(start_day_index + days_later) % 7]
        day_part = f", {final_day}"
    else:
        day_part = ""

    # Days later text
    if days_later == 1:
        day_count = " (next day)"
    elif days_later > 1:
        day_count = f" ({days_later} days later)"
    else:
        day_count = ""

    return f"{final_hours}:{final_minutes:02d} {meridiem}{day_part}{day_count}"


# Test cases
print(add_time('3:00 PM', '3:10'))  # 6:10 PM
print(add_time('11:30 AM', '2:32', 'Monday'))  # 2:02 PM, Monday
print(add_time('11:43 AM', '00:20'))  # 12:03 PM
print(add_time('10:10 PM', '3:30'))  # 1:40 AM (next day)
print(add_time('11:43 PM', '24:20', 'tueSday'))  # 12:03 AM, Thursday (2 days later)
print(add_time('6:30 PM', '205:12'))  # 7:42 AM (9 days later)
