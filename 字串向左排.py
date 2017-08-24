# encoding=utf-8
print '%-10s===' % '0123456789'
print '%-10s===' % '56789'
print '%-10s===' % '0123456789'
print '{:<{}s}'.format('12345', 10)
print '{:>{}s}'.format('12345', 10)
print '%-10s===' % '0123456789'
print '%-10s===' % ('測試')
print '%-10s===' % '0123456789'
print '%-10s===' % (u'測試')
print '%-10s===' % '0123456789'
print '{:10s}==='.format('測試')
print '%-10s===' % '0123456789'
print u'{:10s}==='.format(u'測試')