import sys
sys.stdin.readline()
v1 = list(map(int, sys.stdin.readline().split()))
v2 = 0
while True:
    v3 = False
    for v4 in range(len(v1)):
        if v1[v4] % 2 == 0:
            v1[v4] //= 2
            v3 = True
            v2 += 1
        elif v1[v4] * 3 <= 1000000000:
            v1[v4] *= 3
            v3 = True
            v2 += 1
    if not v3:
        break
print(v2)
