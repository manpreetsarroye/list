
a=[[1,2,3],[4,5,6],[9,8,9]]
i=0
j=0
sum=0
p=0
r=2
sum=0
sum1=0
while i<len(a):
    sum=sum+a[i][j]
    sum1=sum1+a[p][r]
    i=i+1
    j=j+1
    p=p+1
    r=r-1
print(sum)
print(sum1)
print(abs(sum-sum1))