#!usr/bim/python
#! -*- coding: utf-8 -*-

hw = raw_input()
h,w = hw.split()
h = int(h)
w = int(w)

al = [chr(i) for i in range(97, 97+26)]

a = ""
for i in range(h):
    s = raw_input()
    a += s

#print a

#print al

c = []

for x in al:
    count = a.count(x)
    c.append(count)

#print c

status1 = 0
status2 = 0
for x in c:
    if x % 4 == 0:
        pass
    elif x % 2 == 0:
        status1 += 1
    else:
        status2 += 1

ans = 0
if h % 2 == 0 and w % 2 == 0:
    if status1 > 0 or status2 > 0:
        ans = 1
elif h % 2 == 0:
    if status2 > 0:
        ans = 1
    elif status1 > h / 2:
        ans = 1
elif w % 2 == 0:
    if status2 > 0:
        ans = 1
    elif status1 > w / 2:
        ans = 1
else:
    if status2 > 1:
        ans = 1
    elif status1 > h / 2 + w / 2:
        ans = 1

if ans == 0:
    print "Yes"
else:
    print "No"
