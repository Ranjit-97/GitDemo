
a = 4
while a >= 1:
	if a != 3:   
		print(a) #3 is skip - not print in output

	a = a -  1  #after printing 1 condition become false 
print ("execution is done")



print("************")
a = 10
while a >= 1:
	# if a == 9:
	# 	a = a - 1
	# 	continue
	if a == 3:   #3 is not print in output
		break
	print(a) #print only 4

	a = a -  1  #after printing 1 condition become false 
print ("execution is done")
