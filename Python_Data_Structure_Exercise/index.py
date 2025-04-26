# Exercise 1: Create a list by picking an odd-index items from the first list and even index items from the second
# l1 = [3, 6, 9, 12, 15, 18, 21]
# l2 = [4, 8, 12, 16, 20, 24, 28]
# new_l1 = []
# new_l2 = []
# for index in range(len(l1)):
#     if index % 2 != 0:
#         new_l1.append(l1[index])
#     if index % 2 == 0:
#         new_l2.append(l2[index])
# print(new_l1+new_l2)

# Using slicing
# odd = l1[1::2]
# print("odd values:", odd)
# even = l2[0::2]
# print("Even values: ",even)
# final = odd+even
# print("merged list = ",final)

# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 2:Remove and add item in a list
# list1 = [54, 44, 27, 79, 91, 41]
# removed = list1.pop(4)
# print("List after removing element at index 4 ",list1)
# add = list1.insert(2,removed)
# print("List after adding element at index 2 ",list1)
# list1.append(22)
# print("List after adding element at last ",list1)

# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 3:Slice list into 3 equal chunks and reverse each chunk
# sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

# length = len(sample_list)
# chunk_size = int(length/3)
# start = 0
# end = chunk_size


# for i in range(3):
#     indexes = slice(start,end)

#     list_chunk = sample_list[indexes]
#     print("Chunk ",i, list_chunk)

#     print("After reversing it ",list(reversed(list_chunk)))

#     start = end
#     end += chunk_size


# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 4:Count the occurrence of each element from a list
# sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
# count_dict = dict()
# for item in sample_list:
#     if item in count_dict:
#         count_dict[item] += 1
#     else:
#         count_dict[item] = 1

# print("Printing count of each item ",count_dict) 

# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 5:Create a python set such that it shows the element from both lists in pair.

# first_list = [2, 3, 4, 5, 6, 7, 8]
# second_list = [4, 9, 16, 25, 36, 49, 64]

# result = zip(first_list,second_list)
# result_set = set(result)
# print(result_set)


# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 6:Find the intersection (common) of two sets and remove those elements from the first set
# first_set = {23, 42, 65, 57, 78, 83, 29}
# second_set = {57, 83, 29, 67, 73, 43, 48}

# print(f"First set {first_set} \nSecond set {second_set}")
# intersection = first_set.intersection(second_set)
# print("Intersection is ",intersection)
# for item in intersection:
#     first_set.remove(item)

# print("First set after removing common element ",first_set)

# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 7:Checks if one set is a subset or superset of another set. If found,delete all elements from that set
# first_set = {27, 43, 34}
# second_set = {34, 93, 22, 27, 43, 53, 48}

# print("First set is subset of second set ",first_set.issubset(second_set))
# print("Second set is subset of first set ",second_set.issubset(first_set))

# print("First set is superset of second set ",first_set.issuperset(second_set))
# print("Second set is superset of first set ",second_set.issuperset(first_set))

# if first_set.issubset(second_set):
#     first_set.clear()
# if second_set.issubset(first_set):
#     second_set.clear()

# print("First set ",first_set)
# print("Second set ",second_set)


# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 8:Iterate a given list and check if a given element exists as key's value in a dictionary.If not, delete it from the list.

# roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
# sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

# for num in roll_number:
#     if num in sample_dict.values():
#         print(num)
#     else:
#         roll_number.remove(num)
# print("list after removing = ",roll_number)

# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 9:Get all values from the dictionary and add them to a list but don`t add duplicates.

speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
# lst = []
# for value in speed.values():
#     lst.append(value)
# print("answer ",list(set(lst)))

# speed_list = list()

# for val in speed.values():
#     if val not in speed_list:
#         speed_list.append(val)
# print("Unique list ",speed_list)

# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 10:Remove duplicates from a list and create a tuple and find the minimum and maximum number

# sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
# sample_list = list(set(sample_list))
# print("Unique items ",sample_list)

# tp = tuple(sample_list)

# print("Tuple ",tp)

# print("Minimum number ",min(tp))
# print("Maximum number ",max(tp))