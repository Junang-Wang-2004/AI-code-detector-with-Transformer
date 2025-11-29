v1, v2, v3 = map(int, input().split())
for v4 in range(1, v1 + 1):
    v5 = v4 * 0.08
    v6 = v4 * 0.1
    if int(v5) == v2 and int(v6) == v3:
        print(v4)
        break
else:
    print(-1)
