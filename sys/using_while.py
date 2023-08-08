# iterating list using while loop
sizes= [38,40,42,44,46,48,50]
i = 0
while i<=3:
    print(sizes[i])
    i=i+1
# Using len function in while loop
sizes= [38,40,42,44,46,48,50]
i = 0
while i<len(sizes):
    print(sizes[i])
    i=i+1
# using tuple,list and set object
t = ("Rahul","Sonia","Priyanka","DK")
L = ["Rahul","Sonia","Priyanka","DK"]
s = {101,102,103,104,101,102,22,23,22}
i=0
while i<len(t):
    print(t[i])
    i=i+1
a=0
while a<len(L):
    print(L[a])
    a+=1
# While loop is not possible for set object datatype
b=0
while b<len(s):
    print(s[b]) #TypeError: 'set' object is not subscriptable
    b+=1