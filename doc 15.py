# a=[1,2,7,2,5,0,45,76,9,22,54]
# a.sort()
# print('ascending height',a)
# a.sort(reverse=True)
# print(a)
# b=['manu','soni','deepu','radhika','shalini','gunu']
# b.sort()
# print(b)

a=int(input('enter a no:-'))
i=0
c=str(a)
while i<len(c):
    b=a%10
    a=a//10
    d=b*(10**i)
    x='+'.join(b)
    i=i+1
print(x)
















