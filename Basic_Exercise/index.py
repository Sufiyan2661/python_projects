# Exercise 1: Calculate the multiplication and sum of two numbers.
# def multi_and_sum(a,b):
#     product = a * b
#     if product <= 1000:
#         return product
#     else:
#         return  a+b
    
# print(multi_and_sum(20,30))
# print(multi_and_sum(40,30))


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Exercise 2: Print the sum of the current number and a previous number

# previouse_num = 0

# for i in range(1,11):
#     x_sum = previouse_num + 1
#     print(f"Current Number {i} Previous Number {previouse_num} Sum: {x_sum}")

#     previouse_num = i


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Exercise 3: Print characters present at en even index number
# str1 = input("enter a word: ")

# for i in range(0,len(str1),2):
#     print(str1[i])



# +++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Exercise 4: Remove first n characters from a string

# def remove_chars(str,num):
#     if num > len(str):
#         return
#     else:
#         return str[num::1]
    
# print(remove_chars("pynative",4))
# print(remove_chars("pynative",2))


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Exercise 5: Check if the first and last number of a list are the same

# def check_first_and_last(lst):
#    first_element = lst[0]
#    last_element = lst[-1]
#    return first_element == last_element

# numbers_x = [10, 20, 30, 40, 10]
# numbers_y = [75, 65, 35, 75, 30]
# print(check_first_and_last(numbers_x))
# print(check_first_and_last(numbers_y))

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Exercise 6: Display numbers divisible by 5
# def divisible_by_five(lst):
#     for num in lst:
#         if num % 5==0:
#             print(num)

# divisible_by_five([10, 20, 33, 46, 55])

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Exercise 7: Find The number of occurances of substring in a string

# str_x = "Emma is good developer. Emma is a writer"
# print(str_x.count("Emma"))

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Exercise 8:Print the following pattern

# for row in range(1,6):
#     for col in range(1,row+1):
#         print(row,end="")
#     print()

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Exercise 9:Check Palindrome number
# def palindrome(number):
#     reverse = int(str(number)[::-1])
#     if number == reverse:
#         print("Given number is palindrome")
#     else:
#         print("given number is not palindrome")

# palindrome(121)
# palindrome(125)

# def palindrome(number):
#     print("Original number",number)
#     original_number = number
#     reverse_num = 0
#     while number > 0:
#         reminder = number % 10
#         reverse_num = (reverse_num * 10) + reminder
#         number = number//10
#     if original_number == reverse_num:
#         print("Given number is palindrome")
#     else:
#         print("Given number is not palindrome")


# palindrome(121)
# palindrome(123)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Exercise 10: Merge two lists using the following condition
# def merge_list(lst1,lst2):
#     result_list = []
#     for num in lst1:
#         if num %2 != 0:
#             result_list.append(num)
#     for num in lst2:
#         if num %2 == 0:
#             result_list.append(num)
#     return result_list


# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
# print(merge_list(list1,list2))


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Exercise 11: Get each digit from a number in the reverse order.

# def num_in_reverse(num):
#     print("the original number",num)

#     while num >0:
#         digit = num % 10
#         num = num // 10
#         print(digit, end="")

# num_in_reverse(7536)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Exercise 12: Calculate the income tax
# income = 45000
# text_payable = 0
# print("Given income",income)

# if income <= 10000:
#     text_payable = 0
# elif income <= 20000:
#     # no tax of first 10000
#     x = income - 10000

#     # 10% tax payable
#     tax_payable = x * 10/100
# else:
#     tax_payable = 0

#     tax_payable = 10000 * 10/100

#     tax_payable += (income - 20000) * 20/100


# print("Total tax to pay is = ", tax_payable)

# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 13: Print the multiplication table from 1 to 10


# i = 1
# while(i <= 10):
#     for num in range(1,11):
#         print(i * num, end=" ")
#     i += 1
#     print("\t\t")


# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 14: Print the downward half-pyramid
# for row in range(1,6):
#     for col in range(5,row -1,-1):
#         print("*",end=' ')
#     print()


# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 15: Get an int value of base raises to the power of exponent

# def exponent(base,exp):
#     print(base**exp)

# exponent(5,4)

# def exponent(base,exp):
#     num = exp
#     resutl = 1
#     while num > 0:
#         resutl = resutl * base
#         num -= 1
#     print(base, " raises to the power of ",exp," is : ",resutl)
# exponent(5,4)