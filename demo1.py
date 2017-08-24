# encoding=UTF-8

a = 5
b = 3
print a, b
temp = b
b = a
a = temp
print a, b

c, d = 3.14, "2.968K"

print c, d

c, d = d, c

print c, d