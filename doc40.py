
# a=[[1, 2, 4], [2, 4, 4], [1, 2]]
# j=0
# s=[]
# while j<len(a[j]):
#     i=0
#     sum=0
#     while i<len(a):
#         sum=sum+a[i][j]
#         i=i+1
#     j=j+1
#     b=sum
#     s.append(b)
# print(s)

list1 = [1,2,3,4,5,6]
list2 = [2,3,1,0,6,7]
s=[]
for i in list1:
    if i not in list2:
        s.append(i)
print(s)