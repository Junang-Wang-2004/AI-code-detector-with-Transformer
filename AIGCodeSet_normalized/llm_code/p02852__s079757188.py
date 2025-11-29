v1, v2 = map(int, input().split())
v3 = input()[::-1]
if v2 >= v1:
    print(v1)
    exit()
v4 = -1
for v5 in reversed(range(1, v2 + 1)):
    if v3[v5] == '0':
        v4 = v5
        break
if v4 == -1:
    print(-1)
    exit()
v6 = [v4]
for v7 in range(v1 // v2):
    v8 = -1
    for v5 in reversed(range(v6[-1] + 1, v6[-1] + v2 + 1)):
        try:
            if v3[v5] == '0':
                v6.append(v5)
                v8 = v5
                break
        except:
            pass
    if v8 == -1:
        print(-1)
        exit()
v9 = [v6[v5 + 1] - v6[v5] for v5 in range(len(v6) - 1)]
print(*v9[::-1], v6[0])
