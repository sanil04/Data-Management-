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