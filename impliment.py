# a=[]
# for i in range (5):
#     x=int(input("enter add the iten in the list"))
#     a.append(x)
# x=input("enter value whose freuquensy you want")
# f=a.count(x)
# print("freuquensy",x,"=",f)


a=[]
for i in range (5):
    x=int(input("enter add the iten in the list"))
    a.append(x)
x=input("enter value you find index ")
f=a.index(x)
print("index=",x)