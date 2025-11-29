v1 = int(input())
v2 = list(map(int, input().split()))
v3 = set(v2)
print(len(v3) if len(v3) % 2 != 0 else len(v3) - 1)
