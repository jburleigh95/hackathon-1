def convert_to_12_hr(time_in_24_hr):
    time_list = time_in_24_hr.split(":")
    hour = int(time_list[0])
    if hour < 12:
        am_pm = "AM"
        if hour == 0:
            hour = 12
    else:
        am_pm = "PM"
        if hour > 12:
            hour -= 12
    time_list[0] = str(hour)
    time_in_12_hr = ":".join(time_list)
    print(f"{time_in_12_hr} {am_pm}")


print("Convert 24-hour time into 12-hour time.")
time_to_convert = input("Enter the 24 hour time you would like to convert (00:00): ")
convert_to_12_hr(time_to_convert)
