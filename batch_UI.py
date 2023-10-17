# ECOR 1042 Lab 6 - Individual submission for batch_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "William Chicquen"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101275149"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-003"

#==========================================#
# Place your script for your batch_UI after this line
from curve_fit import curve_fit
from histogram import histogram
from load_data import *
from sort import *
import numpy as np
import matplotlib.pyplot as plot
file_name = input("Please enter the name of the file where your cammands are stored: ")
file_read = open(file_name, "r")
loaded_data = []
for line in file_read:
    line_list = line.strip("\n").split(";")
    if line_list[0].upper() == "L":
        file_name = line_list[1]
        attribute = line_list[2]
        if attribute == "School":
            value = line_list[3]
        elif attribute == "StudyTime":
            value = float(line_list[3])
        else:   
            value = int(line_list[3])
        loaded_data = load_data(file_name, (attribute, value))
        print("Data loaded")
    elif line_list[0].upper() == "S":
        attribute = line_list[1]
        ascending_desending = line_list[2]
        display_data = line_list[3]
        sorted_list = sort(loaded_data, ascending_desending, attribute)
        if display_data.upper() == "Y":
            print("Data sorted.")
            print(sorted_list)
        elif display_data.upper() == "N":
            print("Data sorted. <<<You selected not to display>>>")
    elif line_list[0].upper() == "C":
        curve_fit(add_average(loaded_data), line_list[1], line_list[2])
    elif line_list[0].upper() == "H":
        histogram(loaded_data, line_list[1])
    elif line_list[0].upper() == "E":
        print("exited program")
    else:
        print("Invalid command")


