list1=["one","two","three","four","five"]

list2=[1,2,3,4,5,]
 
dict={}
for i in range (len(list1)):
    dict.update({list1[i]:list2[i]})
print(dict)