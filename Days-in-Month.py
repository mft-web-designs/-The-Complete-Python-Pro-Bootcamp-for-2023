def is_leap(year_to_check):
  if year_to_check % 4 == 0:
    if year_to_check % 100 == 0:
      if year_to_check % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

# TODO: Add more code here 👇
def days_in_month(year_to_check, month_to_check):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  #print(f"is_leap = {is_leap(year_to_check)}")
  if month == 2 and is_leap(year_to_check):
    days = 29
  else:
    days = month_days[month_to_check - 1]
  return days
  
#🚨 Do NOT change any of the code below 
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)
