#!/usr/bin/env python

numbers = raw_input().split()

A = int(numbers[0])
B = int(numbers[1])

if A == B :
   print "Draw"
elif A == 1:
   print "Alice"
elif B == 1:
   print "Bob"
elif A > B:
   print "Alice"
elif B > A:
   print "Bob"
