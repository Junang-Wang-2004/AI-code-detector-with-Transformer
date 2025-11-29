v1, v2 = map(int, input().split())
v1 = v1 + 13 if v1 == 1 else v1
v2 = v2 + 13 if v2 == 1 else v2
print('Alice' if v1 > v2 else 'Bob' if v1 < v2 else 'Draw')
