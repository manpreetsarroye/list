#     Iterate over both the values in a list and their indice
# grocery_list = ['flour','cheese','carrots']
# Output:
#=> 0: flour
#=> 1: cheese
#=> 2: carrots


a=['flour','cheese','carrots']
b=1
i=0
while i<len(a):
    print("#=>",b,":",a[i])
    i+=1
    b+=1