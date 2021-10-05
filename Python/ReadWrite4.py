file = open('test.txt')

#read each line by line in list and written
for line in file.readlines():
	print(line)

# print(file.readlines())#print file outputs in lists #['abc\n', 'Ranjit\t\t\n', 'Bhintade\n', '123abc']

file.close()
