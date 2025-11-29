v1, v2 = map(int, input().split())
v3 = []
if v1 > 10:
    while v1 > 50:
        v3.append('#.' * 50)
        v3.append('#' * 100)
        v1 -= 50
    while v1 > 10:
        v3.append('#.' * 10 + '#' * 80)
        v3.append('#' * 100)
        v1 -= 10
    v2 -= 1
v3.append('.' * 100)
while v2 > 50:
    v3.append('#.' * 50)
    v3.append('.' * 100)
    v2 -= 50
while v2 > 10:
    v3.append('#.' * 10 + '.' * 80)
    v3.append('.' * 100)
    v2 -= 10
if v2 > v1:
    v4 = v2 - v1
    v3.append('#.' * v4 + '..' * (50 - v4))
    v3.append('.' * 100)
    for v5 in range(v1):
        v3.append('#' * 100)
        v3.append('.' * 100)
    v3.pop()
elif v1 > v2:
    if v2 == 0:
        v3.pop()
    v3.append('#' * 100)
    v4 = v1 - v2
    v3.append('.#' * v4 + '##' * (50 - v4))
    v3.append('#' * 100)
    v2 -= 1
    for v5 in range(v2):
        v3.append('.' * 100)
        v3.append('#' * 100)
else:
    for v5 in range(v1):
        v3.append('#' * 100)
        v3.append('.' * 100)
    v3.pop()
print(str(len(v3)) + ' 100')
print('\n'.join(v3))
