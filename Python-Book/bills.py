#!/usr/bin/env python

#***************************************************************************************
# Expenses and income
#
#
#
#


water=45
hoa=277
electric=75
internet=40
phone=125
land=1000
xterra=575
psu=1000
insurance=100+25+30
mpg=20
miles=1250
auto_gas=(miles/mpg)*3
home_gas=75
condo_repairs=200
food=750
etc=600
subtotal=etc+food+condo_repairs+auto_gas+phone+electric+water+hoa+internet+insurance
expenses=subtotal+land+xterra+psu
income=7500

#***************************************************************************************


print "HOA              : ",hoa
print "Water            : ",water
print "Internet         : ",internet
print "Phone            : ",phone
print "Electric         : ",electric
print "Repairs/upgrades : ",condo_repairs
print "Insurance        : ",insurance
print "Auto Gas         : ",auto_gas
print "Home Gas         : ",home_gas
print "ETC              : ",etc
print "Food             : ",food
print "Subtotal         : ",subtotal
print "Xterra           : ",xterra
print "Land             : ",land
print "PSU              : ",psu
print "Income           : ",income
print "Total            : ",expenses
print "Savings          : ",income-expenses

