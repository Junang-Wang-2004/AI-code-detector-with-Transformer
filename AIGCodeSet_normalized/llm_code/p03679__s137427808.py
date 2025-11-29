v1, v2, v3 = map(int, input().split())
print('delicious' if 0 <= v3 - v2 <= v1 else 'dangerous' if v1 < v3 - v2 else 'safe')
