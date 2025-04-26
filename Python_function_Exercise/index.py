# Exercise 1: Create a function in python 

# def intro(name,age):
#     print(f"Hello my name is {name} and is {age}")

# intro("xyz",54)


# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 2:Create a function with variable length or arguments


# def func1(*args):
#     for item in args:
#         print(item)


# func1(1,2,3,4)

# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 3:Return multiple values from a fucntion

# def calculation(a,b):
#     return a+b,a-b

# print(calculation(30,20))


# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 4:Create a function with a default argument

# def show_employee(name,salary = 9000):
#     print(f"Name: {name} salary: {salary}")

# show_employee("ben",12000)
# show_employee("jessa")


# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 5:Create an inner function to calculate the addition in the following way

# def outer(a,b):
#     square = a**2

#     def inner(a,b):
#         return a+b
#     add = inner(a,b)

#     return add + 5

# result = outer(5,10)
# print(result)

# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 6:Create a recursive functio

# def addition(num):
#     if num:
#         return num + addition(num-1)
#     else:
#         return 0

# res = addition(10)
# print(res)


# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 8:Generate a python list of all the enven numbers between 4 to 30
# print([i for i in range(4,32,2)])
# print(list(range(4,32,2)))


# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 9:Find the largest item from a given list
# x = [4, 6, 8, 24, 12, 2]
# print(max(x))