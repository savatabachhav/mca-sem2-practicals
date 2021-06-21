"""
Name.: 		Bachhav Savata B.
Class.:		MCA-I
Roll No.:	03
Subject:	Python Programming
Program: 	WAP to display multiplication table
"""

for i in range(1,11):
    for j in range(1,11) :
        print('{:8}'.format(i*j), end=" ")
    print()