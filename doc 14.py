

# QUESTION NO 14
    # FIND THE MAXIMIM LENGTH OF LIST
    
l=[[0], [1, 3], [13, 15, 17],[5, 7], [9, 11]]
i=0
max=0
while i<len(l):
    if len(l[i])>max:
        max=len(l[i])
    i=i+1
print(max,l[i-1])
    