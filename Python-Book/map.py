#!/usr/bin/env python


#*********************************************************************

dict = {}
dict['meat'] = 'carne'
dict['arroz'] = 'rice'
dict['frijoles'] = 'beans'
dict['aqua'] = 'water'
print dict


nested = {'name' : { 'first' : 'bob', 'last' : 'smith'},
          'jobs' : [ 'dev' , 'manager' ],
          'age'  : 40.5,
          'ss#'  : 464984287,
         }


nested['jobs'].append('medic')

print  nested

# Checking for missing keys
# Indent for multible lines
if not 'key' in nested:
   print ('No such key')
   print ('Please add if needed')

key=nested.get('key',0)
print key

key=nested['key']  if 'key' in nested else 0
print key


keys=list(nested.keys())
keys.sort()
print
print keys
print

for key in keys:
    print(key,'-> ', nested[key])

print
for key in sorted(nested):
    print(key,'-> ', nested[key])

# Delete and reclaim memory
print
nested =0
print nested

