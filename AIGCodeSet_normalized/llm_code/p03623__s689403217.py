v1, v2, v3 = map(int, input().split())
print('A' if abs(v1 - v2) < abs(v1 - v3) else 'B')
