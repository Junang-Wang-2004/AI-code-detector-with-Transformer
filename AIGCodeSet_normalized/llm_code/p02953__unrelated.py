def f1(a1, a2):
    v1 = a2[0]
    for v2 in range(1, a1):
        if a2[v2] > v1:
            a2[v2] -= 1
        elif a2[v2] < v1:
            return 'No'
        v1 = a2[v2]
    return 'Yes'
v1 = int(input())
v2 = list(map(int, input().split()))
print(f1(v1, v2))
