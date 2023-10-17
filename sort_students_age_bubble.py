# ECOR 1042 Lab 5 - Individual submission for sort_students_age_bubble

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "William Chicquen"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101275149"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-003"

#==========================================#
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


