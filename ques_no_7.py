dict=[
     {"first":"1"}, 
     {"second": "2"}, 
     {"third": "1"}, 
     {"four": "5"}, 
     {"five":"5"}, 
     {"six":"9"},
     {"seven":"7"}
] 

k={}
j=[]
for i in range (len(dict)):
     k.update(dict[i])
for i in k.values():
     if i not in j:
          j.append(i)
print(j)
    