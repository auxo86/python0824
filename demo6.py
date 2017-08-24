str1 = 'abcdefg1234567'
list1 = list(str1)

list1[0:10:2] = '*' * 5
print list1
list2 = list(str1)
list2[::2] = '*' * 7
print list2
list3 = ['a', 'b', 'c']
list3.append('def')
print list3
list4 = ['a', 'b', 'c']
list4.extend('def')
print list4
list5 = ['a', 'b', 'c']
list5 += 'def'
print list5

list6 = [1, 2, 3]
list6 += [4]
print list6
