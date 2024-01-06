print("The Love Calculator is calculating your score...")
name1 = input("What is your name?\n") # What is your name?
name2 = input("What is their name?\n") # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

#Concat both parties names into a single lowercase string
names_combined = name1.lower() + name2.lower()
#Count the number of times
t = names_combined.count("t")
r = names_combined.count("r")
u = names_combined.count("u")
e = names_combined.count("e")
true_score = t + r + u + e
l = names_combined.count("l")
o = names_combined.count("o")
v = names_combined.count("v")
e = names_combined.count("e")
love_score = l + o + v + e
#Combine the two scores
score = int(str(true_score) + str(love_score))
#Print the True Love score
if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
