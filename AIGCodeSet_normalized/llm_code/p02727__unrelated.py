import heapq
v1, v2, v3, v4, v5 = map(int, input().split())
v6 = list(map(int, input().split()))
v7 = list(map(int, input().split()))
v8 = list(map(int, input().split()))
v6.sort(reverse=True)
v7.sort(reverse=True)
v8.sort(reverse=True)
v9 = heapq.nlargest(v1, v6)
v10 = heapq.nlargest(v2, v7)
v11 = v1 + v2
while v11 > 0 and v8:
    v12 = v8.pop(0)
    if v9 and v12 > v9[-1]:
        v9.pop()
        v9.append(v12)
    elif v10 and v12 > v10[-1]:
        v10.pop()
        v10.append(v12)
    v11 -= 1
v13 = sum(v9) + sum(v10)
print(v13)
