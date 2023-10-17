# ECOR 1042 Lab 6 - Individual submission for text_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Sanil Srivastava"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101268578"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-003"

#==========================================#
# Place your script for your text_UI after this line
from load_data import load_data 
from sort import sort
from curve_fit import curve_fit
from histogram import histogram

cont = True

while cont == True :
    
    print("The available commands are:")
    print("L = Load Data")
    print("S = Sort Data")
    print("C = Curve Fit")
    print("H = Histogram")
    print("E = Exit\n")
    command = input("Please type your command: ")
    print("")
    
    
    
    if command == "l" or command == "L":
        
        data_loaded = []
        
        filename = input("Please enter the name of the file: ")
        
        attribute_true = True
        
        while attribute_true == True :
            
            attribute_true = False
            attribute = input("Please enter the attribute to use as a filter: ")
            
            if attribute == "School":
                value = input("Please enter the value of the attribute: ")
                data_loaded = load_data(filename,("School",value))
                print ("Data loaded")
            
            elif attribute == "Age":
                value = int(input("Please enter the value of the attribute: "))
                data_loaded = load_data(filename,("Age",value))
                print ("Data loaded")
           
            elif attribute == "Failures":
                value = int(input("Please enter the value of the attribute: "))
                data_loaded = load_data(filename,("Failures",value))    
                print ("Data loaded")
            
            elif attribute == "Health":
                value = int(input("Please enter the value of the attribute: "))
                data_loaded = load_data(filename,("Health",value))   
                print ("Data loaded")
        
            elif attribute == "All":
                data_loaded = load_data(filename,("All",0))
                print ("Data loaded")
                
            else :
                
                print("Invalid attribute")
                print("Valid attributes are: 'School', 'Age', 'Failures', 'Health', or 'All'")
                print("Please try again")
                attribute_true = True
            
        
            print("")
        
      
       
    elif command == "s" or command == "S":
        
        sorted_data = []
        
        if len(data_loaded)>0:
            
            attribute_true = True 
            
            while attribute_true == True :
                
                attribute_true = False
       
                print("Please enter the attribute you want to use for sorting:")
                print("'Age'  'Studytime'  'Failures'  'G_Avg' ")
                sort_method = input(":")
                
                while True:
                    direction = input("Ascending (A) or Descending (D) order: ")
                    if direction == "A" or direction == "D" :
                        break
                    else:
                        print("Invalid Input")
                        print("Please enter 'A' or 'D'")
                        
                
                if sort_method == "Age" :
                    sorted_data = sort(data_loaded, direction, "Age")
                    print("Data sorted")
                    
                elif sort_method == "Studytime" :
                    sorted_data = sort(data_loaded, direction, "Studytime")
                    print("Data sorted")  
                          
                elif sort_method == "Failures" :
                    sorted_data = sort(data_loaded, direction, "Failures")
                    print("Data sorted")   
                    
                elif sort_method == "G_avg" :
                    sorted_data = sort(data_loaded, direction, "G_avg")
                    print("Data sorted")                
                
                else:
                    
                    print("Invalid input. Please enter on of the following:")
                    print("'Age'  'Studytime'  'Failures'  'G_Avg' ")
                    attribute_true = True
                    
            while True:
                
                print("Do you want to display the data?")
                YorN = input("'Y' or 'N' : ")
                
                if YorN == "Y":
                    print(sorted_data)
                    print("")
                    break
                elif YorN == "N":
                    break
                else :
                    print("Invalid input")
            
        
        else:
            
            print("No data loaded")
            print("Please load data first")
            print("")
        
    
    
    elif command == "c" or command == "C": 
        
        if len(data_loaded)>0 :
            
            while True:
                avg = input("Please enter the attribute you want to use to find the best fit for G_Avg: ")
                
                if avg == "School" or avg =="Age" or avg =="StudyTime" or avg =="Failures" or avg =="Health" or avg =="Absences" or avg == "G1" or avg == "G2" or avg == "G3" :
                    break
                else:
                    print("Invalid Input. Please enter one of the following: ")
                    print("'School'  'Age'  'StudyTime'  'Failures'  'Health'  'Absences'  'G1'  'G2'  'G3'")
                    
            while True:
                degree = int(input("Please enter the order of the polynomial to be fitted: "))
                if degree == 1 or degree == 2 or degree == 3 or degree == 4 or degree == 5:
                    break 
                else :
                    print("Please enter an int between 1 and 5 inclusive")
                
                
                
            curve_fit(data_loaded,avg,degree)
                
            
            
        else:
            
            print("No data loaded")
            print("Please load data first")
            print("")            
        
    
            
    elif command == "h" or command == "H":
        
        if len(data_loaded)>0 :
            
            while True:
                
                plotting = input("Please enter the attribute you want to use for plotting: ")
                
                if plotting == "School" or plotting =="Age" or plotting =="StudyTime" or plotting =="Failures" or plotting =="Health" or plotting =="Absences" or plotting == "G1" or plotting == "G2" or plotting == "G3" :
                    histogram(data_loaded,plotting)
                    break
                else:
                    print("Invalid Input. Please enter one of the following: ")
                    print("'School'  'Age'  'StudyTime'  'Failures'  'Health'  'Absences'  'G1'  'G2'  'G3'")                
                
                
                
            
        else:
            
            print("No data loaded")
            print("Please load data first")
            print("")            
        
        
        
    elif command == "e" or command == "E":
        print("Exited Program")
        break 
    
    else :
        
        print("Invalid Input")
        print("Please Retry\n")
