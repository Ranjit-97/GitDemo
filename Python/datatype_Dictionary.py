

a = {1:"first name",2:"last name", "age":33, "a":"Hello world"}  #key:value


print(a[1])#print value having key=1
print(a[2])#print value having key=2
print(a["age"])#print value having key="age"
print(a["a"])#we print the value here



print("\n")
#create a dynamic dictionay at run time
#steps- first create an empty dictionay then gives constraint or values
dict = {} #create an empty dictionay
print(dict)#print empty dictionary

dict["firstname"] = "Ranjit"
dict["lastname"] = "Bhintade"
dict["age"] = 24
print(dict)
print(dict["lastname"])