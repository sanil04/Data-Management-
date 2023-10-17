# ECOR 1042 Lab 4 - Individual submission for test2 function

# import check module here
from check import equal, summary
# import load_data module here
from load_data import load_data, student_school_list, student_health_list, student_age_list, student_failures_list, add_average
# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Neel Leuva"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101257773"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-003"

#==========================================#
# Do not modify the code alreayd provided.


def test_return_list_correct_lenght():
    # Complete the function with your test cases

    # test that student_school_list returns a list with the correct lenght (3 different test cases required)
    equal(len(student_school_list(
        "student-test.csv", "GP")), 3)
    equal(len(student_school_list(
        "student-test.csv", "MS")), 4)
    equal(len(student_school_list(
        "student-test.csv", "CF")), 3)

    # test that student_age_list returns a list  with the correct lenght (3 different test cases required)
    equal(len(student_age_list("student-test.csv", 18)), 4)
    equal(len(student_age_list("student-test.csv", 17)), 6)
    equal(len(student_age_list("student-test.csv", 16)), 2)

    # test that student_health_list returns a list  with the correct lenght (3 different test cases required)
    equal(len(student_health_list("student-test.csv", 3)), 8)
    equal(len(student_health_list("student-test.csv", 5)), 3)
    equal(len(student_health_list("student-test.csv", 4)), 3)

    # test that student_failures_list returns a list   with the correct lenght(3 different test cases required)
    equal(
        len(student_failures_list("student-test.csv", 0)), 11)
    equal(
        len(student_failures_list("student-test.csv", 3)), 1)
    equal(
        len(student_failures_list("student-test.csv", 2)), 2)

    # test that load_data returns a list  with the correct lenght (6 different test cases required)
    equal(
        len(load_data("student-test.csv", ("Failures", 1))), 1)
    equal(
        len(load_data("student-test.csv", ("School", "MB"))), 2)
    equal(
        len(load_data("student-test.csv", ("School", "BD"))), 3)
    equal(len(load_data("student-test.csv", ("Age", 15))), 3)
    equal(len(load_data(
        "student-test.csv", ("Health", 1))), 1)
    equal(len(load_data(
        "student-test.csv", ("School", "A"))), 0)

    # test that add_average returns a list   with the correct lenght (3 different test cases required)
    equal(len(add_average([{'School': 'GP', 'Age': 18, 'Studytime': 6.7,
                            'Failures': 1, 'Health': 3, 'Absences': 7, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'MB', 'Age': 15, 'Studytime': 1.0,
                                                                                                    'Failures': 0, 'Health': 3, 'Absences': 2, 'G1': 10, 'G2': 12, 'G3': 12}])), 2)
    equal(len(add_average([{'School': 'GP', 'Age': 18, 'Studytime': 6.7,
          'Failures': 1, 'Health': 3, 'Absences': 7, 'G1': 5, 'G2': 6, 'G3': 6}])), 1)

    equal(len(add_average([])), 0)

    summary()


# Do NOT include a main script in your submission
