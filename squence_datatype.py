# Squence datatypes
l = [1,2,3,4,5,6] #list datatype
t = (1,2,3,4,5,6) #tuple datatype
r = range(1,6)    #Range datatype

print(l)
print(t)
print(r)

for i in l:
    print(i)
    
for i in t:
    print(i)
    
for i in r:
    print(i)

l.append(7)
print(l)
l.remove(1)
l[0]=30
print(l)
'''
Not add,remove or update in tuple datatype
'''