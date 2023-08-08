# Logical operator
x = True
y = False
a = x or x # a is true
b = x or y # b is true
c = y or x # c is true
d = y or y # d is false
e = x and x # e is true
f = x and y # f is false
g = y and x # g is false
h = y and y # h is false
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)