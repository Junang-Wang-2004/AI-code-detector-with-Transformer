import collections
v1 = int(input())
v2 = collections.deque()
while True:
    v2.appendleft(v1 % 2)
    if v1 % -2 == -1:
        v1 -= 2
    v1 //= -2
    if not v1:
        break
for v3 in v2:
    print(v3, end='')
