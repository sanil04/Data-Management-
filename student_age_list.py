# ECOR 1042 Lab 3 - Individual submission for student_age_list function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Sanil Srivastava"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101268578"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-003"

#==========================================#

def student_age_list(file: str, age: int) -> list[dict]:

    """
    Preconditions: The file entered must be "student-mat.csv", the age entered must be an int between 15 and 23 inclusive.
    
    >>>student_age_list("student-mat.csv",15)
    [{'School': 'GP', 'Studytime': 2.0, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}, {'School': 'GP', 'Studytime': 3.0,         'Failures': 0, 'Health': 5, 'Absences': 2, 'G1': 15, 'G2': 14, 'G3': 15}, ........... {'School': 'CF', 'Studytime': 2.0, 'Failures': 2, 'Health':       3,'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7}]


    >>>student_age_list("student-mat.csv",16)
    [{'School': 'GP', 'Studytime': 2.0, 'Failures': 0, 'Health': 5, 'Absences': 4, 'G1': 6, 'G2': 10, 'G3': 10}, {'School': 'GP', 'Studytime': 2.0,         'Failures': 0, 'Health': 5, 'Absences': 10, 'G1': 15, 'G2': 15, 'G3': 15}, ............ {'School': 'BD', 'Studytime': 1.0, 'Failures': 0, 'Health':     3, 'Absences': 0, 'G1': 8, 'G2': 9, 'G3': 8}]

    >>>student_age_list("student-mat.csv",17)
    [{'School': 'GP', 'Studytime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6}, {'School': 'GP', 'Studytime': 2.0,           'Failures': 0, 'Health': 1, 'Absences': 6, 'G1': 6, 'G2': 5, 'G3': 6}, ............. {'School': 'MS', 'Studytime': 1.0, 'Failures': 0, 'Health': 2,     'Absences': 3, 'G1': 14, 'G2': 16, 'G3': 16}]

    """
    information = open(file, "r")
    list_of_lists = []
    for line in information:
        splitted_line = line.split(",")
        list_of_lists.append(splitted_line)
    list_of_lists.pop(0)                        # list of row

    for entry in list_of_lists:
        for i in range(1, 9):
            if i == 2:
                entry[i] = float(entry[i])      # convert each row's entries to appropriate data type
            else:
                entry[i] = int(entry[i])

    list_of_students = []
    student = {}
    keys = [("School", 0), ("Studytime", 2), ("Failures", 3),                           
            ("Health", 4), ("Absences", 5), ("G1", 6), ("G2", 7), ("G3", 8)] # each row and its indices
    for entry in list_of_lists:
        if entry[1] == age:     # list students of a specific age
            for key in keys:
                student[key[0]] = entry[key[1]]

            list_of_students.append(student.copy())
    return list_of_students



# Do NOT include a main script in your submission
