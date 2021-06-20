"""
Name.: 		Bachhav Savata B.
Class.:		MCA-I
Roll No.:	03
Subject:	Python Programming
Program: 	WAP to calculate sum of all number in list
"""

total = 0
list1 = [20, 15, 10, 21, 9, 8.11]
for ele in range(0, len(list1)):
	total = total + list1[ele]
print("Sum of all elements in given list: ", total)
