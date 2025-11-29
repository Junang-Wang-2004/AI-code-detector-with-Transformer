v1, *v2 = map(int, open(0).read().split())
v3 = sum((i % 2 for v4 in v2))
print('sfeicrosntd'[v3 > 0::2])
