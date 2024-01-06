# Typica; number of weeks left to live based on the average age being 90...
#
age = input("Enter your age in years:\n")

age_as_int = int(age)
years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
print(f"You have {days_remaining} days left.")
print(f"You have {weeks_remaining} weeks left.")
print(f"You have {months_remaining} months left")
print("Remember to make the MOST of them!!" )
