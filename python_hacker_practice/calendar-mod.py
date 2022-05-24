# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

user_date=list(map(int,input().split()))
# print(user_date)
print(calendar.day_name[calendar.weekday(user_date[2],user_date[0],user_date[1])].upper())
