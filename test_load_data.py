# ECOR 1042 Lab 4 - team submission

#import check module here
from check import equal, summary, within
#import load_data module here
from load_data import load_data, student_school_list, student_health_list, student_age_list, student_failures_list, add_average

# Update "" with your the name of the active members of the team
__author__ = "William Chicquen, Neel Leuva, Ali El Shennawy, Sanil Srivastava"

# Update "" with your student number (e.g., 100100100)
"101275149, 101257773,  101274917, 101268578"
# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-003"

#==========================================#

# Place test_return_list function here 
def test_return_list():
    #Complete the function with your test cases
    
    #test that student_school_list returns a list (3 different test cases required)
    
    equal(True,(isinstance(student_school_list("student-test.csv","GP"),list)))
    equal(True,(isinstance(student_school_list("student-test.csv","BD"),list)))
    equal(True,(isinstance(student_school_list("student-test.csv","CF"),list)))
    
    #test that student_age_list returns a list (3 different test cases required)
    
    equal(True,(isinstance(student_age_list("student-test.csv",15),list)))
    equal(True,(isinstance(student_age_list("student-test.csv",16),list)))
    equal(True,(isinstance(student_age_list("student-test.csv",17),list)))
    
    #test that student_health_list returns a list (3 different test cases required)
    
    equal(True,(isinstance(student_health_list("student-test.csv",4),list)))
    equal(True,(isinstance(student_health_list("student-test.csv",1),list)))
    equal(True,(isinstance(student_health_list("student-test.csv",3),list)))
    
    #test that student_failures_list returns a list (3 different test cases required)
    
    equal(True,(isinstance(student_failures_list("student-test.csv", 0),list)))
    equal(True,(isinstance(student_failures_list("student-test.csv", 2),list)))
    equal(True,(isinstance(student_failures_list("student-test.csv", 3),list)))
    
    #test that load_data returns a list (6 different test cases required)
    
    equal(True,(isinstance(load_data("student-test.csv", ("Failures", 0)),list)))
    equal(True,(isinstance(load_data("student-test.csv", ("Age", 15)),list)))
    equal(True,(isinstance(load_data("student-test.csv", ("School", "GP")),list)))
    equal(True,(isinstance(load_data("student-test.csv", ("Health", 1)),list)))
    equal(True,(isinstance(load_data("student-test.csv", ("All", 0)),list)))
    equal(True,(isinstance(load_data("student-test.csv", ("School", "CF")),list)))
 
    
     #test that add_average returns a list (3 different test cases required)
     
    equal(True,(isinstance(add_average([{'School': 'GP', 'Age': 18, 'Studytime': 6.7 , 'Failures': 1 , 'Health' : 3, 'Absences': 7, 'G1' : 5, 'G2' : 6, 'G3' : 6}]) ,list)))
    
    
    equal(True,(isinstance(add_average([{'School': 'GP', 'Age': 18, 'Studytime': 6.7 , 'Failures': 1 , 'Health' : 3, 'Absences': 7, 'G1' : 5, 'G2' : 6, 'G3' : 6}, {'School': 'MP', 'Age': 17, 'Studytime': 5.7 , 'Failures': 0 , 'Health' : 3, 'Absences': 3, 'G1' : 1, 'G2' : 3, 'G3' : 6}, {'School': 'GP', 'Age': 19, 'Studytime': 6.0 , 'Failures': 2 , 'Health' : 2, 'Absences': 8, 'G1' : 8, 'G2' : 7, 'G3' : 1}]) ,list)))
    
    equal(True,(isinstance(add_average([{'School': 'CF', 'Age': 17, 'Studytime': 6.7 , 'Failures': 3 , 'Health' : 3, 'Absences': 7, 'G1' : 5, 'G2' : 6, 'G3' : 6}, {'School': 'GP', 'Age': 19, 'Studytime': 5.7 , 'Failures': 0 , 'Health' : 3, 'Absences': 3, 'G1' : 2, 'G2' : 5, 'G3' : 6}, {'School': 'CF', 'Age': 17, 'Studytime': 6.0 , 'Failures': 2 , 'Health' : 2, 'Absences': 8, 'G1' : 9, 'G2' : 7, 'G3' : 1}]) ,list)))
  
     
    summary()

# Place test_return_list_correct_lenght function here
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


#Place test_return_correct_dict_inside_list function here

