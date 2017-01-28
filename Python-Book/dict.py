#!/usr/bin/env python

#***************************************************************************************

tab='\t'

#***************************************************************************************

empty                   = {}
dictionary              = empty
dictionary['requerdo']  = 'memories'
dictionary['cebolla']   = 'onion'
dictionary['cacahuate'] = 'peanuts'
dictionary['mani']      = 'peanuts'
dictionary['pan']       = 'bread'
dictionary['acete']     = 'cooking oil'
dictionary['ajo']       = 'garlic'
dictionary['carne']     = 'meat'
dictionary['pollo']     = 'chicken flesh'
dictionary['espinaca']  = 'spinach'
dictionary['sal']       = 'salt'
dictionary['aqua']      = 'water'
dictionary['cerveza']   = 'beer'
dictionary['arroz']     = 'rice'
dictionary['sopa']      = 'soup'
dictionary['zanahoria'] = 'carrot'

for spanish in dictionary:
   print (spanish  + 3*tab + dictionary[spanish])

