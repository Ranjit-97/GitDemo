# declare a vaiable to iterate the value in list, in java we write as int i = 0; i<n; i++
obj = [2, 4, 5, 8] #list
for i in obj:       #declare variable i # for, in are the keywords
	print(i)
	#print(i*2)
print("\n")

#if list is not given we use range
# print natural number from 1 to 5
for j in range(1, 6): #range(i, j) -> i to j-1
	print(j)
print("\n")


# print sum of natural number from 1 to 5
sum = 0
for j in range(1, 6): #range(i, j) -> i to j-1 #for(i=1; i<=5; i++) #here bydeafult incement by one
	sum = sum + j
	print(sum)

print("*********************")
print("increment by 5")
for k in range(1, 10, 5): #range(i, j, k) -> i to j-1 #k is incrementation 
	print(k)


print("******skipping first idex******")
for m in range(10): #it print 0  to 9 numbers #bydefault starts from 0
	print(m)