v1 = 0
while 'ABC' in S:
    for v2 in range(len(S) - 2):
        if S[v2:v2 + 3] == 'ABC':
            v1 += 1
    v3 = v3.replace('ABC', 'BCA', 1)
print(v1)
