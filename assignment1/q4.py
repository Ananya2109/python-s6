#to print month and year
import calendar

dob = input("Enter your date of birth (DD/MM/YYYY): ")
day, month, year = map(int, dob.split('/'))

print(calendar.month_name[month], year)
