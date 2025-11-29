from collections import Counter
v1 = input()
v2 = Counter(v1)
v3 = v2.most_common()[0][0]
v4 = 0
while len(set(v1)) != 1:
    v5 = ''
    for v6 in range(len(v1) - 1):
        if v1[v6] == v3 or v1[v6 + 1] == v3:
            v5 += v3
        else:
            v5 += v1[v6]
    v4 += 1
    v1 = v5
print(v4)
