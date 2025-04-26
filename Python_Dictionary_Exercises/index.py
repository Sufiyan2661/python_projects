# Exercise 1:Convert two list into a dictionary.

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
# dic = {}
# for i in range(0,3):
#     dic[keys[i]] = values[i]
# print(dic)

# USING ZIP() FUNCTION
# res = dict(zip(keys,values))
# print(res)

# USING .UPDATE() METHOD
# res = dict()
# for i in range(len(keys)):
#     res.update({keys[i]:values[i]})
# print(res)

# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 2:Merge two python dictionaries into one
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# dict3 = {**dict1,**dict2}
# print(dict3)

# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 3:Print the value of key 'history' from the below code:
# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
# print(sampleDict["class"]["student"]["marks"]["history"])

# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 4:Initialize dictionary with default values.
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
# res  = dict.fromkeys(employees,defaults)
# print(res)

# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 5:Create a dictionary by extracting the ekeys from a given dictionary
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}

# Keys to extract
# keys = ["name", "salary"]
# res  = {}
# for key in keys:
#     if key in sample_dict:
#         res[key] = sample_dict[key]

# print(res)


# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 6:Delete a list of keys from a dictionary
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}

# # Keys to remove
# keys = ["name", "salary"]
# for key in keys:
#     if key in sample_dict:
#         sample_dict.pop(key)
# print(sample_dict)

# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 7:Check if a value exists in a dictionary
# sample_dict = {'a': 100, 'b': 200, 'c': 300}
# check_value = 200
# for value in sample_dict.values():
#     if value == check_value:
#         print(f"{check_value} present in a dict")

# if check_value in sample_dict.values():
#     print(f"{check_value} present in dict")


# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 8:Rename key of a dictionary
# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }
# sample_dict["location"] = sample_dict.pop("city")
# print(sample_dict)
 

# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 9:Get the key of a minimum value from the following dictionary
# sample_dict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }
# print(min(sample_dict))

# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 10:Change the value of a key in nested dictionary
# sample_dict = {
#     'emp1': {'name': 'Jhon', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 500}
# }
# sample_dict['emp3']['salary'] = 8500
# print(sample_dict)