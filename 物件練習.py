class Person:
    def __init__(self, age):
        self.age = age



age = 38
print 'before assign new value, id=%s'%hex(id(age))
age = 39
print 'after assign new value, id=%s'%hex(id(age))

Person1 = Person(38)
print 'before assign new value, person address=%s'%hex(id(Person1))
print 'before assign new value, person.age address=%s'%hex(id(Person1.age))
Person1.age = 39
print 'after assign new value, person address=%s'%hex(id(Person1))
print 'after assign new value, person.age address=%s'%hex(id(Person1.age))