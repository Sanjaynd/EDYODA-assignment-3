length=int(input("enter the length of list"))
list=[]
for i in range(length):
	value=input("enter value")
	list.append(value)

maximum=list[0]
for i in list:
	if i>maximum:
		maximum=i
print(maximum)