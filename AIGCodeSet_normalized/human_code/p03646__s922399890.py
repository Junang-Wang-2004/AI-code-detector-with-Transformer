v1 = int(input())
v2 = v1 // 50
v3 = v1 % 50
v4 = 50
v5 = [49 + v2 - v3] * v4
for v6 in range(v3):
    v5[v6] += 51
print(v4)
print(*v5)
'\ncount=0\nfor i in range(50):\n    if A[i]<50:\n        continue\n    count+=1\n    for j in range(50):\n        if i==j:\n            A[j]-=N\n        else:\n            A[j]+=1\n\nprint(A)\nprint(count)\n'
