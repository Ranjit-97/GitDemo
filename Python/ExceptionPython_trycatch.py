try:
	with open('filenotpresent.txt', 'r') as reader:  #no error beacause test.txt file is present
		print(reader.read())

except Exception as e:
	print(e) # No such file or directory: 'filenotpresent.txt'

finally:
	print('this block is executed either try block is fail or success')