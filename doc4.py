list = [6,1,3,5,6,3,1]
a=[]
i=0
while i<len(list):
    if list[i] not in a:
        a.append(list[i])
    i+=1
print(a)
j=0
sum=1
while j<len(a):
    sum=sum*a[j]
    print(sum)
    

