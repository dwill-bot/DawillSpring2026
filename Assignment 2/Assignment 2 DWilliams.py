# Program Name: Lab1.py (use the name the program is saved as)
# Course: IT3883/Section Module 2
# Student Name: David Williams
# Assignment Number: Assignment 2
# Due Date: 02/18/ 2026
# Purpose: Program that Averages grades from text file and output them in descending order
# Resources:W3schools.com


import statistics #import statistics for average-mean
grades = open("Assignment 2/Assignment2input.txt", "r") # Open the external file

results = []

# For loop for importing names and grades
for line in grades:
    parts = line.split()

    student_name = parts[0]
    student_grade = list(map(int, parts[1:]))

    average = statistics.mean(student_grade) #averaging the grades

    results.append((student_name, average)) # storing results


grades.close()

# pulling the average
def get_average(student_tuple):
    return student_tuple[1]

# Sort in descending order
results.sort(key= get_average, reverse=True)

for name, avg in results:
    print(f"{name} {avg:.2f}")


