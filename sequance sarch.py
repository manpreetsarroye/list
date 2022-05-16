# a=[]
# i=0
# while i<3:
#     b=int(input("enter no "))
#     a.append(b)
#     i+=1
# c=int(input("which number you wont"))
# j=0
# while j<len(a):
#     if a[j]==c:
#         print("yes it is in list 'and the pzition of no'",j)
#     if c not in a:
#         print("not in list")
#         break
#     j+=1


match=int(input("enter marks"))
science=int(input("enter marks"))
sst=int(input("enter marks"))
phycical=int(input("enter marks"))
history=int(input("enter marks"))
sub=(match+science+sst+phycical+history)*100/5
if sub>90:
    print('grade a' )
elif sub>70:
    print("grade b")
elif sub>60:
    print("grade c")
elif sub>40:
    print("grade d")
else:
    print("fail")