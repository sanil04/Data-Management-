# ECOR 1042 Lab 4 - Individual submission for test3 function

#import check module here
import check
#import load_data module here
import load_data 
# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "William Chicquen"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101275149"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-003"

#==========================================#
#Do not modify the code already provided.

def test_return_correct_dict_inside_list():

    #Complete the function with your test cases
    
    #test that student_school_list returns a correct dictionary inside the list (3 different test cases required)


  list_all = load_data.student_school_list('student-test.csv', ('School', 'GP')) #creates a list of dictionaries using student_school_list 
  check.equal((list_all[0], list_all[-1]), ({'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {'Age': 15, 'StudyTime': 2.0, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10})) #checks to see if list created is equal to list provided
    
  list_all = load_data.student_school_list('student-test.csv', ('School', 'MB'))#creates a list of dictionaries using student_school_list 
  check.equal((list_all[0], list_all[-1]),({'Age': 16, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}, {'Age': 15, 'StudyTime': 1.0, 'Failures': 0, 'Health': 3, 'Absences': 2, 'G1': 10, 'G2': 12, 'G3': 12}))#checks to see if list created is equal to list provided    
  
  list_all = load_data.student_school_list('student-test.csv', ('School', 'MS'))#creates a list of dictionaries using student_school_list 
  check.equal((list_all[0], list_all[-1]), ({'Age': 17, 'StudyTime': 1.0, 'Failures': 0, 'Health': 4, 'Absences': 8, 'G1': 11, 'G2': 10, 'G3': 10}, {'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Health': 5, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8}))#checks to see if list created is equal to list provided    
    
     
    #test that student_age_list returns a correct dictionary inside the list  (3 different test cases required)
  
  list_all = load_data.student_age_list('student-test.csv', ('Age', 15))#creates a list of dictionaries using student_age_list 
  check.equal((list_all[0], list_all[-1]), ({'School': 'GP', 'StudyTime': 2.0, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}, {'School': 'CF', 'StudyTime': 5.0, 'Failures': 2, 'Health': 3,'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7}))#checks to see if list created is equal to list provided

  list_all = load_data.student_age_list('student-test.csv', ('Age', 16))#creates a list of dictionaries using student_age_list 
  check.equal((list_all[0], list_all[-1]), ({'School': 'MB', 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}, {'School': 'CF', 'StudyTime': 2.0, 'Failures': 1, 'Health': 5, 'Absences': 4, 'G1': 10, 'G2': 12, 'G3': 12}))#checks to see if list created is equal to list provided

  list_all = load_data.student_age_list('student-test.csv', ('Age', 17))#creates a list of dictionaries using student_age_list 
  check.equal((list_all[0], list_all[-1]), ({'School': 'GP', 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6}, {'School': 'MS', 'StudyTime': 3.0, 'Failures': 0, 'Health': 4, 'Absences': 4, 'G1': 14, 'G2': 14, 'G3': 14}))#checks to see if list created is equal to list provided

  
    #test that student_health_list returns a correct dictionary inside the list  (3 different test cases required)
  list_all = load_data.student_health_list('student-test.csv', ('Health', 4))#creates a list of dictionaries using student_health_list 
  check.equal((list_all[0], list_all[-1]), ({'School': 'BD', 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 4, 'G1': 10, 'G2': 9, 'G3': 9}, {'School': 'MS','Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 4, 'G1': 14, 'G2': 14, 'G3': 14}))#checks to see if list created is equal to list provided

  list_all = load_data.student_health_list('student-test.csv', ('Health', 1))#creates a list of dictionaries using student_health_list 
  check.equal((list_all[0]), ({'School': 'MS', 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 7, 'G1': 10, 'G2': 9, 'G3': 9}))#checks to see if list created is equal to list provided
      
  list_all = load_data.student_health_list('student-test.csv', ('Health', 3))#creates a list of dictionaries using student_health_list 
  check.equal((list_all[0], list_all[-1]), ({'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'BD', 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 1, 'G1': 13, 'G2': 12, 'G3': 12}))#checks to see if list created is equal to list provided
 
    
    #test that student_failures_list returns a correct dictionary inside the list (3 different test cases required)
  list_all = load_data.student_failures_list('student-test.csv', ('Failures', 0))#creates a list of dictionaries using student_failures_list 
  check.equal((list_all[0], list_all[-1]), ({'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'MS', 'Age': 18, 'StudyTime': 3.0, 'Health': 5, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8}))#checks to see if list created is equal to list provided
    
  list_all = load_data.student_failures_list('student-test.csv', ('Failures', 2))#creates a list of dictionaries using student_failures_list 
  check.equal((list_all[0], list_all[-1]), ({'School': 'CF', 'Age': 15, 'StudyTime': 5.0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7}, {'School': 'CF', 'Age': 17, 'StudyTime': 1.0, 'Health': 5, 'Absences': 0, 'G1': 7, 'G2': 6, 'G3': 0}))#checks to see if list created is equal to list provided
      
  list_all = load_data.student_failures_list('student-test.csv', ('Failures', 3))#creates a list of dictionaries using student_failures_list 
  check.equal((list_all[0]), ({'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}))#checks to see if list created is equal to list provided
  

    
    #test that load_data returns a correct dictionary inside the list (6 different test cases required)
  list_all = load_data.load_data('student-test.csv', ('Failures', 3))#creates a list of dictionaries using load_data 
  check.equal((list_all[0]), ({'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}))#checks to see if list created is equal to list provided

  list_all = load_data.load_data('student-test.csv', ('Health', 4))#creates a list of dictionaries using load_data 
  check.equal((list_all[0], list_all[-1]), ({'School': 'BD', 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 4, 'G1': 10, 'G2': 9, 'G3': 9}, {'School': 'MS','Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 4, 'G1': 14, 'G2': 14, 'G3': 14}))#checks to see if list created is equal to list provided

  list_all = load_data.load_data('student-test.csv', ('School', 'MB'))#creates a list of dictionaries using load_data 
  check.equal((list_all[0], list_all[-1]),({'Age': 16, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}, {'Age': 15, 'StudyTime': 1.0, 'Failures': 0, 'Health': 3, 'Absences': 2, 'G1': 10, 'G2': 12, 'G3': 12}))#checks to see if list created is equal to list provided

  list_all = load_data.load_data('student-test.csv', ('Age', 17))#creates a list of dictionaries using load_data 
  check.equal((list_all[0], list_all[-1]), ({'School': 'GP', 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6}, {'School': 'MS', 'StudyTime': 3.0, 'Failures': 0, 'Health': 4, 'Absences': 4, 'G1': 14, 'G2': 14, 'G3': 14}))#checks to see if list created is equal to list provided

  list_all = load_data.load_data('student-test.csv',('All', 47))#creates a list of dictionaries using load_data 
  check.equal((list_all[0], list_all[-1]), ({'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0,  'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'MS', 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Health': 5, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8}))#checks to see if list created is equal to list provided

  list_all = load_data.load_data('student-test.csv', ('Failures', 0))#creates a list of dictionaries using load_data 
  check.equal((list_all[0], list_all[-1]), ({'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'MS', 'Age': 18, 'StudyTime': 3.0, 'Health': 5, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8}))#checks to see if list created is equal to list provided

  
     #test that add_average returns a correct dictionary inside the list  (3 different test cases required)
  
  list_add_average = load_data.add_average([{'School': 'GP', 'Age': 18, 'Studytime': 6.7 , 'Failures': 1 , 'Health' : 3, 'Absences': 7, 'G1' : 5, 'G2' : 6, 'G3' : 6}]) #creates a list of dictionaries using add_average and load_data
  check.equal(list_add_average[0], {'School': 'GP', 'Age': 18, 'Studytime': 6.7, 'Failures': 1, 'Health': 3, 'Absences': 7, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.67})

  list_add_average = load_data.add_average([{'School': 'GP', 'Age': 18 , 'Studytime': 6.7 , 'Failures': 1 , 'Health' : 3, 'Absences': 7, 'G1' : 5, 'G2' : 6, 'G3' : 6}, {'School': 'MP', 'Age': 17, 'Studytime': 5.7 , 'Failures': 0 , 'Health' : 3, 'Absences': 3, 'G1' : 1, 'G2' : 3, 'G3' : 6}, {'School': 'GP', 'Age': 19, 'Studytime': 6.0 , 'Failures': 2 , 'Health' : 2, 'Absences': 8, 'G1' : 8, 'G2' : 7, 'G3' : 1}]) #creates a list of dictionaries using add_average and load_data
  check.equal(list_add_average[0], {'School': 'GP', 'Age': 18, 'Studytime': 6.7, 'Failures': 1, 'Health': 3, 'Absences': 7, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.67})
  
  list_add_average = load_data.add_average([{'School': 'MS', 'Age': 21, 'Studytime': 1.0 , 'Failures': 3 , 'Health' : 3, 'Absences': 3, 'G1' : 10, 'G2' : 8, 'G3' : 7}]) #creates a list of dictionaries using add_average and load_data
  check.equal(list_add_average[0], {'School': 'MS', 'Age': 21, 'StudyTime': 1.0, 'Failures': 3, 'Health': 3, 'Absences': 3, 'G1': 10, 'G2': 8, 'G3': 7, 'G_Avg': 8.33})
    

check.summary()
