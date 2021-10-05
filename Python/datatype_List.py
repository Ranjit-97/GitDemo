#list

values= [1, 3, 5, 6, "abcdef", 4.5]
print(values)#[1, 3, 5, 6, 'abcdef', 4.5]
print(values[0]) #1
print(values[-1])#4.5 #print last values in list
print(values[2:5])#[5, 6, 'abcdef'] #get sub list values



values.insert(5, "pqr")#[1, 3, 5, 6, 'abcdef', 'pqr', 4.5] # inset record
print(values)


values.pop(5)#remvove item by index
print(values)#[1, 3, 5, 6, 'abcdef', 4.5]

values.append("pqr") #add item in last postion
print(values)#[1, 3, 5, 6, 'abcdef', 4.5, 'pqr']


values[4] = "Ranjit" #update value
print(values)#[1, 3, 5, 6, 'Ranjit', 4.5, 'pqr']

del values[0]#same like pop
print(values)#[3, 5, 6, 'Ranjit', 4.5, 'pqr']

print("\n")
l = list(range(10))
print(l)# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l.clear()#remove all the items
print(l)# []