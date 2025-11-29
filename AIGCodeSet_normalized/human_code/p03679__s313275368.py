v1, v2, v3 = map(int, input().split())
v4 = 0
if v3 > v2:
    v4 = 1
if v3 > v1 + v2:
    v4 = 2
print(['delicious', 'safe', 'dangerous'][v4])
