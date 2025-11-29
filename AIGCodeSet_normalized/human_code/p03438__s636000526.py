n = int(raw_input())
a = map(int, raw_input().split())
b = map(int, raw_input().split())
c = [a[i] - b[i] for i in xrange(n)]
f = -sum(c)
if f < 0:
    print 'No'
    quit()
t = f
for i in xrange(n):
    if c[i] < 0:
        k = (-c[i] + 1) / 2
        t -= k
        c[i] += k * 2
if t < 0:
    print 'No'
    quit()
s = f
for i in xrange(n):
    s -= c[i]
if s < 0:
    print 'No'
    quit()
if t * 2 == s:
    print 'Yes'
else:
    print 'No'
