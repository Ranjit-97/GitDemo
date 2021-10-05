# with open('test2.txt', 'w')as writer:
# 	n = writer.write("Ranjit\n")
# 	writer.write('Hello')
# 	print(n)
	

#append 
with open('test1.txt', 'a')as writer:
	list = ['Ranjit\n', 'Bhintade\n', 'Hello']
	writer.writelines(list)
	print('sucess')