dic="MISSISSIPI"
dict={}
for i in dic:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]=dict[i]+1
print(dict)
