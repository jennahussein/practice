import math 

"""
Given a string, s, return the number of occurrences of each word in s, separated by spaces
"""


words = {}
with open("rosalind_ini6.txt", "r") as file:
	for line in file:
		for word in line.split():
			if word not in words:
				words[word] = 0
			words[word] += 1

for word, count in words.items():
	print(word, words[word])
