# encoding=utf-8
import numpy as np

r = 5.0
area = r * r * np.pi
# %後面就是要用來替換的tuple
print 'r=%f, area=%f' % (r, area)
print 'r = %(radius).1f, area = %(area).1f' % \
      {'area': area, 'radius': r}
print 'r = {:.1f}, area = {:.1f}'.format(r, area)
print 'r = {1:.1f}, area = {0:.1f}'.format(area, r)
print 'r = {radius:.1f}, area = {area:.1f}'.\
    format(radius=r, area=area)