def test_return_correct_dict_inside_list():

    #Complete the function with your test cases
    
    #test that student_school_list returns a correct dictionary inside the list (3 different test cases required)


  list_all = student_school_list('student-test.csv', 'GP') #creates a list of dictionaries using student_school_list 
  equal((list_all[0], list_all[-1]), ({'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {'Age': 15, 'StudyTime': 2.0, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10})) #checks to see if list created is equal to list provided
    
  list_all = student_school_list('student-test.csv',  'MB') #creates a list of dictionaries using student_school_list 
  equal((list_all[0], list_all[-1]),({'Age': 16, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}, {'Age': 15, 'StudyTime': 1.0, 'Failures': 0, 'Health': 3, 'Absences': 2, 'G1': 10, 'G2': 12, 'G3': 12}))#checks to see if list created is equal to list provided    
  
  list_all = student_school_list('student-test.csv', 'MS')#creates a list of dictionaries using student_school_list 
  equal((list_all[0], list_all[-1]), ({'Age': 17, 'StudyTime': 1.0, 'Failures': 0, 'Health': 4, 'Absences': 8, 'G1': 11, 'G2': 10, 'G3': 10}, {'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Health': 5, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8}))#checks to see if list created is equal to list provided    
    
     
    #test that student_age_list returns a correct dictionary inside the list  (3 different test cases required)
  
  list_all = student_age_list('student-test.csv', 15)#creates a list of dictionaries using student_age_list 
  equal((list_all[0], list_all[-1]), ({'School': 'GP', 'StudyTime': 2.0, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}, {'School': 'CF', 'StudyTime': 5.0, 'Failures': 2, 'Health': 3,'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7}))#checks to see if list created is equal to list provided

  list_all = student_age_list('student-test.csv', 16)#creates a list of dictionaries using student_age_list 
  equal((list_all[0], list_all[-1]), ({'School': 'MB', 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}, {'School': 'CF', 'StudyTime': 2.0, 'Failures': 1, 'Health': 5, 'Absences': 4, 'G1': 10, 'G2': 12, 'G3': 12}))#checks to see if list created is equal to list provided

  list_all = student_age_list('student-test.csv', 17)#creates a list of dictionaries using student_age_list 
  equal((list_all[0], list_all[-1]), ({'School': 'GP', 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6}, {'School': 'MS', 'StudyTime': 3.0, 'Failures': 0, 'Health': 4, 'Absences': 4, 'G1': 14, 'G2': 14, 'G3': 14}))#checks to see if list created is equal to list provided

  
    #test that student_health_list returns a correct dictionary inside the list  (3 different test cases required)
  list_all = student_health_list('student-test.csv', 4)#creates a list of dictionaries using student_health_list 
  equal((list_all[0], list_all[-1]), ({'School': 'BD', 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 4, 'G1': 10, 'G2': 9, 'G3': 9}, {'School': 'MS','Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 4, 'G1': 14, 'G2': 14, 'G3': 14}))#checks to see if list created is equal to list provided

  list_all = student_health_list('student-test.csv', 1)#creates a list of dictionaries using student_health_list 
  equal((list_all[0]), ({'School': 'MS', 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 7, 'G1': 10, 'G2': 9, 'G3': 9}))#checks to see if list created is equal to list provided
      
  list_all = student_health_list('student-test.csv', 3)#creates a list of dictionaries using student_health_list 
  equal((list_all[0], list_all[-1]), ({'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'BD', 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 1, 'G1': 13, 'G2': 12, 'G3': 12}))#checks to see if list created is equal to list provided
 
    
    #test that student_failures_list returns a correct dictionary inside the list (3 different test cases required)
  list_all = student_failures_list('student-test.csv', 0)#creates a list of dictionaries using student_failures_list 
  equal((list_all[0], list_all[-1]), ({'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'MS', 'Age': 18, 'StudyTime': 3.0, 'Health': 5, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8}))#checks to see if list created is equal to list provided
    
  list_all = student_failures_list('student-test.csv', 2)#creates a list of dictionaries using student_failures_list 
  equal((list_all[0], list_all[-1]), ({'School': 'CF', 'Age': 15, 'StudyTime': 5.0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7}, {'School': 'CF', 'Age': 17, 'StudyTime': 1.0, 'Health': 5, 'Absences': 0, 'G1': 7, 'G2': 6, 'G3': 0}))#checks to see if list created is equal to list provided
      
  list_all = student_failures_list('student-test.csv', 3)#creates a list of dictionaries using student_failures_list 
  equal((list_all[0]), ({'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}))#checks to see if list created is equal to list provided
  

    
    #test that load_data returns a correct dictionary inside the list (6 different test cases required)
  list_all = load_data('student-test.csv', ('Failures', 3))#creates a list of dictionaries using load_data 
  equal((list_all[0]), ({'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}))#checks to see if list created is equal to list provided

  list_all = load_data('student-test.csv', ('Health', 4))#creates a list of dictionaries using load_data 
  equal((list_all[0], list_all[-1]), ({'School': 'BD', 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 4, 'G1': 10, 'G2': 9, 'G3': 9}, {'School': 'MS','Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 4, 'G1': 14, 'G2': 14, 'G3': 14}))#checks to see if list created is equal to list provided

  list_all = load_data('student-test.csv', ('School', 'MB'))#creates a list of dictionaries using load_data 
  equal((list_all[0], list_all[-1]),({'Age': 16, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}, {'Age': 15, 'StudyTime': 1.0, 'Failures': 0, 'Health': 3, 'Absences': 2, 'G1': 10, 'G2': 12, 'G3': 12}))#checks to see if list created is equal to list provided

  list_all = load_data('student-test.csv', ('Age', 17))#creates a list of dictionaries using load_data 
  equal((list_all[0], list_all[-1]), ({'School': 'GP', 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6}, {'School': 'MS', 'StudyTime': 3.0, 'Failures': 0, 'Health': 4, 'Absences': 4, 'G1': 14, 'G2': 14, 'G3': 14}))#checks to see if list created is equal to list provided

  list_all = load_data('student-test.csv',('All', 47))#creates a list of dictionaries using load_data 
  equal((list_all[0], list_all[-1]), ({'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0,  'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'MS', 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Health': 5, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8}))#checks to see if list created is equal to list provided

  list_all = load_data('student-test.csv', ('Failures', 0))#creates a list of dictionaries using load_data 
  equal((list_all[0], list_all[-1]), ({'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'MS', 'Age': 18, 'StudyTime': 3.0, 'Health': 5, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8}))#checks to see if list created is equal to list provided

  
     #test that add_average returns a correct dictionary inside the list  (3 different test cases required)
  
  list_add_average = add_average([{'School': 'GP', 'Age': 18, 'Studytime': 6.7 , 'Failures': 1 , 'Health' : 3, 'Absences': 7, 'G1' : 5, 'G2' : 6, 'G3' : 6}]) #creates a list of dictionaries using add_average and load_data
  equal(list_add_average[0], {'School': 'GP', 'Age': 18, 'Studytime': 6.7, 'Failures': 1, 'Health': 3, 'Absences': 7, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.67})

  list_add_average = add_average([{'School': 'GP', 'Age': 18 , 'Studytime': 6.7 , 'Failures': 1 , 'Health' : 3, 'Absences': 7, 'G1' : 5, 'G2' : 6, 'G3' : 6}, {'School': 'MP', 'Age': 17, 'Studytime': 5.7 , 'Failures': 0 , 'Health' : 3, 'Absences': 3, 'G1' : 1, 'G2' : 3, 'G3' : 6}, {'School': 'GP', 'Age': 19, 'Studytime': 6.0 , 'Failures': 2 , 'Health' : 2, 'Absences': 8, 'G1' : 8, 'G2' : 7, 'G3' : 1}]) #creates a list of dictionaries using add_average and load_data
  equal(list_add_average[0], {'School': 'GP', 'Age': 18, 'Studytime': 6.7, 'Failures': 1, 'Health': 3, 'Absences': 7, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.67})
  
  list_add_average = add_average([{'School': 'MS', 'Age': 21, 'Studytime': 1.0 , 'Failures': 3 , 'Health' : 3, 'Absences': 3, 'G1' : 10, 'G2' : 8, 'G3' : 7}]) #creates a list of dictionaries using add_average and load_data
  equal(list_add_average[0], {'School': 'MS', 'Age': 21, 'StudyTime': 1.0, 'Failures': 3, 'Health': 3, 'Absences': 3, 'G1': 10, 'G2': 8, 'G3': 7, 'G_Avg': 8.33})
    
    

summary()



#Place test_add_average function here

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
