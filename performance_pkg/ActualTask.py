
# Function 1: Calculate class average
def class_average(students):

    if len(students) == 0:
        raise ValueError("Student list cannot be empty")

    total = 0

    for student in students:
        marks = student["marks"]

        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100")

        total += marks

    average = total / len(students)

    return average


# Function 2: Find the topper
def topper_details(students):

    if len(students) == 0:
        raise ValueError("Student list cannot be empty")

    topper = max(students, key=lambda student: student["marks"])

    return topper["name"], topper["marks"]


# Function 3: Identify students needing support
def identify_support_students(students, threshold=40):

    if not 0 <= threshold <= 100:
        raise ValueError("Invalid threshold")

    return [
        student["name"]
        for student in students
        if student["marks"] < threshold
    ]
