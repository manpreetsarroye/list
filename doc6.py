
# a[i]>b[i], so Alice receives 1 point.
# a[i]=b[i], so nobody receives a point.
# a[i]<b[i], so Bob receives 1 point

a = [17, 122, 23]
b = [31, 24, 187]
i=0
al=0
bo=0
while i<len(a):
    if a[i]>b[i]:
        al=al+1
    elif a[i]==b[i]:
        pass
    elif a[i]<b[i]:
        bo=bo+1
    i=i+1
print(al,bo)