# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
# Initialize the highest score
highest_score = 0
# Loop through the list of scores
for score in student_scores:
  # Check if the current score is higher than the highest score
  if score > highest_score:
    # If it is, set the highest score to the current score
    highest_score = score
# Print the highest score
print(f"The highest score in the class is: {highest_score}")
