v1 = input()
v2 = [[-1] for v3 in range(26)]
for v3 in range(len(v1)):
    v2[ord(v1[v3]) - ord('a')].append(v3)
for v3 in range(26):
    v2[v3].append(len(v1))
v4 = float('inf')
for v3 in range(26):
    v5 = 0
    for v6 in range(1, len(v2[v3])):
        v7 = v2[v3][v6] - v2[v3][v6 - 1] - 1
        v5 = max(v7, v5)
    v4 = min(v5, v4)
print(v4)
