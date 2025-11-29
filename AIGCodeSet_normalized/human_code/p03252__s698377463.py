v1 = list('abcdefghijklmnopqrstuvwxyz')
v2 = input()
v3 = input()
v4 = [[] for v5 in v1]
v6 = [[] for v5 in v1]
for v5 in range(0, len(v2)):
    v4[ord(v2[v5]) - ord('a')].append(v5)
for v5 in range(0, len(v3)):
    v6[ord(v3[v5]) - ord('a')].append(v5)
v7 = 'Yes'
for v5 in v4:
    if v5 not in v6:
        v7 = 'No'
        break
print(v7)
