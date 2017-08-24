# encoding=utf-8

print '%10s' % '0123456789'
print '%10s' % '12345'
print '%10s' % '0123456789' * 2
print '%10s' % '0123456789'
print len('中文')
print '%10s' % '0123456789'
# big5
print '%10s' % '中文'
print '%10s' % '0123456789'
# utf8
print '%10s' % '中文'
print '%10s' % '0123456789'
# 在一個長度10的空間裡向右縮排
print '{:>10}'.format('中文')
print '%10s' % '0123456789'
# 如果是utf-8字串，就要記得前後都要加u
print u'{:>10}'.format(u'中文')
str1 = u'中文'
print repr(str1.encode('utf8'))
print repr(str1.encode('ms950'))
print repr(str1.encode('big5'))

