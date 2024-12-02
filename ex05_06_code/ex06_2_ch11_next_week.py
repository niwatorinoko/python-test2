from datetime import datetime, timedelta

# Get the current date and time
now = datetime.now()

# Calculate the number of days until the next week starts
days_to_next_week = 7 - now.weekday()

# Define the date format
date_format = "%Y-%m-%d (%a)"

# Loop through the range of dates from days_to_next_week until the end of the week
for i in range(0+days_to_next_week, 7+days_to_next_week):
    # Calculate the date of the ith day
    next_day = now + timedelta(days=i)
    
    # Format and print the date
    print(next_day.strftime(date_format))
