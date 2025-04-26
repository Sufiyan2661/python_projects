# Exercise 1: Accept number form user
# num1 , num2 = map(int,input("Enter two numbers: ").split())
# print(num1 + num2)

# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 2: Display three string "Name", "Is", "James" as "Name**is**james"

# print("Name","is","james",sep="**")


# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 3: convert decimal to octal using print() out formatting

# num = 8
# print("%o"% num)

# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 4:Display float number with 2 decimal places using print()
# num = 458.541315
# print("%.3f"%num)

# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 5:Accept a list of 5 float numbers as an input from the user

# numbers = []

# for i in range(0,5):
#     print("Enter number at location ",i," :")

#     item = float(input())

#     numbers.append(item)


# print("user list:",numbers)


# ++++++++++++++++++++++++++++++++++++++++++++
# Exercise 6: Write all content of a given file into a new file by skipping line number 5


# with open("test.txt","r") as fp:
#     lienes = fp.readline()

# with open("new_file.txt","w") as fp:
#     count = 0

#     for line in lienes:
#         if count == 4:
#             count +=1
#             continue
#         else:
#             fp.write(line)
        # count +=1

# +++++++++++++++++++++++++++++++++++++++++++++
# Exercise 7: Accept any three string from one input() call
# str1,str2,str3 = input("Enter three name ").split()
# print("Name1",str1)
# print("Name2",str2)
# print("Name3",str3)

# +++++++++++++++++++++++++++++++++++++++++++++
# Exercise 8:format variables using string.format() method.

# totalMoney = 1000
# quantity = 3
# price = 450
# print(f"I have {totalMoney} dollars so I can buy {quantity} football for {"%.2f"%price} dollors.")


# +++++++++++++++++++++++++++++++++++++++++++++
# Exercise 9: Check file is empty or not
# import os
# if os.stat("new_file.txt").st_size == 0:
#     print("the file is empty")
# else:
#     print("the file is not empty")


# print(os.stat("new_file.txt").st_size)

# +++++++++++++++++++++++++++++++++++++++++++++
# Exercise 10:Read line number 4 from the following file

# with open("test.txt","r") as obj:
#     lines = obj.readlines()

#     print(lines[3])