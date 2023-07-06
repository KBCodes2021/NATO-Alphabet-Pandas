# # names = ["Alex", "Carolyn", "Dave", "Elanor", "Freddie"]
# # import random
# # #Dictionary comprehension, random student scores
# # students_scores = {student:random.randint(1, 100) for student in names}
# # passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
#
# # print(passed_students)
#
#
# # # BLANK DICTIONARY KEY
# # result = {new_key:new_value for item in list}
# # # BLANK DICTIONARY KEY
#
#
# # sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# #
# # result = {word:len(word) for word in sentence.split()}
# #
# # print(result)
#
#
# # Convert list to farienheight use:
#
# ####################BLANK DICTIONARY FRAME
#
#
#
#
# # result = {new_key:new_value for (key,value) in dictionary.items()}
#
# # # data.to_csv("new_data.csv")
#
#
# ###################
#
# # Convert list to farienheight use:
#
#
# # weather_c = {
# #     "Monday": 12,
# #     "Tuesday": 14,
# #     "Wednesday": 15,
# #     "Thursday": 14,
# #     "Friday": 21,
# #     "Saturday": 22,
# #     "Sunday": 24,
# # }
# #
# # weather_f= {day:temp_c * 9/5 + 32 for (day,temp_c) in weather_c.items()}
# #
# #
# # print(weather_f)
#
#
# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [66, 77, 44]
# }
# # Looping through dictionaries
#
# # for (key, value) in student_dict.items():
# #     print(value)
#
#
# # Looping through a dataframe
#
# import pandas
#
# student_data_frame = pandas.DataFrame(student_dict)
#
# # Looping through a dataframe
#
# # for (key, value) in student_data_frame.items():
#
#
# # Loop through rows of a dataframe
#
# for (index, rows) in student_data_frame.iterrows():
#     print(rows)
#
# # Can add rows.student to target row
