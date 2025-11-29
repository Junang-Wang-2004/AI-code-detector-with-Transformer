import numpy as np

n, a, b = map(int, raw_input().split())
l = []

for i in range(n):
	l.append(input())
ll = np.array(l)
ll.sort()
ll = ll[::-1]

# print count
def solve(count, hpList):
	q = hpList - b * count
	t = q > 0

	if a > b:
		p = (q - 1) / (a - b) + 1
	else:
		p = q
	p = p[p > 0]
	if p.sum() <= count:
		return True
	else:
		return False

l = 1
r = ll[0] / b + 1
while r - l > 1:
	m = (l + r) / 2
	if solve(m, ll):
		r = m
	else:
		l = m

if r == 2:
	if solve(1, ll):
		r = 1

print r
