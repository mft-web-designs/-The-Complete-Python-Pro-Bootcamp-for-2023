#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
bill = input("What was the total bill? $")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

# Calculate the various components of the bill
bill_float = float(bill)
tip_int = int(tip)
people_int = int(people)
tip_percent = tip_int / 100
tip_amount = bill_float * tip_percent
total_bill = bill_float + tip_amount
bill_per_person = total_bill / people_int
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
# Inform of the amount per person
print(f"Each person should pay: ${final_amount}")
