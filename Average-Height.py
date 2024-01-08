# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
# Initialize the sum of heights
sum_heights = 0
# Initialize the number of students
num_students = 0
# Loop through
while num_students < len(student_heights):
  # Add the height to the sum
  sum_heights += student_heights[num_students]
  # Increment the number of students
  num_students += 1
# Calculate the average
average_height = round(sum_heights / num_students)
# Print the average height
print(f"total height = {sum_heights}")
print(f"number of students = {num_students}")
print(f"average height = {average_height}")
