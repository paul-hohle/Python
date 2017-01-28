#!/usr/bin/env python


import sys

#*********************************************************************


x = set('spam')
y = {'h','a','m'};
z = set('greenspam')

tupleXY = x,y

intersectionXY = x & y
unionXY        = x | y
differenceXY   = x - y
differenceXZ   = x - z
supersetXY     = x > y
subsetXY       = x < y
subsetXZ       = x < z
equalXY        = x == y  # Order neutral

print 'x                 : ',x
print 'y                 : ',y
print 'z                 : ',z
print 'Tuple(x,y)        : ',tupleXY
print 'Union(x,y)        : ',unionXY
print 'Intersection(x,y) : ',intersectionXY
print 'Difference(x,y)   : ',differenceXY
print 'Equal(x,y)        : ',equalXY
print 'Superset(x,y)     : ',supersetXY
print 'Subset(x,y)       : ',subsetXY
print 'Subset(x,z)       : ',subsetXZ
print 'Difference(x,z)   : ',differenceXZ


xyz = [x,y,z]
xyz = set(frozenset(i) for i in xyz)

print 'set(x,y,z)        : ',xyz

# Removing duplicates form a list

duplist    = [1,2,3,4,5,1]
noduplist = list(set(duplist))
print noduplist


# Checking for differences in two lists
l1 = [1,2,3,4,5,7]
l2 = [1,2,3,4,5,6]

l1l2diff = list(set(l1) - set(l2))
l2l1diff = list(set(l2) - set(l1))

# Checking for order neutral equality in two lists

l0     = [1,2,3,4,5,7]
l1     = l0
l2     = [1,2,3,4,5,6]
eql0l1 = set(l0) == set(l1)
eql1l2 = set(l1) == set(l2)

# Various operations

engineers = {'Bob','Sue','Ann','Vic'}
managers  = {'Tom','Sue'}

# Object equality

A=[1,2,3]
B=[1,2,3]
C=[4,5,6]
a=1
b=1
c=3
d=4

print
print
print 'Is bob an engineer?                        : ','bob' in engineers
print 'Engineer managers (Intersection)?          : ',engineers & managers
print 'Non-managerial engineers?                  : ',managers  - engineers
print 'Engineers and managers?                    : ',engineers | managers
print 'Are all managers engineers?                : ',engineers > managers 
print 'Are all engineers managers?                : ',managers  > engineers
print 'Are bob and sue engineers?                 : ',{'bob','sue'} < engineers
print 'Engineers/managers a superset of managers? : ',engineers | managers > managers
print 'Who is in one group, but not both        ? : ',engineers ^ managers
print 'Intersection?                              : ',(engineers | managers) -  (engineers ^ managers)
print 'A,B,C                                      : ',A,B,C
print 'Reference count A,B,C?                     : ',sys.getrefcount(A),sys.getrefcount(B),sys.getrefcount(C)
print 'A is B?                                    : ',A is B
print 'a,b                                        : ',a,b
print 'Reference count a,b?                       : ',sys.getrefcount(a),sys.getrefcount(b)
print 'a is b?                                    : ',a is b
print 'c,d                                        : ',c,d
print 'c is d?                                    : ',c is d

str='1234567'


print str[0::2]
print str[0::]
print str[::]
print str[::-1]

