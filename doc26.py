# l=[4, 6, 4, 3, 3, 4, 3, 4, 6, 6]
# s=[]
# i=0
# while i<len(l):
#     p=l.count(l[i])
#     if p>2 and l[i] not in s:
#         s.append(l[i])
#     i=i+1
# print(s)

t=[4, 5, 5, 5, 3, 8,8,8]
i=0
while i<len(t)-2:
    if t[i]==t[i+1] and t[i+1]==t[i+2]:
        print(t[i])
    i=i+1