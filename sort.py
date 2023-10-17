# ECOR 1042 Lab 5 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "William Chicquen, Sanil Srivastava, Ali El Shennawy, Neel Leuva"

# Update "" with your team (e.g. T102)
__team__ = "T-003"

#==========================================#
# Place your sort_students_age_bubble function after this line
def sort_students_age_bubble(list_dictionary: list[dict], asc_descending: str) -> None:
  """Changes list_dictionary to be sorted in either ascending or decending order depending on asc_descending string provided

  Preconditions: asc_descending must be string, "A" or "D", list_dictionary must be atleast 2 dictionaries long

  >>>sort_students_age_bubble([{"Age":10,"School":"GP"},{"Age":19,"School":"MS"}], "D")
  [{"Age": 19, "School":"MS"}, {"Age":10, "School":"GP"}]
  >>>sort_students_age_bubble([{"Age":19,"School":"GP"},{"Age":18,"School":"MS"}], "A")
   [{"Age": 18, "School":"MS"}, {"Age":19, "School":"GP"}]
  >>>sort_students_age_bubble([{"School":"GP"}, {"School":"MS"}], "D")
  'Age' key is not present
  """

  
  for dictionary in list_dictionary:
    if "Age" not in dictionary:
      print("'Age' key is not present")
      return list_dictionary
    else:
      swap = True
      while swap:
        swap = False
        for i in range(len(list_dictionary) - 1):
          dictionary1 = list_dictionary[i]
          dictionary2 = list_dictionary[i + 1]
          age_key1 = dictionary1["Age"]
          age_key2 = dictionary2["Age"]
          if age_key1 > age_key2:
            list_dictionary_lock = list_dictionary[i]
            list_dictionary[i] = list_dictionary[i + 1]
            list_dictionary[i + 1] = list_dictionary_lock
            swap = True
          if asc_descending == "D":
            list_dictionary.reverse()
            swap = False
    
    return list_dictionary



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


#==========================================#
# Place your sort_students_failures_bubble function after this line

def sort_students_failures_bubble(data:list[dict], order: chr):

  
    """
    
    This function takes in a list of dictonaries and sorts the failure keys of dictionaries in the list.
    
    >>>sort_students_failures_bubble([{"Failures":10,"School":"GP"},{"Failures":19,"School":"MS"}], "D")
    [{'Failures': 19, 'School': 'MS'}, {'Failures': 10, 'School': 'GP'}]
    
    
    >>>sort_students_failures_bubble([{"Failures":10,"School":"GP"},{"Failures":19,"School":"MS"}], "A")
    [{'Failures': 10, 'School': 'GP'}, {'Failures': 19, 'School': 'MS'}]
    
    >>>sort_students_failures_bubble([{"Failures":10,"School":"GP"},{"Failu":19,"School":"MS"}], "D")
    'Failures' key is not present 
    [{'Failures': 10, 'School': 'GP'}, {'Failu': 19, 'School': 'MS'}]
    
    
    """
    
    
    isin = False
    
    for i in range(len(data)) :
        
        isin = ('Failures' in data[i])
            
        if isin == False :
            print( "'Failures' key is not present ")
            return data
            
    
    if order == "A" :
        
        for z in range(len(data)):
            
            for i in range (len(data)-1):
                
                if data[i]['Failures'] > data[i+1]['Failures']:
                    
                    temp = data[i]
                    data[i] = data[i+1]
                    data[i+1] = temp          
    
    
    
    if order == "D" :
        
        for z in range(len(data)):
            
            for i in range (len(data)-1):
                
                if data[i]['Failures'] < data[i+1]['Failures']:
                    
                    temp = data[i]
                    data[i] = data[i+1]
                    data[i+1] = temp        
                    
    return data

#==========================================#
# Place your sort function after this line


def sort(data:list[dict], order:str, method:str) -> list[dict]:
  
  """
  This function calls other sorting functions to sort different items in a list using different ways.
  
  >>>sort([{"Age":10,"School":"GP"},{"Age":19.1,"School":"MS"}],"D","Age")
  [{'Age': 19.1, 'School': 'MS'}, {'Age': 10, 'School': 'GP'}]
  
  >>>sort([{"School":"GP"},{"School":"MS"}], "D", "School")
  Cannot be sorted by ' School '
  [{'School': 'GP'}, {'School': 'MS'}]
  
  >>>sort([{"Failures":10,"School":"GP"},{"Failures":19,"School":"MS"}], "D","Failures")
  [{'Failures': 19, 'School': 'MS'}, {'Failures': 10, 'School': 'GP'}]
  
  >>>sort([{'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.67}, {'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6, 'G_Avg': 5.33}, {'Age': 15, 'StudyTime': 2.0, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10, 'G_Avg': 8.33}], "D","G_Avg")
  [{'Age': 15, 'StudyTime': 2.0, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10, 'G_Avg': 8.33}, {'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.67}, {'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6, 'G_Avg': 5.33}]

  >>>sort([{'Age': 17, 'StudyTime': 1.0, 'Failures': 3, 'Health': 3, 'Absences': 2, 'G1': 8, 'G2': 8, 'G3': 10}, {'Age': 16, 'StudyTime': 4.0, 'Failures': 0, 'Health': 3, 'Absences': 0, 'G1': 11, 'G2': 11, 'G3': 11}], "A","Studytime")
  [{'Age': 17, 'StudyTime': 1.0, 'Failures': 3, 'Health': 3, 'Absences': 2, 'G1': 8, 'G2': 8, 'G3': 10}, {'Age': 16, 'StudyTime': 4.0, 'Failures': 0, 'Health': 3, 'Absences': 0, 'G1': 11, 'G2': 11, 'G3': 11}]

  >>>sort([{"Age":10,"School":"GP"},{"Age":19,"School":"MS"}], "D","Age")
  [{'Age': 19, 'School': 'MS'}, {'Age': 10, 'School': 'GP'}]


  
  """
  
  if method == "Age" :
    final_data = sort_students_age_bubble(data,order)
    
  elif method == "Studytime" :
    final_data = sort_students_time_selection(data,order)
    
  elif method == "G_Avg" :
    final_data = sort_students_g_avg_insertion(data,order)
    
  elif method == "Failures" :
    final_data = sort_students_failures_bubble(data,order)
    
  else :
    print(" Cannot be sorted by '" , method,"'")
    final_data = data
    
  return final_data
    

# Do NOT include a main script in your submission