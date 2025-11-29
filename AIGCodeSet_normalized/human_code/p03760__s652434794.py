from itertools import zip_longest
v1 = input()
v2 = input()
print(''.join([O + E for v3, v4 in zip_longest(v1, v2, fillvalue='')]))
