names_string = "Angela, Ben, Jenny, Michael, Chloe"
names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆

import random
lucky_person = random.choice(names)
print(f"{lucky_person} is going to buy the meal today!")
