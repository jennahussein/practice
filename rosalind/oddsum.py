import math

"""
given two positive integers a and b, return the sum of all integers from a through b
"""

def oddsum(a, b):
	total = 0
	for i in range(a,b+1):
		if i % 2 != 0:
			total += i
	print(total)


oddsum(4296,9279)		