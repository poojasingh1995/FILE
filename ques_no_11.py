my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20,
    'g':2200,
    'h':23400
    }

a=[]
for i in my_dict.values():
    a.append(i)
j=[]
for i in range(5):
    j.append(max(a))
    a.remove(max(a))
print(j)