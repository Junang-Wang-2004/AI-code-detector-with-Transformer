v1 = [0] * 26
v2 = input()
v3 = len(v2)
for v4 in range(v3):
    v1[ord(v2[v4]) - ord('a')] += 1
print(v3 * (v3 - 1) // 2 - sum([v4 * (v4 - 1) // 2 for v4 in v1]) + 1)
