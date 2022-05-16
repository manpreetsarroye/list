#     Write a Python program to remove all the values except integer values from a given array of mixed values. 
# Original list: [34.67, 12, -94.89, 'Python', 0, 'C


a= [34.67, 12, -94.89, 'Python', 0, 'C#']
i=0
s=[]
while i<len(a):
    if type(a[i])==int:
        s.append(a[i])
    i=i+1
print(s)