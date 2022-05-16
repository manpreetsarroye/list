#  Remove empty List from List                
# The original list is: [5, 6, [], 3, [], [], 9]
# List after empty list removal: [5, 6, 3, 9]


s=[5, 6, [], 3, [], [], 9]
p=[]
i=0
while i<len(s):
    if s[i]!=[]:
        p.append(s[i])
    i=i+1
print(p)