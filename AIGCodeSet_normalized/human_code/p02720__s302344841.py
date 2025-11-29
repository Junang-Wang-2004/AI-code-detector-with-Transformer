from collections import deque
v1 = int(input())
v2 = deque([i for v3 in range(1, 10)])

def f1(a1):
    v1 = a1 % 10
    if 0 <= v1 - 1:
        yield (10 * a1 + v1 - 1)
    yield (10 * a1 + v1)
    if v1 + 1 < 10:
        yield (10 * a1 + v1 + 1)
v4 = 0
while True:
    v5 = v2.popleft()
    for v3 in f1(v5):
        v2.append(v3)
    v4 += 1
    if v4 == v1:
        print(v5)
        break
