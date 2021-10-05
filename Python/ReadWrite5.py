# write
# file = open('test.txt')#file is the object
# file.close()

#read the file and store it into list
#reverse list
#write the list back into the file

with open('test.txt', 'r') as reader:   #reader is obj  #no need to close file
	content = reader.readlines() 
	reversed(content)
	with open('test.txt', 'w') as writer:
		for line in reversed(content):
			writer.write(line)
