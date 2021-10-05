# print line by line using reading method

file = open('test.txt')

lines = file.readline()

while lines!= "":
	print(lines)
	lines = file.readline()

file.close()
