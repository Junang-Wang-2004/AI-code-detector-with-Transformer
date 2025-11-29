v1, v2 = map(int, input().split())
v3 = [str(input()) for v4 in range(v1)]
v3 = sorted(v3)
print(''.join(v3))
