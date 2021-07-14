name_dic={'bijender':45,'pooja':90,'deepak':60,'param':20,'anjili':30,'roshini':50}
    
# i=0
# y={}
# for i in name_dic:
#     j=name_dic[i]
#     for i in name_dic:
#         k=name_dic[i]
#         if j>k:
#             y[i]=k
# for i in name_dic:
#     j=name_dic[i]
#     for i in name_dic:
#         k=name_dic[i]
#         if j<k:
#             y[i]=k
# print(y)

i=0
y={}
for i in name_dic:
    j=name_dic[i]
    for i in name_dic:
        k=name_dic[i]
        if j<k:
            y[i]=k
for i in name_dic:
    j=name_dic[i]
    for i in name_dic:
        k=name_dic[i]
        if j>k:
            y[i]=k
print(y)
