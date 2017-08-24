# encoding=UTF-8
str1 = 'abcde12345'
str1 *= 2
print str1
print str1[0], str1[2], str1[10]
print str1[-1], str1[-5], str1[-7]

# slice 包含起點但是不包含終點。也可以不寫起點跟終點
print str1[0:5], str1[5:8]
print str1[:5], str1[5:]
print len(str1)

str2 = 'www.uuu.com.tw'
print type(str2)
result = str2.split('.')
print type(result), result
# 可以用某個字串join list的元素
print '#'.join(result)