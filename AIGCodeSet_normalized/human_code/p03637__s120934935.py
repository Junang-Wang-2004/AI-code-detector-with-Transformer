N = int(raw_input())
a = [int(i[-2:])for i in raw_input().split(" ")]

c1 = 0
c2 = 0

for ai in a:
    if ai % 2 != 0:
        c1 += 1
    elif ai % 4 == 0:
        c2 += 1
if c1 <= c2:
    print "Yes"
elif c1 - 1 == c2 and N == c1 + c2:
    print "Yes"
else:
    print "No"
