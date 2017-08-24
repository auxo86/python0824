a1 = ['a','b','c']
# a2是shallow
a2 = a1
a3 = a1[:]
# a4也是複製一份新的
a4 = list(a1)

print a1, a2, a3, a4
a2[0] = '*'
a2[1] = '$'
a2[2] = '&'
print a1, a2, a3, a4
a3[0] = 'p'
a3[1] = 'q'
a3[2] = 'r'
print a1, a2, a3, a4
