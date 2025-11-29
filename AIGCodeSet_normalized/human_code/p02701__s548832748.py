def f1():
    return [int(k) for v1 in input().split()]
v1 = int(input())
v2 = [0] * v1
for v3 in range(v1):
    v2[v3] = input()
print(len(set(v2)))
