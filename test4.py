# ECOR 1042 Lab 4 - Individual submission for test4 function

#import check module here
from check import equal, within, summary
#import load_data module here
from load_data import student_school_list, student_health_list, student_failures_list, student_age_list, add_average, load_data

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Ali El Shennawy"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101274917"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-003"

#==========================================#
#Do not modify the code alreayd provided.

def test_add_average():
    
    equal(len(add_average(student_school_list("student-test.csv", "GP"))),
            len(student_school_list("student-test.csv", "GP")))
    
    equal(len(add_average(student_health_list("student-test.csv", 5))),
            len(student_health_list("student-test.csv", 5)))
    
    equal(len(add_average(student_age_list("student-test.csv", 18))),
            len(student_age_list("student-test.csv", 18)))
    
    equal(len(add_average(student_failures_list("student-test.csv", 3))),
            len(student_failures_list("student-test.csv", 3)))
    
    equal(len(add_average(load_data("student-test.csv", ("All", 0)))),
          len(load_data("student-test.csv", ("All", 0))))
    
    equal(len(add_average(student_school_list("student-test.csv", "NA"))),
          len(student_school_list("student-test.csv", "NA")))
    
    
    
    equal(len(add_average(student_school_list("student-test.csv", "GP"))[0].keys()),
          len(student_school_list("student-test.csv", "GP")[0].keys()) + 1)
    
    equal(len(add_average(student_health_list("student-test.csv", 5))[0].keys()),
          len(student_health_list("student-test.csv", 5)[0].keys()) + 1)
    
    equal(len(add_average(student_age_list("student-test.csv", 18))[0].keys()),
          len(student_age_list("student-test.csv", 18)[0].keys()) + 1)
    
    equal(len(add_average(student_failures_list("student-test.csv", 0))[0].keys()),
          len(student_failures_list("student-test.csv", 0)[0].keys()) + 1)    
    
    equal(len(add_average(load_data("student-test.csv", ("All", 0)))[0].keys()),
          len(load_data("student-test.csv", ("All", 0))[0].keys()) + 1)
    
    
    
    within(
        add_average(student_school_list("student-test.csv", "MB"))[0]["G_Avg"],
        (((student_school_list("student-test.csv", "MB")[0]["G1"] +
           student_school_list("student-test.csv", "MB")[0]["G2"] +
           student_school_list("student-test.csv", "MB")[0]["G3"]) / 3)), 0.01)
    
    within(
        add_average(student_health_list("student-test.csv", 1))[0]["G_Avg"],
        (((student_health_list("student-test.csv", 1)[0]["G1"] +
           student_health_list("student-test.csv", 1)[0]["G2"] +
           student_health_list("student-test.csv", 1)[0]["G3"]) / 3)), 0.01)
    
    within(
        add_average(student_age_list("student-test.csv", 15))[0]["G_Avg"],
        (((student_age_list("student-test.csv", 15)[0]["G1"] +
           student_age_list("student-test.csv", 15)[0]["G2"] +
           student_age_list("student-test.csv", 15)[0]["G3"]) / 3)), 0.01)
    
    within(
        add_average(student_failures_list("student-test.csv", 2))[0]["G_Avg"],
        (((student_failures_list("student-test.csv", 2)[0]["G1"] +
           student_failures_list("student-test.csv", 2)[0]["G2"] +
           student_failures_list("student-test.csv", 2)[0]["G3"]) / 3)), 0.01)
    
    within(
        add_average(load_data("student-test.csv", ("All", 0)))[0]["G_Avg"],
        (((load_data("student-test.csv", ("All", 0))[0]["G1"] +
           load_data("student-test.csv", ("All", 0))[0]["G2"] +
           load_data("student-test.csv", ("All", 0))[0]["G3"]) / 3)), 0.01)        

    summary()

# Do NOT include a main script in your submission
