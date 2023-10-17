# ECOR 1042 Lab 4 - Individual submission for test1 function

#import check module here

import check 
import load_data
from load_data import student_school_list
from load_data import student_age_list
from load_data import student_health_list
from load_data import student_failures_list
from load_data import load_data
from load_data import add_average

#import load_data module here

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Sanil Srivastava"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101268578"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-003"

#==========================================#
#Do not modify the code alreayd provided.

def test_return_list():
    #Complete the function with your test cases
    
    #test that student_school_list returns a list (3 different test cases required)
    
    check.equal(True,(isinstance(student_school_list("student-mat.csv","GP"),list)))
    check.equal(True,(isinstance(student_school_list("student-mat.csv","BD"),list)))
    check.equal(True,(isinstance(student_school_list("student-mat.csv","CF"),list)))
    
    #test that student_age_list returns a list (3 different test cases required)
    
    check.equal(True,(isinstance(student_age_list("student-mat.csv",15),list)))
    check.equal(True,(isinstance(student_age_list("student-mat.csv",16),list)))
    check.equal(True,(isinstance(student_age_list("student-mat.csv",17),list)))
    
    #test that student_health_list returns a list (3 different test cases required)
    
    check.equal(True,(isinstance(student_health_list("student-mat.csv",4),list)))
    check.equal(True,(isinstance(student_health_list("student-mat.csv",1),list)))
    check.equal(True,(isinstance(student_health_list("student-mat.csv",3),list)))
    
    #test that student_failures_list returns a list (3 different test cases required)
    
    check.equal(True,(isinstance(student_failures_list("student-mat.csv", 0),list)))
    check.equal(True,(isinstance(student_failures_list("student-mat.csv", 2),list)))
    check.equal(True,(isinstance(student_failures_list("student-mat.csv", 3),list)))
    
    #test that load_data returns a list (6 different test cases required)
    
    check.equal(True,(isinstance(load_data("student-mat.csv", ("Failures", 0)),list)))
    check.equal(True,(isinstance(load_data("student-mat.csv", ("Age", 15)),list)))
    check.equal(True,(isinstance(load_data("student-mat.csv", ("School", "GP")),list)))
    check.equal(True,(isinstance(load_data("student-mat.csv", ("Health", 1)),list)))
    check.equal(True,(isinstance(load_data("student-mat.csv", ("All", 0)),list)))
    check.equal(True,(isinstance(load_data("student-mat.csv", ("School", "CF")),list)))
 
    
     #test that add_average returns a list (3 different test cases required)
     
    check.equal(True,(isinstance(add_average([{'School': 'GP', 'Age': 18, 'Studytime': 6.7 , 'Failures': 1 , 'Health' : 3, 'Absences': 7, 'G1' : 5, 'G2' : 6, 'G3' : 6}]) ,list)))
    
    
    check.equal(True,(isinstance(add_average([{'School': 'GP', 'Age': 18, 'Studytime': 6.7 , 'Failures': 1 , 'Health' : 3, 'Absences': 7, 'G1' : 5, 'G2' : 6, 'G3' : 6}, {'School': 'MP', 'Age': 17, 'Studytime': 5.7 , 'Failures': 0 , 'Health' : 3, 'Absences': 3, 'G1' : 1, 'G2' : 3, 'G3' : 6}, {'School': 'GP', 'Age': 19, 'Studytime': 6.0 , 'Failures': 2 , 'Health' : 2, 'Absences': 8, 'G1' : 8, 'G2' : 7, 'G3' : 1}]) ,list)))
    
    check.equal(True,(isinstance(add_average([{'School': 'CF', 'Age': 17, 'Studytime': 6.7 , 'Failures': 3 , 'Health' : 3, 'Absences': 7, 'G1' : 5, 'G2' : 6, 'G3' : 6}, {'School': 'GP', 'Age': 19, 'Studytime': 5.7 , 'Failures': 0 , 'Health' : 3, 'Absences': 3, 'G1' : 2, 'G2' : 5, 'G3' : 6}, {'School': 'CF', 'Age': 17, 'Studytime': 6.0 , 'Failures': 2 , 'Health' : 2, 'Absences': 8, 'G1' : 9, 'G2' : 7, 'G3' : 1}]) ,list)))
  
     
    check.summary()


# Do NOT include a main script in your submission
