#!/usr/bin/env python
'ProtectAndHideX.py -- protect the "x" attribute'

class ProtectAndHideX(object):
    def __init__(self, x):
        self.x = x

        def x():
            def fget(self):
		return ~self.__x

            def fset(self, x):
                assert isinstance(x, int), \
                    '"x" must be an integer!'
                self.__x = ~x

            return locals()

        x = property(**x())

inst = ProtectAndHideX(10)
print 'inst.x has a value of:', inst.x
inst.x = 20
print 'inst.x has a value of:', inst.x
#inst.fset(40)   # sorry!
#print 'inst.x has a value of:', inst.x
inst.x.fset(40)   # sorry!
print 'inst.x has a value of:', inst.x
