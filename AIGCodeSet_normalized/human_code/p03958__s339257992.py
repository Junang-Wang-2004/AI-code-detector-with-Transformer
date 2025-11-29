v1, v2 = map(int, input().split())
v3 = sorted(map(int, input().split()))
print(max(2 * v3[-1] - v1 - 1, 0))
