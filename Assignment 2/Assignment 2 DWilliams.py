# Program Name: Lab1.py (use the name the program is saved as)
# Course: IT3883/Section Module 1
# Student Name: David Williams
# Assignment Number: Assignment 2
# Due Date: 02/18/ 2026
# Purpose: Program that creates a list with springs
# Resources:


import statistics #import statistics for average-mean
grades = open("Assignment2input.txt", "r") # Open the external file

# For loop for importing names and grades
for line in grades:
    parts = line.split()

    student_name = parts[0]
    student_grade = list(map(int, parts[1:]))

    average = statistics.mean(student_grade) #averaging the grades

    print(f"{student_name} {average: .2f}") # Printing name and grade average

grades.close()


