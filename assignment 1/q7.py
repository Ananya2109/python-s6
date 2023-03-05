#to convert total seconds to hour minute second format
time_in_seconds = int(input("Enter the time in seconds: "))
hours = time_in_seconds // 3600
minutes = (time_in_seconds % 3600) // 60
seconds = time_in_seconds % 60
formatted_time = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
print("The time in HH:MM:SS format is", formatted_time)
