#     Count unique values inside a list.
# input_list = [1, 2, 2, 5, 8, 4, 4, 8]
# Count = 5 #because [1,2,5,8,4] are unique values


il = [1, 2, 2, 5, 8, 4, 4, 8]
s=[]
i=0
count=0
while i<len(il):
    if il[i] not in s:
        s.append(il[i])
        count=count+1
    i=i+1
print(s)
print('unique values are',count)