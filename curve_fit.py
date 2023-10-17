# ECOR 1042 Lab 6 - Individual submission for curve_fit function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Neel Leuva"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "10125773"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-003"

#==========================================#
# Place your curve_fit function after this line

import numpy as np


def curve_fit(data_list: list[dict], key: str, deg: int) -> list[dict]:
    """
    Input a list of dictionaries, a key, and a degree. It returns an output of the function of best fit between the key and G_Avg. The deg input determines the power of the function of best fit. 

    Preconditions: Each dictionary in data_list should have the key G_Avg. The value associated to the key should be an integer. Deg should be between 1 and 5 inclusive. 

    >>>curve_fit([{'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.67}, ..., {'Age': 17, 'StudyTime': 1.0, 'Failures': 3, 'Health': 3, 'Absences': 2, 'G1': 8, 'G2': 8, 'G3': 10, 'G_Avg': 8.67}], "G1", 1)
    'y = 1.13x + 0.93'

    >>>curve_fit([{'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.67}, ..., {'Age': 17, 'StudyTime': 1.0, 'Failures': 3, 'Health': 3, 'Absences': 2, 'G1': 8, 'G2': 8, 'G3': 10, 'G_Avg': 8.67}], "Health", 5)
    'y = 2.25x^5 + 17.46x^4 + -8.13x^3 + 0.46x^2 + 0.34x + -0.05'


    """
    g_avg = []
    key_values = []
    for data in data_list:
        g_avg.append(data['G_Avg'])
        key_values.append(data[key])
    g_avg = np.array(g_avg)
    key_values = np.array(key_values)

    unique_key = np.unique(key_values)
    avg_g_avg = []
    for avg in unique_key:
        mask = (key_values == avg)
        avg_g_avg.append(np.mean(g_avg[mask]))
    avg_g_avg = np.array(avg_g_avg)

    if deg <= len(avg_g_avg):
        coefficients = np.polyfit(unique_key, avg_g_avg, deg)
        poly = 'y = '
        degree = deg
        for i in range(len(coefficients)):
            c = coefficients[-i - 1]
            if degree > 1:
                poly += f'{c:.2f}x^{degree} + '
            elif degree == 1:
                poly += f'{c:.2f}x + '
            else:
                poly += f'{c:.2f}'
            degree -= 1
    else:
        coefficients = np.polyfit(unique_key,
                                  avg_g_avg, len(avg_g_avg) - 1)
        poly = 'y = '
        degree = len(avg_g_avg) - 1
        for i in range(len(coefficients)):
            c = coefficients[-i - 1]
            if degree > 1:
                poly += f'{c:.2f}x^{degree} + '
            elif degree == 1:
                poly += f'{c:.2f}x + '
            else:
                poly += f'{c:.2f}'
            degree -= 1
    return poly
# Do NOT include a main script in your submission



