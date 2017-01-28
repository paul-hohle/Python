#!/usr/bin/env python

#***************************************************************************************

import decimal

#***************************************************************************************

x = decimal.Decimal(1.1)
y = decimal.Decimal(0.3)
z = 3*x-y
print z

decimal.getcontext().prec = 2

x = decimal.Decimal(1.1)
y = decimal.Decimal(0.3)
z = 3*x-y
print z


with decimal.localcontext() as ctx:
   ctx.prec = 3
   x        = decimal.Decimal(1.1)
   y        = decimal.Decimal(0.3)
   z        = 3*x-y
   print z

with decimal.localcontext() as ctx:
   ctx.prec = 4
   x        = decimal.Decimal(1.1)
   y        = decimal.Decimal(0.3)
   z        = 3*x-y
   print z
