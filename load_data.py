# ECOR 1042 Lab 3 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__authors__ = "Ali El Shennawy, Neel Leuva, Sanil Srivastava, William Chicquen"

# Update "" with your team (e.g. T102)
__team__ = "T-003"

#==========================================#
# Place your student_school_list function after this line

def student_school_list(file: str, school_name: str) -> list[dict]:
    """
    Takes in two inputs, the first being a file name and the second one being a name of a school. The function returns a list of dictionaries where each dictionary is the information of one student excluding the school name.

    Preconditions: File has to be student-mat.csv and school_name has to be GP, MB, CF, BD, or MS

    >>>student_school_list("student-mat.csv","GP")
    [{'Age:': 18, 'StudyTime:': 2.0, 'Failures:': 0, 'Health:': 3, 'Absences:': 6, 'G1:': 5, 'G2:': 6, 'G3:': 6}, {'Age:': 17, 'StudyTime:': 2.0, 'Failures:': 0, 'Health:': 3, ..., {'Age:': 17, 'StudyTime:': 1.0, 'Failures:': 3, 'Health:': 3, 'Absences:': 2, 'G1:': 8, 'G2:': 8, 'G3:': 10}]
    """
    # Takes the CSV file and converts it into a list of lists where each list is one student
    information = open(file, "r")
    list_of_lists = []
    for line in information:
        splitted_line = line.split(",")
        list_of_lists.append(splitted_line)
    list_of_lists.pop(0)

    # Convert each entry to the right data type
    for entry in list_of_lists:
        for i in range(1, 9):
            if i == 2:
                entry[i] = float(entry[i])
            else:
                entry[i] = int(entry[i])

    # Fiter through all the students and create a list of dictionaries with the
    list_of_students = []
    student = {}
    keys = [("Age", 1), ("StudyTime", 2), ("Failures", 3),
            ("Health", 4), ("Absences", 5), ("G1", 6), ("G2", 7), ("G3", 8)]
    for entry in list_of_lists:
        if entry[0] == school_name:
            for key in keys:
                student[key[0]] = entry[key[1]]

            list_of_students.append(student.copy())

    return list_of_students


