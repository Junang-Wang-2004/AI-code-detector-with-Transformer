import itertools
import math
v1 = str(input()).split(' ')
v2 = str(input()).split(' ')
v3 = str(input()).split(' ')
v4 = 0
v5 = range(int(v1[0]))
v6 = range(int(v1[1]))
v7 = itertools.combinations(v5, 2)
v8 = itertools.combinations(v6, 2)
for v9 in v7:
    for v10 in v8:
        v4 += (int(xAr[v9[1]]) - int(v2[v9[0]])) * (int(v3[v10[1]]) - int(v3[v10[0]]))
v4 %= 1000000007
print(v4)
