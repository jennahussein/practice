import math

def mod_fib(n, k):
	fib = [0] * (n + 1)
	fib[1] = 1
	if n >= 2:
		fib[2] = 1
	for i in range (k, n + 1):
		fib[i] = fib[i-1] + k * fib[i-2]
	return fib[n]
	
print(mod_fib(35, 2))