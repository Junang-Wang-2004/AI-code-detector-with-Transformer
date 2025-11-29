import math
v1, v2 = map(int, input().split())
v3 = math.ceil((v1 - 1) / 50)
v4 = (v1 - 1) // 50
v5 = math.ceil((v2 - 1) / 50)
v6 = (v2 - 1) // 50
if v3 == 0:
    v3 = 1
if v5 == 0:
    v5 = 1
v7 = (v1 - 1) % 50
v8 = (v2 - 1) % 50
if v3 == v4:
    v7 = 50
    v4 -= 1
if v5 == v6:
    v8 = 50
    v6 -= 1
print('100 ', (v3 + v5) * 2)
for v9 in range(50):
    print('.#' * v4 + ('.#' if v9 < v7 else '##') + '.#' * v6 + ('.#' if v9 < v8 else '..'))
    print('##' * v3 + '..' * v5)
