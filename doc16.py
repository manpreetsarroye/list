# QUESTION NO 16
a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i=1
s=[]
while i<len(a):
    b=a[i]-a[i-1]
    s.append(b)
    i=i+1
print(s)