print("Hello")

# this first prog

print("\n")
#create a variable
a = 5   #integer
print(a)


# Data type is present in python but need not to mention them explicitly while creating a varibale
# need not declare a datatype 

str = "Hello"   #string
print(str)

#create multiple variable a one line
b, c, d = 2, 3.4, "hello"
print(c)

# no simicolon ';' at the end like java, C, C++

# print string with integer
# print("value is"+ b)  #it gives concatanation error beacuse we can not concate two different datatype
#concating a string and integer using format method 
print("{} {}".format("value is ", c)) 

# if same data type then no need of use format method 
print("hello" +" "+ "ranjit")
print(2 + 10)


#how to know what data type our each variable are having?
# check the data type of vaiable using type() method

print(type(c))


# Different data type that python support and catagorised data type


# complex data type
e = 100+3j  #complex number
print("type of variable",e,"is", type(e))

print("type of variable",d,"is", type(d))


print("hello","","ranjit")
print("A"+" "+ d+" " +"B")
print('Single code')


