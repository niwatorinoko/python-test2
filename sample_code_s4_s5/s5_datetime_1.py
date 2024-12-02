from datetime import datetime, timedelta

# Find current time
dt = datetime.now()
print('\ncurrent datetime: ', dt)
print('current date    : ',  dt.date())
print('current date/time:', datetime.today())
print(dt.year, dt.month, dt.day)

print('current weekday:', datetime.today().weekday()) # Monday is 0
print('current weekday:', datetime.today().isoweekday()) # Monday is 1

# Create a datetime object for specific date and time
dt2 = datetime(2017, 3, 3, 0, 0, 0)
print('dt2 datetime:', dt2)

# compare datetime objects
print('dt2 is later than now(): ', dt2 > dt)

# timedelta data type
twodays = timedelta(days=2, hours=3)

dt_plus2 = dt + twodays 
print('dt_plus2 datetime:', dt_plus2)
print('dt_plus2 is later than now(): ', dt_plus2 > dt)

print()
print("strftime(): Convert datetime object into string format")
# strftime means string formatter, convert datetime object into string format"
# https://strftime.org/
print(dt.strftime('%Y/%m/%d %H:%M:%S'))  # note that stfrtime begins with a datetime object
print(dt.strftime('%B %d, %Y')) # January 01, 2018
print(dt.strftime('%I:%M %p')) # 00:00 AM/PM

print()
print("strptime():  Convert strings into datetime objects....")
# strptime means string parser, this converts a string format to datetime.
dt_object = datetime.strptime('March 4, 2017', '%B %d, %Y')
print(dt_object)

# print as specific fromat
print(dt_object.strftime('%B %d, %Y'))

# print in default format: xxxx-xx-xx
print(dt_object.date())

# convert unix timestamp string to readable date.
print()
print("Convert unix timestamp string to readable date....")

## get current timestamp since January 1, 1970
ts = datetime.now().timestamp()
print("local timestamp in secs: ", ts)

## convert timestamp to datetime object
dt4 = datetime.fromtimestamp(ts)

# print in default format
print(dt4.isoformat())

# print in specific format
print(dt4.strftime('%Y-%m-%d %H:%M:%S'))
print()

## convert timestamp to datetime object with specific timezone
from dateutil.tz import gettz, tzutc, tzlocal

# Specific format
fmt = '%Y-%m-%d %H:%M:%S %z'

# Specific timezones: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
tpe_tz = gettz('Asia/Taipei')
ber_tz = gettz("Europe/Berlin")
utc_tz = gettz("UTC")

dt5_local = datetime.fromtimestamp(ts, tzlocal())
# dt5_local = datetime.now(tzlocal())
# print in specific format
print("Local Time:")
print(dt5_local.strftime('%Y-%m-%d %H:%M:%S %z'))

# Converting between timezones
print("\nUTC Time: ")
dt5_utc = dt5_local.astimezone(utc_tz) #tzutc() 
print(dt5_utc.strftime(fmt))

print("\nLocal Time in Berlin: ")
dt5_berlin = dt5_local.astimezone(ber_tz)
print(dt5_berlin.strftime(fmt))

print("\nLocal Time in Taipei: ")
dt5_taipei = dt5_berlin.astimezone(tpe_tz)
print(dt5_taipei.strftime(fmt))
print()

# 如何取得今天日期的字串
today_str = datetime.now().strftime('%Y-%m-%d')
print("今天是： " + today_str)

today_str = str(datetime.now().date())
print("今天是： " + today_str)

today_str = datetime.now().strftime('%x')
print("今天是： " + today_str)

"""
    %a  Locale’s abbreviated weekday name.
    %A  Locale’s full weekday name.      
    %b  Locale’s abbreviated month name.     
    %B  Locale’s full month name.
    %c  Locale’s appropriate date and time representation.   
    %d  Day of the month as a decimal number [01,31].    
    %f  Microsecond as a decimal number [0,999999], zero-padded on the left
    %H  Hour (24-hour clock) as a decimal number [00,23].    
    %I  Hour (12-hour clock) as a decimal number [01,12].    
    %j  Day of the year as a decimal number [001,366].   
    %m  Month as a decimal number [01,12].   
    %M  Minute as a decimal number [00,59].      
    %p  Locale’s equivalent of either AM or PM.
    %S  Second as a decimal number [00,61].
    %U  Week number of the year (Sunday as the first day of the week)
    %w  Weekday as a decimal number [0(Sunday),6].   
    %W  Week number of the year (Monday as the first day of the week)
    %x  Locale’s appropriate date representation.    
    %X  Locale’s appropriate time representation.    
    %y  Year without century as a decimal number [00,99].    
    %Y  Year with century as a decimal number.   
    %z  UTC offset in the form +HHMM or -HHMM.
    %Z  Time zone name (empty string if the object is naive).    
    %%  A literal '%' character.
"""