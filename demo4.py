str1 = 'abcde12345'
str1 *= 2
print 'abc' in str1, 'abcdef' in str1
print 'xyz' + 'abc', 'xyz'*3, 3*'xyz'
print str1[0:10:2]
print len(str1[0:10:2])
print min(str1)
print max(str1)
print str1.index('a'), str1.index('3')

# print str1.index('p')
print str1.count('c'), str1.count('g')

str2 = 'www.uuu.edu.tw'
str3 = str2.replace('.', '*')
print str3
