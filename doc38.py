
b='https://www.w3resource.com/python-exercises/list/'
a=['.com', '.edu', '.tv']
i=0
while i<len(a):
    if a[i] in b:
        print('true')
    else:
        print('false')
    i=i+1