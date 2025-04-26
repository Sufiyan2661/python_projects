# Exercise 1A:Create a string of the first ,middle and last character
# str1 = 'james'
# print(str1[0], str1[int(len(str1)/2)], str1[len(str1)-1],sep="")

# str1 = 'james'

# res = str1[0]

# l = len(str1)

# mi = int(l/2)

# res += str1[mi]
# res += str1[l - 1]

# print("New String:", res)

# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 1B:Create a string made of the middle three characters
# def middle_three(str):
    # getting the first character
    # first = str[int(len(str)/2)-1]
    # second = str[int(len(str)/2)]
    # third = str[int(len(str)/2)+1]
    # print(first,second,third,sep="")

#     "now using the slicing"
#     mi = int(len(str)/2)
#     res = str[mi -1:mi +2]
#     print("Middle Three chars are :",res)


# middle_three("JhonDipPeta")

# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 2:Append new string in the middle of a given string
# s1 = "Ault"
# s2 = "Kelly"
# mi = int(len(s1)/2)
# x = s1[:mi:]
# x += s2
# x += s1[mi:]
# print(x)

# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 3:Create a new string made of the first, middle, and last characters of each input string.

# def f_m_l(s1,s2):
#     first = s1[0] + s2[0]
#     middle = s1[int(len(s1)/2)] + s2[int(len(s2)/2)]
#     last = s1[len(s1)-1] + s2[len(s2)-1]
#     print(first,middle,last,sep="")


# s1 = "America"
# s2 = "Japan"
# f_m_l(s1,s2)



# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 4:Arrange string characters such that lowercase letters should come first
# str1 = "PyNaTive"
# lower = ""
# upper = ""
# for ch in str1:
#     if ch.islower():
#         lower +=ch
#     else:
#         upper += ch
# print(lower+upper)

# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 5:Count all letters, digits, and special symbols from a given string.
# str1 = "P@#yn26at^&i5ve"
# char_count = 0
# digit_count = 0
# symbol_count = 0
# for ch in str1:
#     if ch.isalpha():
#         char_count += 1
#     elif ch.isdigit():
#         digit_count +=1
#     else:
#         symbol_count +=1

# print(f"chars = {char_count} \nDigits = {digit_count} \nsymbol = {symbol_count}")


# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 6:Create a mixed strign using the following rules
# s1 = "Abc"
# s2 = "Xyz"
# s1_length = len(s1)
# s2_length = len(s2)

# length = s1_length if s1_length > s2_length else s2_length
# result = ""

# s2 = s2[::-1]

# for i in range(length):
#     if i<s1_length:
#         result += s1[i]
#     if i < s2_length:
#         result += s2[i]
# print(result)


# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 7: String characters balance test
# s1 = "Ynf"
# s2 = "PYnative"
# check = True
# for ch in s1:
#     if ch in s2:
#         continue
#     else:
#         check = False

# print(check)


# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 8:Find all ocurrences of a substring in a given string by ignoring the case
# str1 = "Welcome to USA. usa awesome, isn't it?"
# sub_string = "USA"
# temp_string = str1.lower()

# count = temp_string.count(sub_string.lower())
# print("The USA count is: ",count)

# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 9:Calculate the sum and average of the digits present in a string.
# str1 = "PYnative29@#8496"
# count = 0
# add = 0
# for ch in str1:
#     if ch.isdigit():
#         add += int(ch)
#         count +=1
# print(f"Sum is :{add} Average is {add/count}")


# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 10:Write a program to count occureances of all characters within a string
# str1 = "Apple"

# dic = {}
# for ch in str1:
#     count = str1.count(ch)

#     dic[ch] = count

# print(dic)

# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 11:Reverse aa given string

# str1 = "PYnative"
# str1 = str1[::-1]
# print(str1)


# str1 = "".join(reversed(str1))
# print(str1)

# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 12:Find the last positon of a given substring
# str1 = "Emma is a data scientist who knows Python. Emma works at google."

# index = str1.rfind("Emma")
# print(index)


# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 13:Split a string on hypens
# str1 = "Emma-is-a-data-scientist"
# lst = str1.split("-")
# for i in lst:
#     print(i)


# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 14:Remove empty strings from a list of strings
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
# new_list = []
# for str in str_list:
#     if str == "":
#         continue
#     else:
#         new_list.append(str)

# print(new_list)


# using filter

# new_str_list = list(filter(None,str_list))
# print(new_str_list)

# ++++++++++++++++++++++++++++++++++++++++++++
# 15 :Remove special symbols / punctuation from a string
# import string
# str1 = "/*Jon is @developer & musician"
# new_str = str1.translate(str.maketrans("","",string.punctuation))
# print("New string is ",new_str)

# Usin regex
# import re
# str1 = "/*Jon is @developer & musician"
# res = re.sub(r'[^\w\s]','',str1)
# print("New string is :",res)


# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 16: Removal all characters from a string except integers
# str1 = 'I am 25 years and 10 months old'
# res = ''
# for i in str1:
#    if i.isdigit():
#       res += i
# print(res)

# Using list comprehension

# res = "".join([item for item in str1 if item.isdigit()])
# print(res)

# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 17:Find words with both alphabets and numbers
# str1 = "Emma25 is Data scientist50 and AI Expert"
# lst = str1.split(" ")
# for word in lst:
#     if not word.isalpha():
#         print(word)


# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 18:Replace each symbol with # in the following string
# import string
# str1 = '/*Jon is @developer & musician!!'
# replace_char = "#"

# for char in string.punctuation:
#     str1 = str1.replace(char, replace_char)

# print("The string after replacement: ",str1)








