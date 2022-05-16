
# QUESTION NO 4

l= [6,1,3,5,6,3,1]
s=[]
i=0
p=1
while i<len(l):
    if l[i] not in s:
        s.append(l[i])
        p=p*l[i]
    i=i+1
print(s)
print(p)
