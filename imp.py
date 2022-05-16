# a='s,o,n,i,p,a,r,a,j,a,p,a,t,i,'
# b=a.split(',')
# print(b)
# a='gunu'
# b=list(a)
# print(b)

# a= [50, 40, 23, 70, 56, 12, 5, 10, 7]
# i=1
# while i<len(a):
#     if a[i-1]>a[i]:
#         max=a[i-1]
#     elif a[i-1]<a[i]:
#         max=a[i]
#     i=i+1
# print(max)
# b=a.sort()
# print(a)
# print(a[-1])

# a='a,y,u,s,h,i,p,a,r,m,a,r'
# b=a.split(',')
# print(b)
# a='ayushi parmar'
# b=list(a)
# print(b)

# a=input("enter any name:-")
# b=a.split(a)
# print(b)

# a=[1,2,3,7,4,]
# a.clear()
# print(a)

# del a[3]
# print(a)


# a.remove(4)
# print(a)

# a.sort(reverse=True)
# print(a)

# a.copy()
# print(a)

# print(a.count(4))
# print(min(a))

# marks = [10, 32,42]
# total_marks = 0
# counter = 0
# while counter < len(marks):
#     total_marks = total_marks + marks[counter]
#     counter = counter + 1
# print(total_marks)

# name = ["Savitri", "Phule", "26"]
# # Ab hum iss list ko use karke poora naam (full name) print karna chaste hai
# print(name[0]+name[1]+name[2])
# grocery_list = ['flour','cheese','carrots']
# # Output: 
#=> 0: flour
#=> 1: cheese
#=> 2: carrots
# i=0
# while i<len(grocery_list):
#     print('#=> ',i,':',grocery_list[i])
#     i=i+1
# l=[3,5,4]
# print(l*2)
# l=['py','c','C','c++']
# print(l[-1])
# print(max(l))
# print(list('wel'))
# L=[1,4,2,56,7]
# for i in L:
#     print(i,end=' ')
#     i=i+1
# l=[1,3,5,2,4,6,2]
# l.remove(2)
# print(sum(l))

# a=['my_name_is_preet']
# i=0
# s=' '
# while i<len(a):
#     if a[i]!='_':
#         s=s+a[i]
#     else:
#         pass
#     i=i+1
# print(s)

# a=['my name is manu']
# i=0
# while i<len(a):
#     print(a[i-1])
#     i=i+1

# a=[5,78,90,548]
# i=0
# m=0
# mini=a[i]
# while i<len(a):
#     if a[i]<mini:
#         m=a[i]
#     i=i+1
# print(m)




# ODD AND EVEN

# i=0
# a=input("enter any name:-")
# b=a.split(a)
# print(b)
# while i<9:
#     i=i+2
#     print(i)
#     if i==10:
#         print('odd')
#         i=-1
    
    
    

# a=int(input('enter no:-'))
# i=1
# while i<=a:
#     if i%2==0:
#         print(i)
#     i=i+1

# FIND THE SUM OF NESTED LIST

# a=[[2,3,4],[5,6,7]]
# i=0
# sum=0
# while i<len(a):
#     j=0
#     while j<3:
#         sum=sum+a[i][j]
#         j=j+1
#     i=i+1
# print(sum)
# # print(sum(a[0])+sum(a[1]))

# a=[[4,5,6],[2,3,4],[5,6,7]]

# QUESTION NO 3 

# a=[2,3,4,5,6,7]
# i=0
# s=[]
# while i<len(a)//2:
#     p=a[i]+a[-(i+1)]
#     s.append(p)
#     i=i+1
# print(s)

# a=[4,[7,[3,4,2],5],1]
# print(a[1][1])

# a='i love python programming'
# print(a[0:25:3])

# r=1
# while r<=3:
#     c=1
#     while c<=3:
#         if ((r==1 and c==2) or (r==2 and (c==1 or c==3)) or (r==3 and c==2)):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#         c=c+1
#     print()
#     r=r+1

# r=1
# while r<=4:
#     c=1
#     while c<=4:
#         if ((r==1 and c==1) or (r==2 and (c==1 or c==2)) or (r==3 and (c==1 or c==2 or c==3)) or(r==4 and (c==1 or c==2 or c==3 or c==4))) :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#         c=c+1
#     print()
#     r=r+1

# print(even odd)
# print('even')
# i=0
# while i<9:
#     i=i+2
#     print(i)
#     if i==10:
#         print('odd')
#         i=-1

# a=[4,[7,[3,4,2],5],1]
# print(a[1][1][1])
# a=1234567389123456
# b=float(a)
# print(b)
# x = 10
# y = 50
# if (x ** 2 >100 and y < 100):
#     print(x, y)


a=['m adhu','p ooja','a nju','d eep']
i=0
b=[]
while i<len(a):
    j=0
    c=''
    while j<len(a[i]):
        if a[i][j]==" ":
            pass
        else:
            c=c+a[i][j]
        j=j+1
    b.append(c)
    i=i+1
print(b)


# a=[[4,5,6],[2,3,4],[5,6,7]]
# print((sum(a[0])+sum(a[1])+sum(a[1]))/3)
