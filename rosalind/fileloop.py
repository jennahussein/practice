"""
given a file containing at most 1000 lines, return a file containing all the even-numbered
lines from the original file assuming 1 based numbering of lines
"""

linenum = 1
file = open('rosalind_ini5.txt' ,'r')
for line in file:
	if linenum % 2 == 0:
		print(line, end = ' ')
	linenum += 1
	
file.close()