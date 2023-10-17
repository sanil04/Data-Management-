# ECOR 1042 Lab 3 - Individual submission for student_failures_list function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Ali El Shennawy"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101274917"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-003"

#==========================================#
# Place your student_failures_list function after this line



def student_failures_list(file: str, number_of_failures: int) -> list[dict]:
    """Takes a list of students and returns a new list containing the students with a specific number of failures.
    Precondition(s): number_of_failures >= 0
    >>> student_failures_list("student-mat.csv", 0)
    [{'School': 'GP', 'Age': 18, 'Studytime': 2.0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'GP', 'Age': 17, 'Studytime': 2.0, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6},...,{'School': 'MS', 'Age': 19, 'Studytime': 1.0, 'Health': 5, 'Absences': 5, 'G1': 8, 'G2': 9, 'G3': 9}]
    >>> student_failures_list("student-mat.csv", 2)
    [{'School': 'GP', 'Age': 16, 'Studytime': 1.0, 'Health': 5, 'Absences': 14, 'G1': 6, 'G2': 9, 'G3': 8}, {'School': 'GP', 'Age': 15, 'Studytime': 2.0, 'Health': 5, 'Absences': 2, 'G1': 8, 'G2': 6, 'G3': 5},...,{'School': 'MS', 'Age': 20, 'Studytime': 2.0, 'Health': 4, 'Absences': 11, 'G1': 9, 'G2': 9, 'G3': 9}]
    >>> student_failures_list("student-mat.csv", 3)
    [{'School': 'GP', 'Age': 16, 'Studytime': 1.0, 'Health': 5, 'Absences': 14, 'G1': 6, 'G2': 9, 'G3': 8}, {'School': 'GP', 'Age': 15, 'Studytime': 2.0, 'Health': 5, 'Absences': 2, 'G1': 8, 'G2': 6, 'G3': 5},...,{'School': 'MS', 'Age': 20, 'Studytime': 2.0, 'Health': 4, 'Absences': 11, 'G1': 9, 'G2': 9, 'G3': 9}]
    """
    information = open(file, "r")
    list_of_lists = []
    for line in information:
        splitted_line = line.split(",")
        list_of_lists.append(splitted_line)
    list_of_lists.pop(0)  # list of columns

    for entry in list_of_lists:
        for i in range(1, 9):
            if i == 2:
                entry[i] = float(entry[i])  # convert each column's entries to appropriate data type
            else:
                entry[i] = int(entry[i])

    list_of_students = []
    student = {}
    keys = [("School", 0), ("Age", 1), ("StudyTime", 2), ("Failures", 3),  # each column and its indices
            ("Health", 4), ("Absences", 5), ("G1", 6), ("G2", 7),
            ("G3", 8)]
    for entry in list_of_lists:
        for key in keys:
            student[key[0]] = entry[key[1]]
        list_of_students.append(student.copy())
    list_of_failures = []

    for student in list_of_students:
        if student["Failures"] == number_of_failures:
            list_of_failures.append(student)

    for student in list_of_failures:
        del student["Failures"]

    return list_of_failures

