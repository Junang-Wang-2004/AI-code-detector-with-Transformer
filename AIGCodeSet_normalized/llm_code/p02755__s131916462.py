v1, v2 = map(int, input().split())
for v3 in range(1, 10001):
    v4 = v3 * 0.08
    v5 = v3 * 0.1
    if int(v4) == v1 and int(v5) == v2:
        print(v3)
        break
else:
    print(-1)
