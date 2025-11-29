v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v3.sort()
for v4 in range(v2):
    if v3[-1] > 0:
        v3[-1] = 0
    else:
        v3.pop()
print(sum(v3))
