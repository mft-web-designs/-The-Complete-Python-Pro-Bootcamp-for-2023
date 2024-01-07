line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
# split the input into two variables
horizontal = position[0]
vertical = int(position[1])

if horizontal == "A":
  if vertical == 1:
    line1[0] = "X"
  elif vertical == 2:
    line2[0] = "X"
  elif vertical == 3:
    line3[0] = "X"
elif horizontal == "B":
  if vertical == 1:
    line1[1] = "X"
  elif vertical == 2:
    line2[1] = "X"
  elif vertical == 3:
    line3[1] = "X"
elif horizontal == "C":
  if vertical == 1:
    line1[2] = "X"
  elif vertical == 2:
    line2[2] = "X"
  elif vertical == 3:
    line3[2] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
