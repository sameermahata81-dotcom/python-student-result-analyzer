# Student Result Analyzer
# Author: Samir Mahata
# Description: A Python program that calculates total, average,
# highest, and lowest marks using for loops and lists.

print("\n---Students Result Calculation---\n")

subjects = []

for i in range(1, 6):
    mark = int(input(f"Enter your marks in subject {i}: "))
    subjects.append(mark)

total = 0
for mark in subjects:
    total = total + mark

highest = subjects[0]
lowest   = subjects[0]

for mark in subjects:
    if mark > highest:
        highest = mark

    if mark < lowest:
        lowest = mark

average = total / len(subjects)
print("\n")
print(f"Total Marks   : {total}")
print(f"Highest Mark  : {highest}")
print(f"Lowest Mark   : {lowest}")
print(f"Average Mark  : {average:.2f}")