import math

s = 'FdsfHomalopsisYBf8E2Es9BG88bcheVTdCL7cKbUf3F2tnwMxTj667lJlNrVfj7NrWoLsyPWMhyr7PUsBSLjHhsfzV1jkHkcHugQGRn01LcWYS5QgUdt80HEffL67mPNYNhEPZU2UxC0UUOrr3t8sBuTbv9TasperumjI.'
def string_idx(s,a,b,c,d):
	half1 = s[a:b+1]
	half2 = s[c:d+1]
	return half1 + " " + half2
	
print(string_idx(s, 4, 13, 157, 163))