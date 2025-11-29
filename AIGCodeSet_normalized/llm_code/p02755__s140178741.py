v1, v2 = map(int, input().split())
for v3 in range(101):
    if int(v3 * 1.08) == v1 and int(v3 * 1.1) == v2:
        print(v3)
        exit(0)
print(-1)
