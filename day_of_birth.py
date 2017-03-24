#!/usr/bin/env python
# coding: utf-8


def log(txt):
	print "===================================="
	print txt
	print "===================================="


def dob(d,m,y):
	# Zeller's Birthday

	# Stage: 4  Challenge Level:2 Challenge Level:2
	# What day of the week were you born on? Do you know?
	# Here's a way to find out.
	# For example, if your date of birth was 6 July 1989 :
	# D=6 , M=7 , and Y=1989
	# If M had been a 1 or 2, subtract 1 from Y and add 12 to M.
	# YF is made from the first two digits of Y and YL is made from the last two digits of Y.
	# To begin, work out the sum of all the integer parts of 2.6M−5.39 , of YF4 , and of YL4
	# Add D and YL into that total, and then subtract 2 lots of YF
	# Divide that final answer by 7 and notice the remainder .
	# A remainder value of 0 means the date was a Sunday, 1 means it was a Monday, 2 for a Tuesday, and so on.
	# Can you follow the method (what you actually have to do) ?
	# You could check some dates you happen to know the answer for ?
	# When you are getting good at using the method start to ask yourself how it works and why does it give the right result?
	# Why 2.6 and why 5.39?

	if m in [1,2]:
		y -= 1
		m += 12

	YF = int(str(y)[:2])
	YL = int(str(y)[2:])

	s1 = int(2.6*m-5.39)
	s2 = int(YF/4)
	s3 = int(YL/4)

	S = s1 + s2 + s3 + d + YL - 2*YF

	dow = S % 7
	return dow


if __name__ == '__main__':
	log("Zeller's Birthday")

	d = int(input("Type day of birth (1-31): "))
	m = int(input("Type month of birth (1-12): "))
	y = int(input("Type year of birth (aaaa): "))

	dow = dob(d,m,y)

	WEEKDAYS = ["SUNDAY","MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY",]

	log("You born at {0}".format(WEEKDAYS[dow]))