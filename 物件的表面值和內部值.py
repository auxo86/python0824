class Foo(object):
    def __str__(self):
        return 'string format'

    def __repr__(self):
        return 'representation format'


print '%s, %r' % (Foo(), Foo())
print '{0!s}, {0!r}'.format(Foo())
