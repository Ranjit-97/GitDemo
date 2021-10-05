class demo: #class variable
	num = 100
	# #Default Constructor
	# def __init__(self):
	# 	print("Default constructor")

	# Parameterized constructor
	def __init__(self, b, d):
		self.FirstNumber = b   #store this value in instace variable or store into memory
		self.LastNumber = d
		print("parameterized constructor is called")

	def getdata(self):
		print("Executing in method of class")
		print(self.num)   #or return demo.num 

	def sum(self):
		return self.FirstNumber + self.LastNumber + demo.num  #we never call variable by its simply name # it required self.

obj = demo(2, 3)#get value at run time
#constructor is automatically called when obj is created # so it called first construcotr method

obj.getdata() #call method
print("class variable is", obj.num)#call clas variable
print("sum is", obj.sum())

