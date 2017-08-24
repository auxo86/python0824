str1 = 'abcdefg1234567'
list1 = list(str1)
print type(str1), type(list1)
print str1, list1
list1[0] = '*'
print list1
list2 = list(str1)
list2[0:8] = '*'*8
print list2
list3 = list(str1)
del list3[0:8]
list4 = list(str1)
list4[0:8] = []
print list3, list4
