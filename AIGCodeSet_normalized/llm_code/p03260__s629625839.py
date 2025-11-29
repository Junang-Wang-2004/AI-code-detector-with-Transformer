v1, v2 = map(int, input().split())
print('NO' if v1 * v2 % 2 == 0 and v1 != 1 and (v2 != 1) else 'YES')
