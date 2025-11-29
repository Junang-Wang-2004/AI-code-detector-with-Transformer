v1 = int(input())
v2 = list(map(int, input().split()))
v2.sort()
v3 = [v2[0]]
for v4 in range(v1 - 1):
    v3.append(v3[v4] + v2[v4 + 1])
v2.sort(reverse=True)
v3.reverse()
v5 = 1
for v4 in range(v1 - 1):
    if v2[v4] > 2 * v2[v4 + 1] and v2[v4] > 2 * v3[v4 + 1]:
        v5 = 0
        print(v4 + 1)
        break
if v5:
    print(v1)
