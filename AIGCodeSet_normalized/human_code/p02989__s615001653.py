v1 = int(input())
v2 = list(map(int, input().split()))
print(sorted(v2)[int(v1 / 2)] - sorted(v2)[int(v1 / 2 - 1)])
