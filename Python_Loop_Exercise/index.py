# Exercise 1: Print first 10 natural numbers using while loop

# for i in range(1,11):
#     print(i)

# +++++++++++++++++++++++++++++++++++++++++++++
# Exercise 2: Print the following pattern
# for row in range(1,6):
#     for col in range(1,row+1):
#         print(col,end=" ")
#     print()

# +++++++++++++++++++++++++++++++++++++++++++++
# Exercise 3: Calculate sum of all numbers from 1 to a given number

# num = int(input("Enter the number: "))
# total = 0
# for i in range(1,num+1):
#     total += i
# print("Sum is :",total)

# +++++++++++++++++++++++++++++++++++++++++++++
# Exercise 4: Print multiplication table of a given number
# num = int(input("Enter the number: "))
# for i in range(1,11):
#     print(num*i)

# +++++++++++++++++++++++++++++++++++++++++++++
# Exercise 5:Display numbers from a list using a loop
# numbers = [12, 75, 150, 180, 145, 525, 50]
# for num in numbers:
#     if num > 500:
#         break
#     elif num > 150:
#         continue
#     elif num % 5 == 0:
#         print(num)

# +++++++++++++++++++++++++++++++++++++++++++++
# Exercise 6:Count the total number of digits in a number

# counter = 0
# num = 75869
# while num != 0:
#     num = num // 10
#     counter += 1
# print(counter)

# +++++++++++++++++++++++++++++++++++++++++++++
# Exercise 7:Print the following pattern
# for row in range(1,6):
#     for col in range(1,row+1):
#         print(col,end=" ")
#     print()
    
# n = 5
# k = 5
# for i in range(0,n+1):
#     for j in range(k-i,0,-1):
#         print(j,end=" ")
#     print()

# +++++++++++++++++++++++++++++++++++++++++++++
# Exercise 8:Print list in reverse order using a loop
list1 = [10,20,30,40,50]
# size = len(list1) -1
# for i in range(size, -1,-1):
#     print(list1[i])
# USING REVERSED() FUNCTION

# new_list = reversed(list1)
# for item in new_list:
#     print(item)


# +++++++++++++++++++++++++++++++++++++++++++++
# Exercise 9:Display numbers from -10 to -1 using for loop
# for i in range(-10,0):
#     print(i)

# +++++++++++++++++++++++++++++++++++++++++++++
# Exercise 10:Display a message "Done" after the succesful execution of the for loop
# for i in range(6):
#     print(i)
# else:
#     print("Done!")

# +++++++++++++++++++++++++++++++++++++++++++++
# Exercise 11:Print all prime numbers within a range

# start = 25
# end = 50
# print(f"Prime numbers between {start} and {end} are:")

# for num in range(start,end+1):
#     if num > 1:
#         for  i in range(2,num):
#             if (num%i) == 0:
#                 break
#         else:
            # print(num)

# +++++++++++++++++++++++++++++++++++++++++++++
# Exercise 12:Display Fibonacci series up to 10 terms
# num1 = 0
# num2 = 1
# for i in range(11):
#     print(num1)
#     result = num1 + num2
#     num1 = num2
#     num2  = result

# +++++++++++++++++++++++++++++++++++++++++++++
# Exercise 13:find the factorial of a given number

# factorial = 1 
# n = 5
# for i in range(1,n+1):
#     factorial = factorial * i
# print(factorial)

# +++++++++++++++++++++++++++++++++++++++++++++
# Exercise 14:Reverse a integer number
# num = 76542
# reverse_number = 0
# while num > 0:
#     reminder = num % 10
#     reverse_number = (reverse_number * 10) + reminder
#     num = num // 10
# print("Reverse Number ",reverse_number)
# +++++++++++++++++++++++++++++++++++++++++++++
# Exercise 15:Print elements from a given list present at odd index positions
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for i in my_list[1::2]:
#     print(i,end=" ")

# +++++++++++++++++++++++++++++++++++++++++++++
# Exercise 16:Calculate the cube of all numbers from 1 to given number
# input_number = 6
# for i in range(1,input_number+1):
#     print(f"Current Number is : {i} and the cube is {i**3}")

# +++++++++++++++++++++++++++++++++++++++++++++
# Exercise 17:Find the sum of the series up to n terms
# n = 5
# start = 2
# sum_seq = 0

# for i in range(0,n):
#     print(start,end="+")
#     sum_seq += start

#     start = start * 10 +2
# print("\nSum of above series is :",sum_seq)

# +++++++++++++++++++++++++++++++++++++++++++++
# Exercise 18:Print the following pattern
# for row in range(1,6):
#     for col in range(1,row+1):
#         print("*",end=" ")
#     print()
# for row in range(5,0,-1):
#     for col in range(0,row-1):
#         print("*",end=' ')
#     print("\r")