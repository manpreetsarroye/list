
a=[]
size=int(input("how many elements you want"))
for i in range (size):
    val=int (input("enter no"))
    a.append(val)
sum=0
for i in range(size):
    sum=sum+a[i]
print('sum of list elements=',sum)  