#==========================================#
# Place your student_health_list function after this line
def student_health_list(file: str, current_health: int) -> list[dict]:
  """Returns students from a file named student-mat.cvs that have the current_health provided when calling the function

  Preconditions: 0 < current_health <= 5, current_health must be interger value. file must be student-mat.csv
  
  >>>student_health_list(student-mat.csv, 4) 
  [{'School': 'GP', 'Age': 15, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 4, 'G1': 10, 'G2': 12, 'G3': 12}, {'School': 'GP', 'Age': 16, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 4, 'G1': 8, 'G2': 10, 'G3': 10},...{'School': 'MS','Age': 20, 'StudyTime': 2.0, 'Failures': 2, 'Absences': 11, 'G1': 9, 'G2': 9, 'G3': 9}]
  >>>student_health_list(student-mat.csv, 1)
  [{'School': 'GP', 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 6, 'G1': 6, 'G2': 5, 'G3': 6}, {'School': 'GP', 'Age:': 15, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 0, 'G1': 16, 'G2': 18, 'G3': 19}, ...{'School': 'MS', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 0, 'G1': 7, 'G2': 9, 'G3': 8}]
  >>>student_health_list(student-mat.csv, 3)
  [{'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'GP','Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6},...{'School': 'MS', 'Age': 21, 'StudyTime': 1.0, 'Failures': 3, 'Absences': 3, 'G1': 10, 'G2': 8, 'G3': 7}]
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
  keys = [("School", 0), ("Age", 1), ("StudyTime", 2), ("Failures", 3),
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

#==========================================#
# Place your student_age_list function after this line
def student_age_list(file: str, age: int) -> list[dict]:
    
        """
    This funtion outputs the information of every student of a certain age when given "student-mat.csv" and an int age.
    
    Preconditions: The file entered must be "student-mat.csv", the age entered must be an int between 15 and 22 inclusive.
    
    >>>student_age_list("student-mat.csv",15)
    [{'School': 'GP', 'StudyTime': 2.0, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}, {'School': 'GP', 'StudyTime': 3.0,'Failures': 0, 'Health': 5, 'Absences': 2, 'G1': 15, 'G2': 14, 'G3': 15}, ........... {'School': 'CF', 'StudyTime': 2.0, 'Failures': 2, 'Health':       3,'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7}]


    >>>student_age_list("student-mat.csv",16)
    [{'School': 'GP', 'StudyTime': 2.0, 'Failures': 0, 'Health': 5, 'Absences': 4, 'G1': 6, 'G2': 10, 'G3': 10}, {'School': 'GP', 'StudyTime': 2.0,         'Failures': 0, 'Health': 5, 'Absences': 10, 'G1': 15, 'G2': 15, 'G3': 15}, ............ {'School': 'BD', 'StudyTime': 1.0, 'Failures': 0, 'Health':     3, 'Absences': 0, 'G1': 8, 'G2': 9, 'G3': 8}]

    >>>student_age_list("student-mat.csv",17)
    [{'School': 'GP', 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6}, {'School': 'GP', 'StudyTime': 2.0,           'Failures': 0, 'Health': 1, 'Absences': 6, 'G1': 6, 'G2': 5, 'G3': 6}, ............. {'School': 'MS', 'StudyTime': 1.0, 'Failures': 0, 'Health': 2,     'Absences': 3, 'G1': 14, 'G2': 16, 'G3': 16}]

    """
information = open(file, "r") # allows us to read file 
    list_of_lists = [] # list containing lists that hold data of every row 
    
    for line in information: # makes every row in the file a list
        splitted_line = line.split(",")
        list_of_lists.append(splitted_line)
    list_of_lists.pop(0)                        # removes first row

    for entry in list_of_lists:
        for i in range(1, 9):
            if i == 2:
                entry[i] = float(entry[i])      # convert each row's entries to appropriate data type
            else:
                entry[i] = int(entry[i])

    list_of_students = [] # list with students that are of specified age
    student = {} 
    keys = [("School", 0), ("StudyTime", 2), ("Failures", 3), ("Health", 4), ("Absences", 5), ("G1", 6), ("G2", 7), ("G3", 8)] # each row and its indices
    
    for stu in list_of_lists:
        if stu[1] == age:     # list students of a specific age
            for key in keys:
                student[key[0]] = stu[key[1]]

            list_of_students.append(student.copy())
    return list_of_students



#==========================================#
# Place your student_failures_list function after this line

def student_failures_list(file: str, number_of_failures: int) -> list[dict]:
    """Takes a list of students and returns a new list containing the students with a specific number of failures.
    Precondition(s): number_of_failures >= 0
    >>> student_failures_list("student-mat.csv", 0)
    [{'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'GP', 'Age': 17, 'StudyTime': 2.0, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6},...,{'School': 'MS', 'Age': 19, 'StudyTime': 1.0, 'Health': 5, 'Absences': 5, 'G1': 8, 'G2': 9, 'G3': 9}]
    >>> student_failures_list("student-mat.csv", 2)
    [{'School': 'GP', 'Age': 16, 'StudyTime': 1.0, 'Health': 5, 'Absences': 14, 'G1': 6, 'G2': 9, 'G3': 8}, {'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Health': 5, 'Absences': 2, 'G1': 8, 'G2': 6, 'G3': 5},...,{'School': 'MS', 'Age': 20, 'StudyTime': 2.0, 'Health': 4, 'Absences': 11, 'G1': 9, 'G2': 9, 'G3': 9}]
    >>> student_failures_list("student-mat.csv", 3)
    [{'School': 'GP', 'Age': 16, 'StudyTime': 1.0, 'Health': 5, 'Absences': 14, 'G1': 6, 'G2': 9, 'G3': 8}, {'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Health': 5, 'Absences': 2, 'G1': 8, 'G2': 6, 'G3': 5},...,{'School': 'MS', 'Age': 20, 'StudyTime': 2.0, 'Health': 4, 'Absences': 11, 'G1': 9, 'G2': 9, 'G3': 9}]
    """
    information = open(file, "r")
    list_of_lists = []
    for line in information:
        splitted_line = line.split(",")
        list_of_lists.append(splitted_line)
    list_of_lists.pop(0)  # list of columns

    for entry in list_of_lists:
        for i in range(1, 9):
            if i == 2:
                entry[i] = float(entry[i])  # convert each column's entries to appropriate data type
            else:
                entry[i] = int(entry[i])

    list_of_students = []
    student = {}
    keys = [("School", 0), ("Age", 1), ("StudyTime", 2), ("Failures", 3),  # each column and its indices
            ("Health", 4), ("Absences", 5), ("G1", 6), ("G2", 7),
            ("G3", 8)]
    for entry in list_of_lists:
        for key in keys:
            student[key[0]] = entry[key[1]]
        list_of_students.append(student.copy())
    list_of_failures = []

    for student in list_of_students:
        if student["Failures"] == number_of_failures:
            list_of_failures.append(student)

    for student in list_of_failures:
        del student["Failures"]

    return list_of_failures

#==========================================#
# Place your load_data function after this line

def load_data(file: str, student_feature: tuple) -> list[dict]:
  """Returns students from a file named student-mat.cvs that have the student_feature provided when calling the function

  Preconditions: student_feature must be a tuple and first value of tuple must be School, Age, Failures, Health or All, secound value must fit within these parameters; School has to be GP, MB, CF, BD, or MS, 15 <= Age <= 21, 0 <= Failures <= 3, 0 < Health <= 5 , All has no parameters.

  >>>load_data("student-mat.csv", ("Failures", 0))
  [{'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'GP', 'Age': 17, 'StudyTime': 2.0, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6},...,{'School': 'MS', 'Age': 19, 'StudyTime': 1.0, 'Health': 5, 'Absences': 5, 'G1': 8, 'G2': 9, 'G3': 9}]
  >>>load_data("student-mat.csv", ("All", -1))
  [{'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0,  'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'GP', 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6},...,{'School': 'MS', 'Age': 19, 'StudyTime': 1.0, 'Failures': 0, 'Health': 5, 'Absences': 5, 'G1': 8, 'G2': 9, 'G3': 9}]
  >>>load_data("student-mat.csv", ("G1", 10))
  Invalid Value // "G1" is not a valid input [] //Return value
  """

  if student_feature[0] == "School":
    return student_school_list(file, student_feature[1])
  
  elif student_feature[0] == "Age":
    return student_age_list(file, student_feature[1])
  
  elif student_feature[0] == "Failures":
    return student_failures_list(file, student_feature[1])
  
  elif student_feature[0] == "Health":
    return student_health_list(file, student_feature[1])
    
  elif student_feature[0] == "All":
    
    information = open(file, "r")
    list_of_lists = []
    for line in information:
        splitted_line = line.split(",")
        list_of_lists.append(splitted_line)
    list_of_lists.pop(0)

    for entry in list_of_lists:
        for i in range(9):
            if i == 0:
                entry[i] = str(entry[i])
            elif i == 2:
                entry[i] = float(entry[i])
            else:
                entry[i] = int(entry[i])

    student_information = ["School", "Age", "StudyTime", "Failures", "Health", "Absences", "G1", "G2", "G3"]

    student = {}
    list_of_students = []

    for student_list in list_of_lists:
        index = -1
        for data in student_list:
            index += 1
            student[student_information[index]] = data
        list_of_students.append(student)
        student = {}

    return list_of_students

    
#==========================================#
# Place your add_average function after this line

def add_average(students: list[dict]) -> list[dict]: 
    """
    Takes a list of students and returns an updated list with their grade averages added to it.
    Precondition(s): None
    """  
    student_with_avg_added = []
    for student in students:
        G_Avg = (student.get(
            "G1") + student.get("G2") + student.get("G3")) / 3
        student["G_Avg"] = round(G_Avg, 2)
        student_with_avg_added.append(student)
    return student_with_avg_added

  
  
# Do NOT include a main script in your submission
