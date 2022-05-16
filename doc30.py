
l = [2, -7, 5, -64, -14]
pos=0
neg=0
i=0
while i<len(l):
    if l[i]>0:
        pos=pos+1
    else:
        neg=neg+1
    i=i+1
print('pos=',pos)
print('neg=',neg)