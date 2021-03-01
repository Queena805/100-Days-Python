#List comprehension

#new_list = [new_item for item in list if test]


#Dictionary Comprehension

#new_dict = {new_key: new_value for item in list}

student_score = {
    "student": ["Alex", "Caroline","Queena"],
    "score":[98,87,99]

}
# Looping through dictionaries:
for (key,value) in student_score.items():
    print(key)

import pandas
student_df = pandas.DataFrame(student_score)
print(student_df)

##Loop through a data frame
# for (key,value) in student_score.items():
#     print(value)

#Loop through row of a data frame
for (index, row) in student_df.iterrows():
    if row.student == "Queena":
        print(row.score)