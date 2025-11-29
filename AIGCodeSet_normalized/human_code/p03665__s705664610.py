v1, v2, *v3 = map(int, open(0).read().split())
print(2 ** (~-v1) * (any((x % 2 for v4 in v3)) or -2 * ~-v2))
