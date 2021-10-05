
# open file and read the contents
file = open('test.txt') #or text file path
print(file.read())  # read all content of the file


print("****read only first two character in the file***")
file = open('test.txt') 
print(file.read(5)) #read n number of character by passing parameter

file.close()