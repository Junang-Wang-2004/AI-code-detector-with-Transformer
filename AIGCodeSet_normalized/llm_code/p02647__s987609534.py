import math
v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v3.insert(0, 0)
v4 = [0 for v5 in range(len(v3))]
v6 = 1
for v5 in range(v2):
    for v7 in range(1, len(v3)):
        if v3[v7] == 0:
            continue
        v8 = max(1, v7 - v3[v7])
        v9 = min(len(v3), v7 + v3[v7] + 1)
        for v10 in range(v8, v9):
            v4[v10] += 1
    '\n    for l in range(1,int(len(A)/2)):\n\n        if Atemp[l]>abs(len(A)-l):\n            flag*=1\n        else:\n            flag*=0\n\n    for l in range(int(len(A)/2),len(A)):\n        if Atemp[l]>l:\n            flag*=1\n        else:\n            flag*=0\n\n    '
    v3 = v4.copy()
    v4 = [0 for v11 in range(len(v3))]
    '\n    if flag==1:\n        for o in range(1,len(A)):\n            A[o]+=(K-i+1)*len(A)\n            print(o)\n        break\n    flag=1\n    '
for v12 in range(1, len(v3)):
    print(v3[v12], end=' ')
