v1 = 10 ** 9 + 7
v2 = input()
v3 = len(v2)
v4 = [0] * (v3 + 1)
v5 = [0] * (v3 + 1)
v6 = [0] * (v3 + 1)
for v7 in range(v3):
    if v2[v7] == 'A':
        v4[v7 + 1] = v4[v7] + 1
    else:
        v4[v7 + 1] = v4[v7]
    if v2[v7] == 'B':
        v5[v7 + 1] = v5[v7] + 1
    else:
        v5[v7 + 1] = v5[v7]
    if v2[v7] == 'C':
        v6[v7 + 1] = v6[v7] + 1
    else:
        v6[v7 + 1] = v6[v7]
v8 = 0
for v7 in range(v3):
    for v9 in range(v7 + 1, v3):
        for v10 in range(v9 + 1, v3 + 1):
            if v2[v7] == '?' and v2[v9] == '?' and (v2[v10 - 1] == '?'):
                v8 += v4[v7] * v5[v9] * v6[v10] % v1
            elif v2[v7] == '?' and v2[v9] == '?':
                if v2[v10 - 1] == 'A':
                    v8 += v4[v7] * v5[v9] * (v6[v10] - v6[v10 - 1]) % v1
                elif v2[v10 - 1] == 'B':
                    v8 += v4[v7] * (v5[v9] - v5[v9 - 1]) * v6[v10] % v1
                elif v2[v10 - 1] == 'C':
                    v8 += v4[v7] * v5[v9] * (v6[v10] - v6[v10 - 1]) % v1
            elif v2[v7] == '?':
                if v2[v9] == 'A':
                    if v2[v10 - 1] == 'B':
                        v8 += v4[v7] * (v5[v9] - v5[v9 - 1]) * (v6[v10] - v6[v10 - 1]) % v1
                    elif v2[v10 - 1] == 'C':
                        v8 += v4[v7] * (v5[v9] - v5[v9 - 1]) * (v6[v10] - v6[v10 - 1]) % v1
                elif v2[v9] == 'B':
                    if v2[v10 - 1] == 'C':
                        v8 += (v4[v7] - v4[v7 - 1]) * (v5[v9] - v5[v9 - 1]) * (v6[v10] - v6[v10 - 1]) % v1
                elif v2[v9] == 'C':
                    if v2[v10 - 1] == 'A':
                        v8 += (v4[v7] - v4[v7 - 1]) * (v5[v9] - v5[v9 - 1]) * (v6[v10] - v6[v10 - 1]) % v1
            elif v2[v9] == '?':
                if v2[v7] == 'A':
                    if v2[v10 - 1] == 'B':
                        v8 += (v4[v7] - v4[v7 - 1]) * (v5[v9] - v5[v9 - 1]) * (v6[v10] - v6[v10 - 1]) % v1
                    elif v2[v10 - 1] == 'C':
                        v8 += (v4[v7] - v4[v7 - 1]) * (v5[v9] - v5[v9 - 1]) * (v6[v10] - v6[v10 - 1]) % v1
                elif v2[v7] == 'B':
                    if v2[v10 - 1] == 'C':
                        v8 += (v4[v7] - v4[v7 - 1]) * (v5[v9] - v5[v9 - 1]) * (v6[v10] - v6[v10 - 1]) % v1
                elif v2[v7] == 'C':
                    if v2[v10 - 1] == 'A':
                        v8 += (v4[v7] - v4[v7 - 1]) * (v5[v9] - v5[v9 - 1]) * (v6[v10] - v6[v10 - 1]) % v1
            elif v2[v10 - 1] == '?':
                if v2[v7] == 'A':
                    if v2[v9] == 'B':
                        v8 += (v4[v7] - v4[v7 - 1]) * (v5[v9] - v5[v9 - 1]) * (v6[v10] - v6[v10 - 1]) % v1
                    elif v2[v9] == 'C':
                        v8 += (v4[v7] - v4[v7 - 1]) * (v5[v9] - v5[v9 - 1]) * (v6[v10] - v6[v10 - 1]) % v1
                elif v2[v7] == 'B':
                    if v2[v9] == 'C':
                        v8 += (v4[v7] - v4[v7 - 1]) * (v5[v9] - v5[v9 - 1]) * (v6[v10] - v6[v10 - 1]) % v1
                elif v2[v7] == 'C':
                    if v2[v9] == 'A':
                        v8 += (v4[v7] - v4[v7 - 1]) * (v5[v9] - v5[v9 - 1]) * (v6[v10] - v6[v10 - 1]) % v1
            elif v2[v7] == 'A' and v2[v9] == 'B' and (v2[v10 - 1] == 'C'):
                v8 += (v4[v7] - v4[v7 - 1]) * (v5[v9] - v5[v9 - 1]) * (v6[v10] - v6[v10 - 1]) % v1
print(v8)
