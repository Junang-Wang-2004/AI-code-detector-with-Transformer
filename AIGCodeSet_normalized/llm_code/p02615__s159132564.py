v1 = int(input())
v2 = list(map(int, input().split()))
v2.sort(reverse=True)
v3 = v2[0]
if v1 > 2:
    v4 = (v1 - 2) // 2
    v5 = (v1 - 2) % 2
    v3 += 2 * sum(v2[1:min(1 + v4, len(v2))])
    if v5 == 1 and 1 + v4 < len(v2):
        v3 += v2[1 + v4]
print(v3)
