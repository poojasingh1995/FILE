dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:6}

dict4={}
dict4.update(dic1)
dict4.update(dic2)
dict4.update(dic3)

dic4={}
for i in dic1:
    for j in dic2:
        for k in dic3:
            if i==j:
                a=dic1[i]+dic2[j]
                dic4[i]=a
dict4={}
dict4.update(dic1)
dict4.update(dic2)
dict4.update(dic3)
for r in dic4:
    for l in dic4:
        for l in dict4:
            if r==l:
                dict4[r]=dic4[l]
                break
print(dict4)



