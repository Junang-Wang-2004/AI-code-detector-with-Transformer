"""
Created on Sat May 25 20:54:22 2019

@author: Yamazaki Kenichi
"""
v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = [list(map(int, input().split())) for v5 in range(v2)]
v3.sort()
v4.sort(reverse=True, key=lambda x: x[1])
v6 = 0
for v5 in range(v1):
    if v4[v6][1] > v3[v5]:
        v3[v5] = v4[v6][1]
        v4[v6][0] -= 1
        if v4[v6][0] == 0:
            v6 += 1
        if v6 >= v2:
            break
    else:
        break
print(sum(v3))
