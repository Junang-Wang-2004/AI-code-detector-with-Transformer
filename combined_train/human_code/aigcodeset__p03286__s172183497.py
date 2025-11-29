from bisect import bisect_left

def f1():
    return list(map(int, input().split()))
v1 = int(input())
v2 = []
v3 = []
for v4 in range(2 ** 16):
    v2.append(int(('0{}' * 16).format(*list(bin(v4)[2:].zfill(16))), 2))
for v4 in range(2 ** 16):
    v3.append(-int(('{}0' * 16).format(*list(bin(v4)[2:].zfill(16))), 2))
for v5, v6 in enumerate(v3):
    v4 = bisect_left(v2, v1 - v6)
    if v4 == len(v2):
        continue
    v7 = v2[v4]
    if v7 + v6 == v1:
        v8 = [''] * 32
        v8[::2] = list(bin(v5)[2:].zfill(16))
        v8[1::2] = list(bin(v4)[2:].zfill(16))
        print(int(''.join(v8)))
        break
