"""
Name.: 		Bachhav Savata B.
Class.:		MCA-I
Roll No.:	03
Subject:	Python Programming
Program: 	WAP to display three types of pyramid
"""

n=11 #number of spaces

print('*****CENTER ALIGNED PYRAMID*****')
for i in range(1,11):
    print(' '*n, end='')
    print('* '*(i))
    n=n-1
print('*****LEFT ALIGNED PYRAMID*****')
for i in range(1,11):
    print('* '*(i))
print('*****RIGHT ALIGNED PYRAMID*****')  
for i in range(1,11):
    print('* '*(i))