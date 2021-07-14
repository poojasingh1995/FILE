my_dict = {
    'a':50, 
    'b':58,
    'c': 56,
    'd':40,
    'e':100, 
    'f':20,
    } 

list_value=[]
list_key=[]
for i in range(3):
    max_1=0
    for value in my_dict:
        if max_1<my_dict[value]:
            max_1=my_dict[value]
            key=value
    list_value.append(max_1)
    list_key.append(key)
    my_dict.pop(key)
print(list_value)
print(list_key)