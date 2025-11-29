v1 = int(input())
v2 = [int(x) for v3 in input().split()]

def f1(a1):
    for v1 in a1:
        if v1 % 2 != 0:
            return False
    return True
v4 = 0
while f1(v2):
    for v5 in range(len(v2)):
        v2[v5] = v2[v5] // 2
    v4 += 1
print(v4)
