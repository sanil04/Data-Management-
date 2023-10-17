# ECOR 1042 Lab 3 - Individual submission for student_school_list function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Neel Leuva"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101257773"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-003"


# ==========================================#
# Place your student_school_list function after this line


def student_school_list(file: str, school_name: str) -> list[dict]:
    """
    Takes in two inputs, the first being a file name and the second one being a name of a school. The function returns a list of dictionaries where each dictionary is the information of one student excluding the school name.

    Preconditions: File has to be student-mat.csv and school_name has to be GP, MB, CF, BD, or MS

    >>>student_school_list("student-mat.csv","GP")
    [{'Age:': 18, 'StudyTime:': 2.0, 'Failures:': 0, 'Health:': 3, 'Absences:': 6, 'G1:': 5, 'G2:': 6, 'G3:': 6}, {'Age:': 17, 'StudyTime:': 2.0, 'Failures:': 0, 'Health:': 3, ..., {'Age:': 17, 'StudyTime:': 1.0, 'Failures:': 3, 'Health:': 3, 'Absences:': 2, 'G1:': 8, 'G2:': 8, 'G3:': 10}]
    """
    # Takes the CSV file and converts it into a list of lists where each list is one student
    information = open(file, "r")
    list_of_lists = []
    for line in information:
        splitted_line = line.split(",")
        list_of_lists.append(splitted_line)
    list_of_lists.pop(0)

    # Convert each entry to the right data type
    for entry in list_of_lists:
        for i in range(1, 9):
            if i == 2:
                entry[i] = float(entry[i])
            else:
                entry[i] = int(entry[i])

    # Fiter through all the students and create a list of dictionaries with the
    list_of_students = []
    student = {}
    keys = [("Age", 1), ("StudyTime", 2), ("Failures", 3),
            ("Health", 4), ("Absences", 5), ("G1", 6), ("G2", 7), ("G3", 8)]
    for entry in list_of_lists:
        if entry[0] == school_name:
            for key in keys:
                student[key[0]] = entry[key[1]]

            list_of_students.append(student.copy())

    return list_of_students

# Do NOT include a main script in your submission
