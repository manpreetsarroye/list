# O/P=[1, 3, 5, 7, 20, 9, 11, 0, 2, 20, 4, 6, 8, 10, 20, 8, 9, 0, 4, 20, 3, 0]

a=[1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
i=0
s=[]
while i<len(a):
    s.append(a[i])
    if (i+1)%4==0:
        s.append(20)
    i=i+1
print(s)

a=['s', 'd', 'f', 'j', 's', 'a', 'j', 'd', 'f', 'd']
i=0
s=[]
while i<len(a):
    s.append(a[i])
    if (i+1)%3==0:
        s.append('Z')
    i=i+1
print(s)