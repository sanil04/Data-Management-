# ECOR 1042 Lab 5 - Individual submission for sort_students_time_selection function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Ali El Shennawy"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101274917"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-003"

#==========================================#
# Place your sort_students_time_selection function after this line

def sort_students_time_selection(students: list[dict], order: str) -> list[dict]:
    """Returns a list of students with their StudyTime attributes sorted in ascending or descending order using the 
        selection sort algorithm.
        Precondition(s): order = "A" or "D"
        >>> sort_students_time_selection([{'Age': 17, 'StudyTime': 1.0, 'Failures': 3, 'Health': 3, 'Absences': 2, 'G1': 8, 'G2': 8, 'G3': 10}, {'Age': 16, 'StudyTime': 4.0, 'Failures': 0, 'Health': 3, 'Absences': 0, 'G1': 11, 'G2': 11, 'G3': 11}], "D")
        [{'Age': 16, 'StudyTime': 4.0, 'Failures': 0, 'Health': 3, 'Absences': 0, 'G1': 11, 'G2': 11, 'G3': 11}, {'Age': 17, 'StudyTime': 1.0, 'Failures': 3, 'Health': 3, 'Absences': 2, 'G1': 8, 'G2': 8, 'G3': 10}]
        >>> sort_students_time_selection([{'Age': 17, 'StudyTime': 1.0, 'Failures': 3, 'Health': 3, 'Absences': 2, 'G1': 8, 'G2': 8, 'G3': 10}, {'Age': 16, 'StudyTime': 4.0, 'Failures': 0, 'Health': 3, 'Absences': 0, 'G1': 11, 'G2': 11, 'G3': 11}], "A")
        [{'Age': 17, 'StudyTime': 1.0, 'Failures': 3, 'Health': 3, 'Absences': 2, 'G1': 8, 'G2': 8, 'G3': 10}, {'Age': 16, 'StudyTime': 4.0, 'Failures': 0, 'Health': 3, 'Absences': 0, 'G1': 11, 'G2': 11, 'G3': 11}]
        """
    
    minimum = 1000
    index = -1

    for student in students:
        if "StudyTime" not in student:
            print("\"StudyTime\" key is not present")
            return students

    for student in students:
        index += 1
        if student["StudyTime"] <= minimum:
            minimum = student["StudyTime"]
            current_student = students[index]
            students.pop(index)
            students.insert(0, current_student)
          
    if order == "D":
        students.reverse()

    return students

# Do NOT include a main script in your submission
