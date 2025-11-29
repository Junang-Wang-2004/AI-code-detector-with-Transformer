v1 = int(input())
v2 = int(input())
v3 = list(map(int, input().split()))
v4 = list(map(int, input().split()))
v5 = list(map(int, input().split()))

def f1(a1):
    for v1 in range(v2):
        if v4[v1] == a1 or v5[v1] == a1:
            continue
        if v3[a1] <= v3[v4[v1]] and v3[a1] <= v3[v5[v1]]:
            return False
    return True
v6 = 0
for v7 in range(v1):
    if f1(v7):
        v6 += 1
print(v6)
