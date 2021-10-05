str = "Hello, welcome!"
str2 = "happy?"
str3 = "Hello"
print(str)
print(str2)

print(str[0]) 	#H #index starts from zero
print(str[-1])	#print last character in string

print("****print substring*****")
print(str[1:5])	#ell #print subtring

print("****Concating string*****")
print(str+ " " +str2)

#check string is present in another string
#used in automation testing
print("****substring check***")
print(str3 in str) #if yes, print True

print("***Spilt the string****")
print(str.split(","))
# or
var = str.split(",")
print(var)#['Hello', ' welcome!'] #result is in list

print(var[0]) #Hello


print("****remove the white space****")
str4 = "   great "
print(str4.strip()) 


print("****remove only left side white space****")
print(str4.lstrip()) #remove the white space

print("****remove only right side white space****")
print(str4.rstrip()) #remove the white space


d = {0: 'a', 1: 'b', 2: 'c'}
for i in d:
	print(i)