v1, v2 = map(int, input().split())
for v3 in range(int(min(v1 / 0.08, v2 / 0.1)), int(max((v1 + 1) / 0.08, (v2 + 1) / 0.1))):
    if int(v3 * 0.08) == v1 and int(v3 * 0.1) == v2:
        print(v3)
        exit()
print(-1)
