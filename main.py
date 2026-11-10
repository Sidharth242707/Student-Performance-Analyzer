
# Import functions from our user-defined package

from performance_pkg import (
    class_average,
    topper_details,
    identify_support_students
)


# Student details
students = [
    {"name": "Arun", "marks": 85},
    {"name": "Rahul", "marks": 35},
    {"name": "Anu", "marks": 92},
    {"name": "Vishnu", "marks": 65}
]


# Display project title
print("================================")
print("   STUDENT PERFORMANCE ANALYZER")
print("================================")


# Calculate class average
average = class_average(students)
print("\nClass Average:", average)


# Find topper
name, marks = topper_details(students)
print("Topper:", name, "-", marks)


# Identify students needing support
support = identify_support_students(students)
print("Students Needing Support:", support)


# Testing invalid input
print("\n--- TESTING ---")

try:
    class_average([
        {"name": "Test", "marks": 120}
    ])
except ValueError as e:
    print("Invalid Input Test:", e)


# Testing edge case
print("Edge Case Test:",
      class_average([{"name": "Test", "marks": 0}]))

print("\nProgram completed successfully!")
