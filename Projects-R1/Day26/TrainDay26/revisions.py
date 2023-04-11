# # List comprehension
#
# # for loop - old way
#
# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)
#
# print(numbers)
# print(new_list)
#
# # for loop - comprehensive
# # list_name -> [operation_applied_to_item for item in old_list]
# # list_name -> [item-expression for item in iterator]
# #               n + 1           n       numbers
# new_list_compact = [n + 1 for n in numbers]
#
# name = "fernando"
# new_list_char = [letter for letter in name]
#
# my_double_list = [n * 2 for n in range(1, 5)]
# print(my_double_list)
#
# # conditional list comprehension
# # [item-expression for item in iterator if conditional].
#
# names = ["alex", "beth", "caroline", "dave", "elanor", "freddie"]
# short_names = [name for name in names if len(name) <= 4]
# all_caps_names = [name.upper() for name in names if len(name) >= 5]
#
# # dictionary comprehension
# # new_dict ->  {new_key:new_value for item in list}
# # new_dict ->  {new_key:new_value for (key,value) in dict.items()}
#
# import random
#
# # new_dict ->  {new_key:new_value for item in list}
# students_scores = {student: random.randint(1, 100) for student in names}
#
# # new_dict ->  {new_key:new_value for (key,value) in dict.items() if test }
# passed_students = {student: value for (student, value) in students_scores.items() if value > 50}
#
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# Loop through a data frame - not useful
# for (key, value) in student_data_frame.items():
#     print(value)

# Loop through rows of a data frame , in-build method on pandas
# for (index, row) in student_data_frame.iterrows():
#     # print(index)
#     print(row.student)
#     print(row.score)

for (index, row) in student_data_frame.iterrows():
    # print(index)
    if row.student == "Angela":
        print(row.score)
