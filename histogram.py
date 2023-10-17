# ECOR 1042 Lab 6 - Individual submission for histogram

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Ali El Shennawy"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101274917"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-003"

#==========================================#
# Place your histogram function after this line

import matplotlib.pyplot as plot

def histogram(students: list[dict], attribute: str) -> None:
    """Shows a histogram depicting frequencies of a given attribute
    Precondition(s): None
    >>> histogram(load_data("student-mat.csv", ("All", 0)), "Age")
    """
  
    elements = {}
    
    for student in students:
        if student[attribute] not in elements.keys():
            elements[student[attribute]] = 1
        else:
            elements[student[attribute]] += 1
    
    x_coordinates = []
    y_coordinates = []
    
    for key in elements:
        x_coordinates.append(key)
        y_coordinates.append(elements[key])
    
    plot.bar(x_coordinates, y_coordinates)
    plot.xlabel(attribute)
    plot.ylabel("Frequency")
    plot.title("Frequency of Each Occurence of Element")
    plot.show()    
  
  

# Do NOT include a main script in your submission
