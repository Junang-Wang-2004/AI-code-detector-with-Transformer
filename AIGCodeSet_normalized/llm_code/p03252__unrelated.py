v1 = input()
v2 = input()
v3 = [0] * 26
v4 = [0] * 26
for v5 in range(len(v1)):
    v3[ord(v1[v5]) - ord('a')] += 1
    v4[ord(v2[v5]) - ord('a')] += 1
for v5 in range(26):
    if v3[v5] != v4[v5]:
        print('No')
        exit()
v6 = 0
for v5 in range(26):
    if v3[v5] % 2 != 0:
        v6 += 1
if v6 % 2 != 0:
    print('No')
else:
    print('Yes')
