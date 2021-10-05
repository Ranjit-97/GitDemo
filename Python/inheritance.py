# from Python.oops import demo  error
from oops import demo

class childimplemet(demo):
	num2  = 200
     
     #in child constructor mandatory to have parent constructor, if parent constructor is not default
     #if default need not to called 
	def __init__(self):  #default constructor
		demo.__init__(self, 2, 3)    

	def getCompletedata(self):
		return childimplemet.num2 + self.num + self.sum()


obj2 = childimplemet()  
print(obj2.getCompletedata())