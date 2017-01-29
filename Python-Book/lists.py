#!/usr/bin/env python

#***************************************************************************************

import random

#***************************************************************************************

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

sentence="Liberals act like children"
words=sentence.split(' ') 
print words

seq=[1,2,3,4]
print seq
seq.pop(2)
print seq
del seq[2]
print seq
hetero=[1,"word"]
print hetero
hetero.sort()
print hetero
hetero.reverse()
print hetero
hetero.sort()
print hetero
hetero.append(1.3)
print hetero

row0=[1,2,3]
row1=[4,5,6]
row2=[7,8,9]

matrix=[row0,row1,row2]
print matrix
print matrix[1]
print matrix[2]
print matrix[0][0]


#********************* Comprehensions *******************************

col0=[row[0] for row in matrix]
col1=[row[1] for row in matrix]
col2=[row[2] for row in matrix]
print "Column 0: ",col0
print "Column 1: ",col1
print "Column 2: ",col2

# Extract odd numbers in row0

odd0=[row[0] for row in matrix if row[0] % 2 != 0]
print odd0

# Extract even numbers in row0

even0=[row[0] for row in matrix if row[0] % 2 == 0]
print even0

# Extract even numbers in row1

even1=[row[1] for row in matrix if row[1] % 2 == 0]
print even1

# Add 1 to items in row1

add1=[row[1] + 1 for row in matrix]
print add1

# Extract left/right diag

lrdiag=[matrix[i][i] for i  in [ 0,1,2]]

print lrdiag

lrdiag=[matrix[i][i] for i  in [ 2,1,0]]

print lrdiag

# Extract right/left diag

rldiag=[matrix[i][2-i] for i  in [ 0,1,2]]

print rldiag

rldiag=[matrix[2-i][i] for i  in [ 0,1,2]]

print rldiag

# Double up characters

letters='letters'
double=[c*2 for c in letters]
print double

range1=list(range(4))

print range1
range2=list(range(-6,7,2))
print range2

range3=[[x **2,x**3] for x in range(4)]
print range3

#********************* Generators *******************************

sums = (sum(row) for row in matrix)

first = next(sums)
second=next(sums)
third=next(sums)

# This should and will fail
# fourth=next(sums)

seq=[first,second,third]
print seq

# Another way using map

seq=list(map(sum,matrix))
print seq

# Sets and dictionaries with comprehnesion syntax

seq={sum(row) for row in matrix}

print seq

l=[]
print l
l.append(1)
l.append(2)
pop=l.pop(-2) 
print l
print pop
print l

