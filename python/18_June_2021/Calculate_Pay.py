"""
Name.: 		Bachhav Savata B.
Class.:		MCA-I
Roll No.:	03
Subject:	Python Programming
Program: 	WAP to calculate pay based on hrs and rate per hour
"""

hrs = input('Enter hours: ')
rts = input('Enter rates: ')
h=float(hrs)
r=float(rts)
def computepay(h,r) :
    if h <= 40.0 :
        pay = h * r
    else :
        hnew = h - 40.0
        pay = (40.0 * r + (hnew * (r * 1.5)))
    return pay
pay=computepay(h,r)
print ("Pay",pay)
