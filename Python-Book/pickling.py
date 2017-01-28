#!/usr/bin/env python

#***************************************************************************************

import pickle

#***************************************************************************************


tab    ='\t'
name   = 'pickled.dta'
binary = 'b'
write  = 'w'
read   = 'r'
empty  = {}
bar    = "****************************************************************************\n"

#***************************************************************************************

original              = empty
original['requerdo']  = 'memories'
original['cebolla']   = 'onion'
original['cacahuate'] = 'peanuts'
original['mani']      = 'peanuts'
original['pan']       = 'bread'
original['acete']     = 'cooking oil'
original['ajo']       = 'garlic'
original['carne']     = 'meat'
original['pollo']     = 'chicken flesh'
original['espinaca']  = 'spinach'
original['sal']       = 'salt'
original['aqua']      = 'water'
original['cerveza']   = 'beer'
original['arroz']     = 'rice'
original['sopa']      = 'soup'
original['zanahoria'] = 'carrot'

file = open(name,write + binary)

pickle.dump(original,file)

file.close()

file = open(name,read + binary)

copy = pickle.load(file)

file.close()


equal = copy == original
same  = copy  is  original

print 'copy is original : ',same
print 'copy == original : ',equal

a='1'

x = ( a + a +
      a + a 
    )

print x

a,b,c,d = 'seqs'

print a,b,c,d

# 3.x only
# e,*f = 'seqs'

# print e,f

# swap
a = 1
b = 2
print a,b
a,b = b,a
print a,b
