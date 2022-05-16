
a=[[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
j=0
s=[]
while j<len(a[j]):
    i=0
    sum=0
    while i<len(a[j]):
        sum=sum+a[i][j]
        i=i+1
    j=j+1
    b=sum/len(a)
    s.append(b)
print(s)