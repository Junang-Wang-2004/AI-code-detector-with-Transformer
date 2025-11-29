from itertools import *
for v1, v2 in zip(*[iter((len(list(l)) for v3, v4 in groupby(input())))] * 2):
    print('0 ' * ~-v1, -~v1 // 2 + v2 // 2, v1 // 2 + -~v2 // 2, '0 ' * ~-v2)
