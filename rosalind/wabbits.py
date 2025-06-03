import math

"""
given positive integers n <= 40 and k <=5, return the total number of rabbit
pairs that will be present after n months if we begin with 1 pair and in each
generation, every pair of reproduction age rabbits produces a littler of k rabbit 
pairs instead of only one pair
"""

def mod_fib(n, k):
	fib = [0] * (n + 1) #made a list to hold count of rabbits
	fib[1] = 1 #says we begin with 1 pair
	if n >= 2:
		fib[2] = 1
	for i in range (k, n + 1):
		fib[i] = fib[i-1] + k * fib[i-2]
	return fib[n]
	
print(mod_fib(35, 2))