v1 = int(input())
v2 = list(map(int, input().split()))
v3 = len(set(v2))
print(v3 + v3 % 2 - 1)
