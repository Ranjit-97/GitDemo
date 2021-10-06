print("git")
print("develop branch")


def functoin_demo(): #function declaration
	print("Hello!!!")

functoin_demo()#fuction calling


print("***********parameterized function************")
def functoin_demo2(name): #name is varible 
	print("welcome", name)
	print("welcome" +" "+name)

functoin_demo2("Ranjit")


print("*****sum of two integer*****")
def sum(a, b):
	c = a + b
	print(c)
	# print(a + b)

sum(2, 3)

print("****return***")
def return_sum(a, b):
	return a+b

print(return_sum(4, 5))#calling return function


print("***concating string and value****")
def concat(str, c):
	print("{} {} {}".format("Hello", str, c)) 

concat("ranjit", 24)

# c = 24
# str = "Ranjit"
# print(str)

# print("{} {} {}".format("value is", str, c))