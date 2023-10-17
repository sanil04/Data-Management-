# ECOR 1042 Lab 3 - Individual submission for student_health_list function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "William Chicquen"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101275149"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-003"

#==========================================#
# Place your student_health_list function after this line
def student_health_list(file: str, current_health: int) -> list[dict]:
  """Returns students from a file named student-mat.csv that have the current_health provided when calling the function

  Preconditons: 0 < current_health <= 5, current_health must be interger value. file must be student-mat.cvs
  
  >>>student_health_list(student-mat.csv, 4) 
  [{'School': 'GP', 'Age': 15, 'Studytime': 3.0, 'Failures': 0, 'Absences': 4, 'G1': 10, 'G2': 12, 'G3': 12}, {'School': 'GP', 'Age': 16, 'Studytime': 2.0, 'Failures': 0, 'Absences': 4, 'G1': 8, 'G2': 10, 'G3': 10},...{'School': 'MS','Age': 20, 'Studytime': 2.0, 'Failures': 2, 'Absences': 11, 'G1': 9, 'G2': 9, 'G3': 9}]
  >>>student_health_list(student-mat.csv, 1)
  [{'School': 'GP', 'Age': 17, 'Studytime': 2.0, 'Failures': 0, 'Absences': 6, 'G1': 6, 'G2': 5, 'G3': 6}, {'School': 'GP', 'Age:': 15, 'Studytime': 2.0, 'Failures': 0, 'Absences': 0, 'G1': 16, 'G2': 18, 'G3': 19}, ...{'School': 'MS', 'Age': 18, 'Studytime': 2.0, 'Failures': 0, 'Absences': 0, 'G1': 7, 'G2': 9, 'G3': 8}]
  >>>student_health_list(student-mat.csv, 3)
  [{'School': 'GP', 'Age': 18, 'Studytime': 2.0, 'Failures': 0, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'GP','Age': 17, 'Studytime': 2.0, 'Failures': 0, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6},...{'School': 'MS', 'Age': 21, 'Studytime': 1.0, 'Failures': 3, 'Absences': 3, 'G1': 10, 'G2': 8, 'G3': 7}]
  """
  information = open(file, "r") #opens file provided
  list_of_lists = []    
  for line in information: #goes through each line of file provided
      splitted_line = line.split(",") #splits code into individual string values
      list_of_lists.append(splitted_line) #adds splited_line to empty list
  list_of_lists.pop(0) 

  for entry in list_of_lists: #goes through each entry in list_of_lists
      for i in range(1, 9): # for loop is going over each column and assigning it the proper type
          if i == 2:
              entry[i] = float(entry[i])
          else:
              entry[i] = int(entry[i])

  list_of_students = []
  student = {}
  keys = [("School", 0), ("Age", 1), ("Studytime", 2), ("Failures", 3),
            ("Health", 4), ("Absences", 5), ("G1", 6), ("G2", 7), ("G3", 8)] #showing each columns and its proper indices
  for entry in list_of_lists: 
          for key in keys: #looks through columns defined in keys
              student[key[0]] = entry[key[1]]

          list_of_students.append(student.copy()) #adds a copy of student to list_of_students
  list_of_health = []

  for student in list_of_students: #goes over list_of_students for each student
      if student["Health"] == current_health: #looks for Health in student to see if equavilant to list_of_heath
            
        list_of_health.append(student)
        for items in list_of_health: # creats loop that will search for "Health:" and pop it out of list_of_health
          items.pop("Health", None)
  return list_of_health

# Do NOT include a main script in your submission