"""
Created on Wed Jan 16 23:07:29 2019

@author: Yamazaki Kenichi
"""
v1 = input()
v2 = [0 for v3 in range(len(v1))]
v4 = [0 for v3 in range(len(v1))]
v5, v6 = (0, 0)
for v3 in range(len(v1)):
    if v1[v3] == 'A':
        v5 += 1
    elif v1[v3] == '?':
        v6 += 1
    v2[v3] = v5
    v4[v3] = v6

def f1(a1):
    if len(a1) == 1:
        return 0
    if a1[len(a1) - 1] == '?':
        return f1(a1[:-1]) * 3 + v2[len(a1) - 1 - 1] * pow(3, v4[len(a1) - 1 - 1]) + v4[len(a1) - 1 - 1] * pow(3, v4[len(a1) - 1 - 1] - 1)
    elif a1[len(a1) - 1] == 'B':
        return f1(a1[:-1]) + v2[len(a1) - 1 - 1] * pow(3, v4[len(a1) - 1 - 1]) + v4[len(a1) - 1 - 1] * pow(3, v4[len(a1) - 1 - 1] - 1)
    else:
        return f1(a1[:-1])
v7 = [f1(v1[:v3 + 1]) for v3 in range(len(v1))]

def f2(a1):
    if len(a1) == 2:
        return 0
    if a1[len(a1) - 1] == '?':
        return f2(a1[:-1]) * 3 + v7[len(a1) - 1 - 1]
    elif a1[len(a1) - 1] == 'C':
        return f2(a1[:-1]) + v7[len(a1) - 1 - 1]
    else:
        return f2(a1[:-1])
print(int(f2(v1) % 1000000007))
