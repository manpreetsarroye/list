# Given a List, extract all elements whose frequency is greater than K.
# Input: test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], K = 3
# Output: [4, 3]
# Explanation: Both elements occur 4 times.
# Input: test_list = [4, 6, 4, 3, 3, 4, 3, 4, 6, 6], K = 2
# Output: [4, 3, 6]
# Explanation: Occur 4, 3, and 3 times respectivelyl=[4, 6, 4, 3, 3, 4, 3, 4, 6, 6]
l=[4, 6, 4, 3, 3, 4, 3, 4, 6, 6]
s=[]
i=0
while i<len(l):
    p=l.count(l[i])
    if p>2 and l[i] not in s:
        s.append(l[i])
    i=i+1
print(s)