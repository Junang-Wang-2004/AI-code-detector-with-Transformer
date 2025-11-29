from operator import itemgetter
from itertools import chain
v1 = int(input())
v2 = []
v3 = []
for v4 in range(v1):
    v5 = input()
    v6 = 0
    v7 = 0
    for v8 in v5:
        if v8 == '(':
            v7 += 1
        else:
            v7 -= 1
        v6 = min(v6, v7)
    if v7 >= 0:
        v2.append((v6, v7))
    else:
        v3.append((v6, v7))
v2.sort(key=itemgetter(0), reverse=True)
v3.sort(key=lambda x: x[0] - x[1])
v9 = 0
for v4, (v6, v7) in enumerate(chain(v2, v3)):
    if v9 + v6 < 0:
        v10 = 'No'
        break
    v9 += v7
else:
    v10 = 'Yes' if v9 == 0 else 'No'
print(v10)
