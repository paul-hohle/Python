#!/usr/bin/env python

#***************************************************************************************

import random
import math

#***************************************************************************************

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
home_gas=50
condo_repairs=200
food=750
leisure=500
subtotal=leisure+food+condo_repairs+auto_gas+phone+electric+water+hoa+internet+insurance
expenses=subtotal+land+xterra+psu
income=8000

print "HOA              : ",hoa
print "Water            : ",water
print "Internet         : ",internet
print "Phone            : ",phone
print "Electric         : ",electric
print "Repairs/upgrades : ",condo_repairs
print "Insurance        : ",insurance
print "Auto Gas         : ",auto_gas
print "Home Gas         : ",home_gas
print "Leisure          : ",leisure
print "Food             : ",food
print "Subtotal         : ",subtotal
print "Xterra           : ",xterra
print "Land             : ",land
print "PSU              : ",psu
print "Income           : ",income
print "Total            : ",expenses
print "Savings          : ",income-expenses

print math.sqrt(123)
print random.random()

set=[1,2,3,4,5,6,7,8,9,10,11]
rand=random.choice(set)
head = set[0:1]
tail = set[-1]
subset=set[0:3]
divider=" : "
all=set[:]
join = 'head ' + 'tail'
many = '1' * 3
word="word"
letters=list(word)
letters[0]='c'
cord=''.join(letters)

print all,divider,head,divider,tail,divider,rand,divider,subset,divider,join,divider,many, divider,letters,divider,word,divider,cord

sentence="Liberals are children"
words=sentence.split(' ') 
print words
