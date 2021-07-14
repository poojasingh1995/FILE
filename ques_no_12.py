dict={}
count=0
for i in range(1,16):
    i=i**2
    count=count+1
    dict.update({count:i})
print(dict)
