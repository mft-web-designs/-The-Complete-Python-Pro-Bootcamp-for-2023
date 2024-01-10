age = input("How old are you?\n")
if age: #sing truthy for test
  age = int(age)
  if age >= 18 and age < 21:
    print("You can enter, but need a wristband.")
  elif age >= 21:
    print("You can enter and drink.")
  else:
    print("You can't enter little one :-(")
else:
  print("You didn't enter your age.")
