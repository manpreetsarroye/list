
a=[12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83,56]
i=0
s=[]
while i<len(a)-2:
    p=[]
    p.append(a[i]),p.append(a[i+1]),p.append(a[i+2])
    s.append(p)
    i=i+3
print(s)