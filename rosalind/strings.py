import math

"""
Given: A string s of length at most 200 letters and four integers a, b, c, and d
Return: The slice of this string from indices a through b and c through d (with space in 
between).
"""
s = 'FdsfHomalopsisYBf8E2Es9BG88bcheVTdCL7cKbUf3F2tnwMxTj667lJlNrVfj7NrWoLsyPWMhyr7PUsBSLjHhsfzV1jkHkcHugQGRn01LcWYS5QgUdt80HEffL67mPNYNhEPZU2UxC0UUOrr3t8sBuTbv9TasperumjI.'
def string_idx(s,a,b,c,d):
	half1 = s[a:b+1]
	half2 = s[c:d+1]
	return half1 + " " + half2
	
print(string_idx(s, 4, 13, 157, 163))