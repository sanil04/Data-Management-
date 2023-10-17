# ECOR 1042 Lab 5 - Individual submission for sort_students_g_avg_insertion function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Neel Leuva"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101257773"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-003"

#==========================================#
# Place your sort_students_g_avg_insertion function after this line


def sort_students_g_avg_insertion(student_list: list[dict], ascend_or_descend: str) -> list[dict]:
    """
    Return a list which is sorted either ascending or descending by the G_avg key.

    Preconditions: ascend_or_descend should be A or D

    >>>sort_students_g_avg_insertion([{'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.67}, {'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6, 'G_Avg': 5.33}, {'Age': 15, 'StudyTime': 2.0, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10, 'G_Avg': 8.33}], "D")
    [{'Age': 15, 'StudyTime': 2.0, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10, 'G_Avg': 8.33}, {'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.67}, {'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6, 'G_Avg': 5.33}]

    >>>sort_students_g_avg_insertion([{'School': 'CF', 'Age': 15, 'StudyTime': 5.0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7, 'G_Avg': 7.0}, {'School': 'CF', 'Age': 17, 'StudyTime': 1.0, 'Health': 5, 'Absences': 0, 'G1': 7, 'G2': 6, 'G3': 0, 'G_Avg': 4.33}], "A")
    [{'School': 'CF', 'Age': 17, 'StudyTime': 1.0, 'Health': 5, 'Absences': 0, 'G1': 7, 'G2': 6, 'G3': 0, 'G_Avg': 4.33}, {'School': 'CF', 'Age': 15, 'StudyTime': 5.0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7, 'G_Avg': 7.0}]


    """
    j = 1
    while j < len(student_list):
        dict_of_key = student_list[j]
        i = j - 1
        while i >= 0 and 'G_Avg' in dict_of_key:
            if ascend_or_descend == 'A' and 'G_Avg' in student_list[i] and student_list[i]['G_Avg'] > dict_of_key['G_Avg']:
                student_list[i + 1] = student_list[i]
                i -= 1
            elif ascend_or_descend == 'D' and 'G_Avg' in student_list[i] and student_list[i]['G_Avg'] < dict_of_key['G_Avg']:
                student_list[i + 1] = student_list[i]
                i -= 1
            else:
                break
        student_list[i + 1] = dict_of_key
        j += 1

    for student in student_list:
        if 'G_Avg' not in student:
            return "G_Avg key is not present"

    return student_list


# Do NOT include a main script in your submission
